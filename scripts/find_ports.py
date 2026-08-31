import socket
import sys


def find_free_port(start: int = 8000, attempts: int = 100) -> int:
    for port in range(start, start + attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    return start


if __name__ == "__main__":
    starts = [int(arg) for arg in sys.argv[1:]] if len(sys.argv) > 1 else [8000, 3000]
    ports = [find_free_port(start) for start in starts]
    print(" ".join(str(p) for p in ports))
