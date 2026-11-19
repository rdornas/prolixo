# Prolixo - Natural Multilanguage Placeholder Text Generator

**Prolixo** is a professional, multilingual web application for generating placeholder text across three distinct output modes: **Words**, **Sentences**, and **Paragraphs**. The project is designed to be minimalist, robust, and elegant, built with **Go (`net/http` standard library)** on the backend API and **Next.js** on the frontend with **Radix UI** primitives styled via the **`tailwindcss-radix`** plugin.

The text generation engine is **100% algorithmic, local, and deterministic-statistical**, executing entirely offline in the API without requiring external third-party AI APIs or internet connectivity.

---

## 📂 Project Structure

The project directory layout is organized as follows:

```text
prolixo/
├── INFRASTRUCTURE.md           # Canonical infrastructure architecture & Makefile specification
├── Makefile                    # Single control plane for local automation (native & Docker)
├── README.md                   # Project documentation & reference guide
├── roadmap.md                  # Project milestones & completed roadmap
│
├── api/                        # Go Backend API (zero external dependencies)
│   ├── cmd/
│   │   └── server/
│   │       └── main.go         # Local & Docker HTTP server entrypoint
│   ├── index.go                # Vercel Go Serverless Function entrypoint
│   ├── go.mod                  # Go module definition (Go 1.22+)
│   ├── Dockerfile              # Multi-stage Go -> Alpine container build
│   └── internal/
│       ├── limiter/            # In-memory sliding-window rate limiter & tests
│       ├── models/             # Request/response structs, validation & tests
│       ├── server/             # HTTP handlers, CORS, OpenAPI/Swagger & tests
│       └── generator/          # Statistical natural language generation engine
│           ├── dicts.go        # Embedded JSON lexicon loader (embed.FS)
│           ├── engine.go       # CFG and Markov generation algorithms
│           ├── noise.go        # Grammar and orthographical error injection engine
│           ├── *_test.go       # Automated Go unit tests
│           └── data/           # Lexicon decks & domain corpora (pt, en, es, fr, la, themes)
│
└── frontend/                   # Next.js Web Interface
    ├── package.json            # Dependencies (Next.js, React, Radix UI, Lucide)
    ├── tsconfig.json           # TypeScript compiler configuration
    ├── tailwind.config.js      # Tailwind CSS configuration + tailwindcss-radix plugin
    ├── postcss.config.js       # PostCSS stylesheet processing
    └── src/
        └── app/
            ├── globals.css     # Global stylesheets and theme tokens (Light/Dark Mode)
            ├── layout.tsx      # Root HTML layout and metadata
            ├── opengraph-image.png # Open Graph & social card preview image
            └── page.tsx        # Responsive Web SPA interface
```

---

## 🚀 Running the Project Locally

### Option 1: Fast Local Development (Recommended)

To spin up both the Go API and Frontend (Next.js dev server with live hot reloading; API changes require restarting the server) natively in **~1 second**:

```bash
make run-local
```

> **Note**: Requires Go 1.22+, Node.js, and Python 3 (used by `scripts/find_ports.py` to allocate free local ports).

Access the running services:
- **Frontend Web UI**: `http://localhost:3000`
- **Swagger Interactive API Docs**: `http://localhost:8000/api/docs`

To stop both services, press `Ctrl+C`.

---

### Option 2: Running via Docker & Colima (Containerized)

To test the application stack inside Docker containers (matching the production VM environment):

```bash
make run-docker
```

* To force rebuild the Docker images: `make build-run`
* To stop containers: `make stop`

---

### Option 3: Manual Step-by-Step Setup

#### Step 1: Verify Go Toolchain
```bash
make setup-dev
```

#### Step 2: Start Services Separately
- **Backend API**:
  ```bash
  cd api && go run ./cmd/server
  ```
- **Frontend UI**:
  ```bash
  cd frontend && npm run dev
  ```

---

## 🧪 Running Automated Tests

To execute the automated backend test suite (covering the CFG generator, Markov chains, stemmers, noise injectors, and HTTP API contracts):

```bash
make test
```

---

## ☁️ Cloud Deployment (Vercel)

The project is configured for deployment to **Vercel** as a full-stack monorepo via [`vercel.json`](vercel.json):

* Automatically routes `/api/*` traffic to the **Go** backend service (`api/cmd/server/main.go`).
* Serves the **Next.js** application from the `frontend/` directory with static asset and SSR optimization.

---

## ⚡ Raycast Extension (`raycast/`)

Prolixo includes a native **Raycast** extension in [`raycast/`](raycast) that connects to the online Prolixo API (`https://prolixo.vercel.app` by default, configurable in Extension Preferences):

```bash
cd raycast
npm install
npm run dev
```

- **Generate Paragraphs** (`no-view`): Type the number of paragraphs inline (e.g. `3`) and press `Enter` to copy directly to clipboard.
- **Generate Sentences** (`no-view`): Type the number of sentences inline and press `Enter` to copy directly to clipboard.
- **Generate Words** (`no-view`): Type the number of words inline and press `Enter` to copy directly to clipboard.
- **Generate Placeholder Text** (`view`): Interactive form to customize language, theme, and precision with preview.
- **Extension Preferences** (`Cmd+,`): Set default Language, Theme, Grammar/Orthography precision, Quick Action (`Copy` or `Paste`), and API URL (`https://prolixo.vercel.app`).
- **Run Unit Tests**: `cd raycast && npm test`




