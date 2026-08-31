from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse
from app.models import GenerateRequest, GenerateResponse
from app.generator.engine import generate_content
from app.limiter import limiter

app = FastAPI(
    title="Prolixo API",
    version="1.0.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    redoc_url=None
)

@app.get("/docs", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/api/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"name": "Prolixo API", "status": "online"}

@app.get("/api/languages")
async def get_languages():
    return {
        "languages": [
            {"code": "en", "name": "English"},
            {"code": "fr", "name": "French"},
            {"code": "la", "name": "Latin"},
            {"code": "pt", "name": "Portuguese"},
            {"code": "es", "name": "Spanish"}
        ]
    }

@app.get("/api/themes")
async def get_themes():
    return {
        "themes": [
            {"code": "business", "name": "Business", "description": "Strategy, finance, governance, and management"},
            {"code": "ecology", "name": "Ecology", "description": "Environment, sustainability, and biomes"},
            {"code": "law", "name": "Law", "description": "Jurisprudence, norms, and legal procedures"},
            {"code": "medicine", "name": "Medicine", "description": "Clinical diagnostics, healthcare, and pharmacology"},
            {"code": "mining", "name": "Mining", "description": "Geology, mineral processing, and extraction"},
            {"code": "politics", "name": "Politics", "description": "Governance, legislation, and public policy"},
            {"code": "technology", "name": "Technology", "description": "Software engineering, AI, and cloud computing"}
        ]
    }

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 429 and isinstance(exc.detail, dict):
        return JSONResponse(
            status_code=429,
            content=exc.detail,
            headers=exc.headers or {},
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
        headers=exc.headers or {},
    )


@app.post(
    "/api/generate",
    response_model=GenerateResponse,
    dependencies=[Depends(limiter.check_rate_limit)],
)
async def generate_text(request: GenerateRequest):
    try:
        results = generate_content(
            lang=request.lang,
            output_type=request.type,
            theme=request.theme,
            count=request.count,
            grammar_correct=request.grammar_correct,
            orthography_correct=request.orthography_correct
        )
        return GenerateResponse(
            lang=request.lang,
            type=request.type,
            theme=request.theme,
            count=request.count,
            grammar_correct=request.grammar_correct,
            orthography_correct=request.orthography_correct,
            results=results
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal generation error: {str(e)}")
