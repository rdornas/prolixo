# Prolixo — Natural Language Placeholder Text Generator

**Prolixo** is a professional, multilingual web application for generating placeholder text across three distinct output modes: **Words**, **Sentences**, and **Paragraphs**. The project is designed to be minimalist, robust, and elegant, built with **FastAPI** on the backend API and **Next.js** on the frontend with **Radix UI** primitives styled via the **`tailwindcss-radix`** plugin.

The text generation engine is **100% algorithmic, local, and deterministic-statistical**, executing entirely offline in the API without requiring external third-party AI APIs or internet connectivity.

---

## 📂 Project Structure

The project directory layout is organized as follows:

```text
prolixo/
├── estrategia_prolixo.md       # Strategic development plan & architecture
├── Makefile                    # Local workflow automation & container lifecycle
├── README.md                   # Project documentation & reference guide
│
├── api/                        # FastAPI Backend & OpenAPI Documentation
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py             # API routes, OpenAPI Swagger metadata & CORS configuration
│   │   ├── models.py           # Pydantic schemas & input validation
│   │   └── generator/          # Statistical natural language generation engine
│   │       ├── __init__.py
│   │       ├── engine.py       # CFG and Markov generation algorithms
│   │       └── dicts/          # Static lexicon and theme corpora
│   │           ├── __init__.py
│   │           ├── themes.py   # Specialized domain themes (Ecology, Law, Medicine, Mining, Politics, Technology)
│   │           ├── pt.py       # Portuguese corporate/formal lexicon
│   │           ├── en.py       # English corporate/formal lexicon
│   │           ├── es.py       # Spanish corporate/formal lexicon
│   │           └── la.py       # Classical Cicero Latin sentences
│   ├── requirements.txt        # Python dependencies
│   └── run.py                  # API development startup script
│
└── frontend/                   # Next.js Web Interface
    ├── package.json            # NPM dependencies (Next.js, React, Radix UI, Lucide)
    ├── tsconfig.json           # TypeScript compiler configuration
    ├── tailwind.config.js      # Tailwind CSS configuration + tailwindcss-radix plugin
    ├── postcss.config.js       # PostCSS stylesheet processing
    ├── next-env.d.ts           # Next.js type definitions
    └── src/
        └── app/
            ├── globals.css     # Global stylesheets and theme tokens (Light/Dark Mode)
            ├── layout.tsx      # Root HTML layout and metadata
            └── page.tsx        # SPA interface (generator controls and text viewer)
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
- **ReDoc API Docs**: `http://localhost:8000/redoc`

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


---

## 💡 Fallback Engine & Offline Resilience
The Next.js frontend contains an **integrated client-side fallback engine**. If the frontend is run while the FastAPI backend is temporarily unavailable, it automatically switches to a local in-browser simulation engine with equivalent linguistic output rules. This ensures continuous usability during offline workflows and UI prototyping.
