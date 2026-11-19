package models

import (
	"encoding/json"
	"errors"
	"fmt"
	"io"
)

// GenerateRequest represents the payload for POST /api/generate.
type GenerateRequest struct {
	Lang               string `json:"lang"`
	Type               string `json:"type"`
	Theme              string `json:"theme"`
	Count              int    `json:"count"`
	GrammarCorrect     bool   `json:"grammar_correct"`
	OrthographyCorrect bool   `json:"orthography_correct"`
}

// GenerateResponse represents the response payload for POST /api/generate.
type GenerateResponse struct {
	Lang               string   `json:"lang"`
	Type               string   `json:"type"`
	Theme              string   `json:"theme"`
	Count              int      `json:"count"`
	GrammarCorrect     bool     `json:"grammar_correct"`
	OrthographyCorrect bool     `json:"orthography_correct"`
	Results            []string `json:"results"`
}

// DecodeGenerateRequest decodes JSON with Pydantic-compatible defaults and validates bounds.
func DecodeGenerateRequest(r io.Reader) (GenerateRequest, error) {
	req := GenerateRequest{
		Theme:              "business",
		GrammarCorrect:     true,
		OrthographyCorrect: true,
	}

	dec := json.NewDecoder(r)
	if err := dec.Decode(&req); err != nil {
		return GenerateRequest{}, fmt.Errorf("invalid JSON payload: %w", err)
	}

	if req.Theme == "" {
		req.Theme = "business"
	}

	if err := req.Validate(); err != nil {
		return GenerateRequest{}, err
	}

	return req, nil
}

// Validate checks required fields and numeric bounds matching FastAPI/Pydantic rules.
func (r GenerateRequest) Validate() error {
	if r.Lang == "" {
		return errors.New("field 'lang' is required")
	}
	if r.Type == "" {
		return errors.New("field 'type' is required")
	}
	if r.Count < 1 || r.Count > 100 {
		return errors.New("field 'count' must be between 1 and 100")
	}
	return nil
}
