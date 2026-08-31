# Prolixo - Natural Language Placeholder Text Generator

**Prolixo** is a professional, multilingual web application for generating placeholder text across three distinct output modes: **Words**, **Sentences**, and **Paragraphs**. The project is designed to be minimalist, robust, and elegant, built with **FastAPI** on the backend API and **Next.js** on the frontend with **Radix UI** primitives styled via the **`tailwindcss-radix`** plugin.

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
├── api/                        # FastAPI Backend API
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py             # API routes & CORS configuration
│   │   ├── models.py           # Pydantic request/response schemas
│   │   └── generator/          # Statistical natural language generation engine
│   │       ├── __init__.py
│   │       ├── engine.py       # CFG and Markov generation algorithms
│   │       ├── noise.py        # Grammar and orthographical error injection engine
│   │       └── dicts/          # Lexicon decks & domain corpora
│   │           ├── __init__.py
│   │           ├── pt.py       # Portuguese CFG grammatical decks (gender/number tagged nouns, verbs, adj)
│   │           ├── en.py       # English CFG grammatical decks (singular/plural tagged nouns, verbs, adj)
│   │           ├── es.py       # Spanish CFG grammatical decks (gender/number tagged nouns, verbs, adj)
│   │           ├── fr.py       # French CFG grammatical decks (gender/number tagged nouns, verbs, adj)
│   │           ├── la.py       # Classical Latin corpus sentences (Cicero) for Markov Chain generation
│   │           └── themes.py   # Domain vocabulary overrides (Business, Ecology, Law, Medicine, Mining, Politics, Tech)
│   ├── requirements.txt        # Python dependencies
│   └── run.py                  # API development server entry point
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
            └── page.tsx        # Responsive Web SPA interface
```

---

## 🚀 Running the Project Locally

### Option 1: Fast Local Development (Recommended)

To spin up both the API (via Python virtual environment) and Frontend (Next.js dev server) natively in **~1 second** with live hot reloading:

```bash
make run-local
```

> **Note**: If `api/.venv` does not exist yet, `make run-local` will automatically create it and install all dependencies.

Access the running services:
- **Frontend Web UI**: `http://localhost:3000`
- **Swagger Interactive API Docs**: `http://localhost:8000/docs`

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

#### Step 1: Setup API Virtual Environment
```bash
make setup-dev
```

#### Step 2: Start Services Separately
- **Backend API**:
  ```bash
  cd api && .venv/bin/python run.py
  ```
- **Frontend UI**:
  ```bash
  cd frontend && npm run dev
  ```


