.PHONY: help run-local run-dev run-docker build-run stop build logs clean prune check-colima setup-dev test

COLOR_RESET  = \033[0m
COLOR_CYAN   = \033[36m
COLOR_GREEN  = \033[32m
COLOR_YELLOW = \033[33m
COLOR_BOLD   = \033[1m

# Detects whether the system uses 'docker compose' (v2 plugin) or 'docker-compose' (v1 CLI)
DOCKER_COMPOSE := $(shell if docker compose version >/dev/null 2>&1; then echo "docker compose"; elif command -v docker-compose >/dev/null 2>&1; then echo "docker-compose"; else echo "docker compose"; fi)

help: ## Display this help menu
	@echo "$(COLOR_BOLD)Prolixo - Local Management & Development$(COLOR_RESET)"
	@echo ""
	@echo "$(COLOR_YELLOW)Available commands:$(COLOR_RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(COLOR_CYAN)%-15s$(COLOR_RESET) %s\n", $$1, $$2}'

setup-dev: ## Create Python virtual environment and install requirements
	@echo "$(COLOR_CYAN)🐍 Setting up Python virtual environment in api/.venv...$(COLOR_RESET)"
	@if [ ! -d "api/.venv" ]; then python3 -m venv api/.venv; fi
	@api/.venv/bin/pip install -r api/requirements.txt
	@echo "$(COLOR_GREEN)✅ venv ready at api/.venv.$(COLOR_RESET)"

test: ## Run automated backend test suite (pytest)
	@echo "$(COLOR_CYAN)🧪 Running automated backend test suite (pytest)...$(COLOR_RESET)"
	@if [ ! -d "api/.venv" ]; then $(MAKE) setup-dev; fi
	@cd api && .venv/bin/pytest -v

run-local: ## Fast native local dev server (API via venv + Frontend via next dev, ~1s start)
	@if [ ! -d "api/.venv" ]; then \
		echo "$(COLOR_YELLOW)⚡ Initializing Python venv for native mode...$(COLOR_RESET)"; \
		$(MAKE) setup-dev; \
	fi
	@echo "$(COLOR_BOLD)🚀 Starting Prolixo natively in DEV mode (API + Frontend)...$(COLOR_RESET)"
	@echo "$(COLOR_GREEN)=================================================================$(COLOR_RESET)"
	@echo "  📌 $(COLOR_BOLD)Frontend Web:$(COLOR_RESET)       $(COLOR_CYAN)http://localhost:3000$(COLOR_RESET)"
	@echo "  📌 $(COLOR_BOLD)Swagger API Docs:$(COLOR_RESET)   $(COLOR_CYAN)http://localhost:8000/docs$(COLOR_RESET)"
	@echo "  📌 $(COLOR_BOLD)ReDoc API Docs:$(COLOR_RESET)     $(COLOR_CYAN)http://localhost:8000/redoc$(COLOR_RESET)"
	@echo "$(COLOR_GREEN)=================================================================$(COLOR_RESET)"
	@echo "$(COLOR_YELLOW)📡 Streaming live dev logs (Press Ctrl+C to stop both services)...$(COLOR_RESET)"
	@echo ""
	@trap 'kill 0' INT TERM EXIT; \
		(cd api && .venv/bin/python run.py) & \
		(cd frontend && npm run dev) & \
		wait

run-dev: run-local ## Alias for run-local

check-colima:
	@if command -v colima >/dev/null 2>&1; then \
		if ! colima status >/dev/null 2>&1; then \
			echo "$(COLOR_CYAN)⚡ Starting Colima in the background...$(COLOR_RESET)"; \
			colima start; \
		fi \
	fi

run-docker: check-colima ## Start Docker containers via Colima / Docker Compose
	@echo "$(COLOR_BOLD)🚀 Starting Docker containers (API + Frontend)...$(COLOR_RESET)"
	@$(DOCKER_COMPOSE) up -d
	@echo ""
	@echo "$(COLOR_GREEN)=================================================================$(COLOR_RESET)"
	@echo "$(COLOR_BOLD)🎉 Prolixo containers running successfully!$(COLOR_RESET)"
	@echo "$(COLOR_GREEN)=================================================================$(COLOR_RESET)"
	@echo "  📌 $(COLOR_BOLD)Frontend Web:$(COLOR_RESET)       $(COLOR_CYAN)http://localhost:3000$(COLOR_RESET)"
	@echo "  📌 $(COLOR_BOLD)Swagger API Docs:$(COLOR_RESET)   $(COLOR_CYAN)http://localhost:8000/docs$(COLOR_RESET)"
	@echo "  📌 $(COLOR_BOLD)ReDoc API Docs:$(COLOR_RESET)     $(COLOR_CYAN)http://localhost:8000/redoc$(COLOR_RESET)"
	@echo "$(COLOR_GREEN)=================================================================$(COLOR_RESET)"
	@echo "$(COLOR_YELLOW)📡 Streaming logs in real time (Press Ctrl+C to stop and shut down)...$(COLOR_RESET)"
	@echo ""
	-@trap '$(MAKE) stop' INT TERM; $(DOCKER_COMPOSE) logs -f || true

build-run: check-colima ## Force rebuild Docker images and start containers
	@echo "$(COLOR_BOLD)🏗️ Rebuilding Docker containers (API + Frontend)...$(COLOR_RESET)"
	@$(DOCKER_COMPOSE) up -d --build
	@echo ""
	@echo "$(COLOR_GREEN)=================================================================$(COLOR_RESET)"
	@echo "$(COLOR_BOLD)🎉 Prolixo containers rebuilt & running successfully!$(COLOR_RESET)"
	@echo "$(COLOR_GREEN)=================================================================$(COLOR_RESET)"
	@echo "  📌 $(COLOR_BOLD)Frontend Web:$(COLOR_RESET)       $(COLOR_CYAN)http://localhost:3000$(COLOR_RESET)"
	@echo "  📌 $(COLOR_BOLD)Swagger API Docs:$(COLOR_RESET)   $(COLOR_CYAN)http://localhost:8000/docs$(COLOR_RESET)"
	@echo "  📌 $(COLOR_BOLD)ReDoc API Docs:$(COLOR_RESET)     $(COLOR_CYAN)http://localhost:8000/redoc$(COLOR_RESET)"
	@echo "$(COLOR_GREEN)=================================================================$(COLOR_RESET)"
	@echo "$(COLOR_YELLOW)📡 Streaming logs in real time (Press Ctrl+C to stop and shut down)...$(COLOR_RESET)"
	@echo ""
	-@trap '$(MAKE) stop' INT TERM; $(DOCKER_COMPOSE) logs -f || true

stop: ## Stop Docker containers, prune unused images, and stop Colima
	@echo ""
	@echo "$(COLOR_YELLOW)🛑 Stopping Prolixo containers...$(COLOR_RESET)"
	@$(DOCKER_COMPOSE) down 2>/dev/null || true
	@echo "$(COLOR_YELLOW)🧹 Pruning dangling images to free disk space...$(COLOR_RESET)"
	@docker image prune -f 2>/dev/null || true
	@if command -v colima >/dev/null 2>&1; then \
		if colima status >/dev/null 2>&1; then \
			echo "$(COLOR_YELLOW)🔌 Stopping Colima...$(COLOR_RESET)"; \
			colima stop; \
		fi \
	fi

build: check-colima ## Build Docker images without starting services
	@echo "$(COLOR_CYAN)🏗️ Building Docker images (API + Frontend)...$(COLOR_RESET)"
	@$(DOCKER_COMPOSE) build

logs: ## Stream live container logs
	@$(DOCKER_COMPOSE) logs -f

prune: ## Prune dangling images and orphan containers to free disk space
	@echo "$(COLOR_YELLOW)🧹 Pruning dangling images (docker image prune)...$(COLOR_RESET)"
	@docker image prune -f
	@docker system prune -f

clean: prune ## Remove containers, images, and orphaned volumes
	@echo "$(COLOR_YELLOW)🧹 Cleaning Docker environment...$(COLOR_RESET)"
	@$(DOCKER_COMPOSE) down --volumes --remove-orphans 2>/dev/null || true

passo-curto: ## Automated short step: switch/create branch, stage changes, commit locally (make passo-curto BRANCH=... MSG=...)
	@bash scripts/git_workflow.sh curto "$(BRANCH)" "$(MSG)"

passo-longo: ## Automated long step: switch/create branch, commit, push, and open PR (make passo-longo BRANCH=... MSG=... [TITLE=...] [BODY=...])
	@bash scripts/git_workflow.sh longo "$(BRANCH)" "$(MSG)" "$(TITLE)" "$(BODY)"


