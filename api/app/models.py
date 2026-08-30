from pydantic import BaseModel, Field

class GenerateRequest(BaseModel):
    lang: str
    type: str
    theme: str = "business"
    count: int = Field(..., ge=1, le=100)
    grammar_correct: bool = True
    orthography_correct: bool = True

class GenerateResponse(BaseModel):
    lang: str
    type: str
    theme: str
    count: int
    grammar_correct: bool = True
    orthography_correct: bool = True
    results: list[str]
