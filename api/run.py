import os
import socket
import uvicorn


def is_port_free(port: int, host: str = "0.0.0.0") -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host, port))
            return True
        except OSError:
            return False


def find_available_port(start_port: int = 8000, max_attempts: int = 100, host: str = "0.0.0.0") -> int:
    for port in range(start_port, start_port + max_attempts):
        if is_port_free(port, host):
            return port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, 0))
        return s.getsockname()[1]


def get_target_port() -> int:
    env_port = os.getenv("API_PORT") or os.getenv("PORT")
    if env_port and env_port.isdigit():
        target = int(env_port)
        if is_port_free(target):
            return target
        return find_available_port(start_port=target)
    return find_available_port(start_port=8000)


if __name__ == "__main__":
    port = get_target_port()
    print(f"Starting Prolixo API at http://localhost:{port}")
    print(f"Swagger documentation available at http://localhost:{port}/api/docs")
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
