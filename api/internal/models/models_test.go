package models

import (
	"strings"
	"testing"
)

func TestGenerateRequestValidDefaults(t *testing.T) {
	body := `{"lang":"en","type":"words","count":5}`
	req, err := DecodeGenerateRequest(strings.NewReader(body))
	if err != nil {
		t.Fatalf("expected valid request, got error: %v", err)
	}
	if req.Theme != "business" {
		t.Fatalf("expected default theme 'business', got %q", req.Theme)
	}
	if !req.GrammarCorrect || !req.OrthographyCorrect {
		t.Fatalf("expected grammar_correct and orthography_correct to default to true")
	}
}

func TestGenerateRequestExplicitFalse(t *testing.T) {
	body := `{"lang":"pt","type":"sentences","theme":"mining","count":3,"grammar_correct":false,"orthography_correct":false}`
	req, err := DecodeGenerateRequest(strings.NewReader(body))
	if err != nil {
		t.Fatalf("expected valid request, got error: %v", err)
	}
	if req.GrammarCorrect || req.OrthographyCorrect {
		t.Fatalf("expected explicit false values to be preserved")
	}
	if req.Theme != "mining" {
		t.Fatalf("expected theme 'mining', got %q", req.Theme)
	}
}

func TestGenerateRequestCountValidation(t *testing.T) {
	for _, count := range []int{0, -5, 101} {
		req := GenerateRequest{Lang: "en", Type: "words", Theme: "business", Count: count}
		if err := req.Validate(); err == nil {
			t.Fatalf("expected validation error for count=%d", count)
		}
	}

	for _, count := range []int{1, 50, 100} {
		req := GenerateRequest{Lang: "en", Type: "words", Theme: "business", Count: count}
		if err := req.Validate(); err != nil {
			t.Fatalf("expected count=%d to be valid, got error: %v", count, err)
		}
	}
}

func TestGenerateRequestMissingRequiredFields(t *testing.T) {
	for _, body := range []string{
		`{"type":"words","count":5}`,
		`{"lang":"en","count":5}`,
		`{"lang":"en","type":"words"}`,
	} {
		if _, err := DecodeGenerateRequest(strings.NewReader(body)); err == nil {
			t.Fatalf("expected validation error for %s", body)
		}
	}
}
