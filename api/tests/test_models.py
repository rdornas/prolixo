import pytest
from pydantic import ValidationError
from app.models import GenerateRequest, GenerateResponse

def test_generate_request_valid():
    req = GenerateRequest(
        lang="pt",
        type="paragraphs",
        theme="technology",
        count=3,
        grammar_correct=True,
        orthography_correct=True
    )
    assert req.lang == "pt"
    assert req.type == "paragraphs"
    assert req.count == 3
    assert req.theme == "technology"

def test_generate_request_count_validation():
    with pytest.raises(ValidationError):
        GenerateRequest(lang="en", type="words", count=0)
    
    with pytest.raises(ValidationError):
        GenerateRequest(lang="en", type="words", count=101)

def test_generate_response_valid():
    res = GenerateResponse(
        lang="pt",
        type="words",
        theme="business",
        count=5,
        grammar_correct=True,
        orthography_correct=True,
        results=["um dois tres quatro cinco"]
    )
    assert res.count == 5
    assert len(res.results) == 1
