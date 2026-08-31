import time
import pytest
from fastapi import FastAPI, Request, Depends
from fastapi.testclient import TestClient
from app.limiter import InMemoryRateLimiter, INTERNAL_SECRET


def create_test_app(limiter: InMemoryRateLimiter):
    test_app = FastAPI()

    @test_app.get("/test-endpoint")
    def endpoint(request: Request, _=Depends(limiter.check_rate_limit)):
        return {"ok": True}

    return test_app


@pytest.fixture(autouse=True)
def clean_records():
    yield


def test_direct_api_rate_limit_exceeded():
    limiter = InMemoryRateLimiter(frontend_limit=10, direct_limit=3, window_seconds=60)
    app = create_test_app(limiter)
    client = TestClient(app)

    # First 3 requests succeed
    for _ in range(3):
        res = client.get("/test-endpoint")
        assert res.status_code == 200
        assert res.json() == {"ok": True}

    # 4th request exceeds limit
    res = client.get("/test-endpoint")
    assert res.status_code == 429
    assert "Retry-After" in res.headers
    data = res.json()
    assert data["detail"]["error"] == "too_many_requests"
    assert data["detail"]["retry_after"] > 0


def test_frontend_rate_limit_with_internal_secret():
    limiter = InMemoryRateLimiter(frontend_limit=5, direct_limit=2, window_seconds=60)
    app = create_test_app(limiter)
    client = TestClient(app)

    headers = {
        "X-Internal-Secret": INTERNAL_SECRET,
        "X-Forwarded-User-IP": "203.0.113.195",
    }

    # Frontend gets up to 5 requests
    for _ in range(5):
        res = client.get("/test-endpoint", headers=headers)
        assert res.status_code == 200

    # 6th request fails
    res = client.get("/test-endpoint", headers=headers)
    assert res.status_code == 429
    assert int(res.headers["Retry-After"]) >= 1


def test_frontend_and_direct_counters_are_isolated_for_same_ip():
    limiter = InMemoryRateLimiter(frontend_limit=3, direct_limit=2, window_seconds=60)
    app = create_test_app(limiter)
    client = TestClient(app)

    headers_direct = {"X-Forwarded-For": "198.51.100.1"}
    headers_frontend = {
        "X-Internal-Secret": INTERNAL_SECRET,
        "X-Forwarded-User-IP": "198.51.100.1",
    }

    # Exhaust direct limit (2)
    assert client.get("/test-endpoint", headers=headers_direct).status_code == 200
    assert client.get("/test-endpoint", headers=headers_direct).status_code == 200
    assert client.get("/test-endpoint", headers=headers_direct).status_code == 429

    # Frontend quota for the same IP is independent and still available
    assert client.get("/test-endpoint", headers=headers_frontend).status_code == 200
    assert client.get("/test-endpoint", headers=headers_frontend).status_code == 200
    assert client.get("/test-endpoint", headers=headers_frontend).status_code == 200
    assert client.get("/test-endpoint", headers=headers_frontend).status_code == 429


def test_rate_limit_resets_after_window():
    # 1 second window
    limiter = InMemoryRateLimiter(frontend_limit=2, direct_limit=2, window_seconds=1)
    app = create_test_app(limiter)
    client = TestClient(app)

    assert client.get("/test-endpoint").status_code == 200
    assert client.get("/test-endpoint").status_code == 200
    assert client.get("/test-endpoint").status_code == 429

    # Wait for the 1-second window to expire
    time.sleep(1.1)

    # Should be allowed again
    assert client.get("/test-endpoint").status_code == 200
