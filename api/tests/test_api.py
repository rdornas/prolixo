from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data.get("status") == "online"
    assert data.get("name") == "Prolixo API"

def test_docs_endpoint():
    response = client.get("/api/docs")
    assert response.status_code == 200
    assert "swagger" in response.text.lower() or "html" in response.headers.get("content-type", "")

def test_docs_redirect():
    response = client.get("/docs", follow_redirects=False)
    assert response.status_code in (200, 307, 308)

def test_languages_endpoint():
    response = client.get("/api/languages")
    assert response.status_code == 200
    data = response.json()
    assert "languages" in data
    codes = [l["code"] for l in data["languages"]]
    assert set(codes) == {"en", "fr", "la", "pt", "es"}

def test_themes_endpoint():
    response = client.get("/api/themes")
    assert response.status_code == 200
    data = response.json()
    assert "themes" in data
    codes = [t["code"] for t in data["themes"]]
    assert "business" in codes
    assert "technology" in codes
    assert len(codes) == 7

def test_generate_endpoint_success():
    payload = {
        "lang": "en",
        "type": "sentences",
        "theme": "technology",
        "count": 2,
        "grammar_correct": True,
        "orthography_correct": True
    }
    response = client.post("/api/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["lang"] == "en"
    assert data["type"] == "sentences"
    assert len(data["results"]) == 2

def test_generate_endpoint_invalid_payload():
    # count out of bounds
    payload = {
        "lang": "en",
        "type": "words",
        "count": 0
    }
    response = client.post("/api/generate", json=payload)
    assert response.status_code == 422

def test_generate_endpoint_invalid_language():
    payload = {
        "lang": "unsupported",
        "type": "words",
        "count": 5
    }
    response = client.post("/api/generate", json=payload)
    assert response.status_code == 400
