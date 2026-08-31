import os
import time
import math
from typing import Dict, List, Tuple
from fastapi import Request, HTTPException, status

INTERNAL_SECRET = os.getenv("INTERNAL_API_SECRET", "prolixo_internal_client_secret")
RATE_LIMIT_FRONTEND = int(os.getenv("RATE_LIMIT_FRONTEND", "30"))  # req / window
RATE_LIMIT_DIRECT = int(os.getenv("RATE_LIMIT_DIRECT", "10"))      # req / window
RATE_LIMIT_WINDOW = int(os.getenv("RATE_LIMIT_WINDOW", "60"))      # in seconds


class InMemoryRateLimiter:
    """
    Lightweight, zero-dependency in-memory sliding-window rate limiter.
    Differentiates between verified frontend clients and direct public API requests.
    """

    def __init__(
        self,
        frontend_limit: int = RATE_LIMIT_FRONTEND,
        direct_limit: int = RATE_LIMIT_DIRECT,
        window_seconds: int = RATE_LIMIT_WINDOW,
    ):
        self.frontend_limit = frontend_limit
        self.direct_limit = direct_limit
        self.window_seconds = window_seconds
        self._records: Dict[str, List[float]] = {}

    def get_client_key(self, request: Request) -> Tuple[str, bool]:
        """
        Determines the client IP and whether the request originates from a trusted frontend.
        Returns: (rate_limit_key, is_trusted)
        """
        secret = request.headers.get("X-Internal-Secret")
        is_trusted = bool(secret and secret == INTERNAL_SECRET)

        if is_trusted:
            user_ip = request.headers.get("X-Forwarded-User-IP")
            if not user_ip:
                forwarded = request.headers.get("X-Forwarded-For")
                user_ip = (
                    forwarded.split(",")[0].strip()
                    if forwarded
                    else (request.client.host if request.client else "127.0.0.1")
                )
            return f"{user_ip}:frontend", True
        else:
            forwarded = request.headers.get("X-Forwarded-For")
            direct_ip = (
                forwarded.split(",")[0].strip()
                if forwarded
                else (request.client.host if request.client else "127.0.0.1")
            )
            return f"{direct_ip}:direct", False

    def check_rate_limit(self, request: Request) -> None:
        """
        Validates whether the current request is within rate limits.
        Raises HTTPException(429) if the limit is exceeded.
        """
        key, is_trusted = self.get_client_key(request)
        max_allowed = self.frontend_limit if is_trusted else self.direct_limit
        now = time.time()
        cutoff = now - self.window_seconds

        timestamps = [ts for ts in self._records.get(key, []) if ts > cutoff]

        if len(timestamps) >= max_allowed:
            earliest = timestamps[0]
            retry_after = max(1, math.ceil(earliest + self.window_seconds - now))
            self._records[key] = timestamps
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail={
                    "error": "too_many_requests",
                    "message": f"Rate limit exceeded. Please try again in {retry_after} seconds.",
                    "retry_after": retry_after,
                },
                headers={"Retry-After": str(retry_after)},
            )

        timestamps.append(now)
        self._records[key] = timestamps

    def reset(self) -> None:
        """Clears all stored rate limit records (for testing)."""
        self._records.clear()


limiter = InMemoryRateLimiter()
