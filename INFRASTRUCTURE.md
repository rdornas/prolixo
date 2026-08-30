# Infrastructure Documentation

This document maintains the canonical specification for the infrastructure architecture, containerization strategy, orchestration rules, and local runtime management for the Prolixo project.

---

## 1. Stack Overview

The infrastructure stack is designed for lightweight, containerized execution using **Docker** and **Docker Compose**, with support for macOS container runtimes (such as **Colima**).

```
                      +-----------------------------+
                      |         Local Machine       |
                      |  (Colima / Docker Engine)   |
                      +--------------+--------------+
                                     |
                         Docker Compose Network
                                     |
            +------------------------+------------------------+
            |                                                 |
            v                                                 v
  +--------------------+                            +--------------------+
  |  prolixo-frontend  |                            |    prolixo-api     |
  | (Node 20 Alpine)   | --- depends_on (build) --->| (Python 3.12 Slim) |
  |     Port: 3000     |                            |     Port: 8000     |
  +--------------------+                            +--------------------+
```

---

## 2. Containerized Services

### 2.1 API Service (`prolixo-api`)
* **Source Path**: [`api/`](api)
* **Dockerfile**: [`api/Dockerfile`](api/Dockerfile)
* **Base Image**: `python:3.12-slim`
* **Exposed Port**: `8000` (mapped to host `8000:8000`)
* **Environment Variables**:
  * `PYTHONDONTWRITEBYTECODE=1`: Disables `.pyc` creation.
  * `PYTHONUNBUFFERED=1`: Ensures unbuffered standard stdout/stderr streams.
  * `PORT=8000`: Application listening port.
* **Process Manager**: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
* **Restart Policy**: `unless-stopped`

### 2.2 Frontend Service (`prolixo-frontend`)
* **Source Path**: [`frontend/`](frontend)
* **Dockerfile**: [`frontend/Dockerfile`](frontend/Dockerfile) (Multi-stage build)
  * **Stage 1 (builder)**: `node:20-alpine`, runs `npm ci --legacy-peer-deps` and `npm run build`.
  * **Stage 2 (runner)**: `node:20-alpine`, copies built Next.js artifacts (`.next`, `public`, `node_modules`).
* **Exposed Port**: `3000` (mapped to host `3000:3000`)
* **Environment Variables**:
  * `NODE_ENV=production`
* **Process Manager**: `npm start`
* **Dependencies**: Depends on `api` service.
* **Restart Policy**: `unless-stopped`

---

## 3. Orchestration Specification

Orchestration is defined in [`docker-compose.yml`](docker-compose.yml):

* **Service Declarations**: `api`, `frontend`
* **Network Mode**: Default bridge network created by Docker Compose.
* **Port Bindings**:
  * Host `3000` -> Container `3000` (Frontend)
  * Host `8000` -> Container `8000` (API)

---

## 4. Environment & Service Management (`Makefile`)

The project uses a [`Makefile`](Makefile) as the single control plane for local operations:


### Key Automation & Mechanics
* **CLI Auto-Detection**: Automatically detects `docker compose` (v2 plugin) vs `docker-compose` (v1 CLI).
* **Colima Lifecycle Check**: `check-colima` automatically checks if `colima` is installed and starts the background daemon if available.

### Cross-Platform Compatibility
* **Linux**: Linux systems run Docker Engine natively. The `Makefile` uses conditional checks (`command -v colima`), so on Linux systems where `colima` is not installed, all Colima steps are silently skipped. A Linux user simply needs standard Docker (`docker` + `docker compose`) installed and can run `make run-local` directly (or `docker compose up -d --build`).
* **macOS**: On macOS, Colima can be used as a lightweight open-source container runtime alternative to Docker Desktop. If `colima` is installed, `make run-local` will auto-start it if it is stopped. If using Docker Desktop or OrbStack without Colima, the check safely bypasses Colima.
* **Windows (WSL2)**: Works seamlessly via Docker Desktop (WSL2 backend) or native Linux Docker Engine inside WSL2 distributions using standard `make` or `docker compose` commands.

### Management Commands
| Command | Action |
| :--- | :--- |
| `make run-local` | Launches fast native development server (API via `api/.venv` + Frontend via `next dev`) in ~1s. Auto-initializes `api/.venv` if missing. |
| `make run-dev` | Alias for `make run-local`. |
| `make run-docker` | Checks Colima status (if present), starts Docker containers using existing built images (`docker compose up -d`), and streams logs. |
| `make build-run` | Force rebuilds Docker images (`docker compose up -d --build`), launches containers, and streams logs. |
| `make setup-dev` | Creates Python virtual environment at `api/.venv` and installs dependencies (`api/requirements.txt`). |
| `make stop` | Stops container stack (`docker compose down`), prunes dangling images, and stops Colima if active. |
| `make build` | Builds Docker images for API and Frontend without starting services. |
| `make logs` | Streams live container logs. |
| `make prune` | Prunes dangling images and unused Docker system objects. |
| `make clean` | Removes containers, images, and orphaned volumes. |


---

## 5. Endpoints Reference (Local Runtime)

* **Frontend Web Application**: [http://localhost:3000](http://localhost:3000)
* **Swagger API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc API Documentation**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
