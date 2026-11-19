package server

import (
	"bytes"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"time"

	"prolixo-api/internal/limiter"
)

func newTestHandler() (http.Handler, *limiter.Limiter) {
	lim := limiter.New("test_secret", 30, 30, 60*time.Second)
	return NewHandler(lim), lim
}

func TestRootEndpoint(t *testing.T) {
	h, _ := newTestHandler()
	req := httptest.NewRequest(http.MethodGet, "/", nil)
	rec := httptest.NewRecorder()
	h.ServeHTTP(rec, req)

	if rec.Code != http.StatusOK {
		t.Fatalf("expected 200, got %d", rec.Code)
	}
	var body map[string]string
	if err := json.NewDecoder(rec.Body).Decode(&body); err != nil {
		t.Fatal(err)
	}
	if body["status"] != "online" || body["name"] != "Prolixo API" {
		t.Fatalf("unexpected root response: %v", body)
	}
}

func TestDocsAndOpenAPIEndpoints(t *testing.T) {
	h, _ := newTestHandler()

	rec := httptest.NewRecorder()
	h.ServeHTTP(rec, httptest.NewRequest(http.MethodGet, "/api/docs", nil))
	if rec.Code != http.StatusOK || !strings.Contains(strings.ToLower(rec.Body.String()), "swagger") {
		t.Fatalf("expected swagger UI on /api/docs, got %d", rec.Code)
	}

	rec = httptest.NewRecorder()
	h.ServeHTTP(rec, httptest.NewRequest(http.MethodGet, "/docs", nil))
	if rec.Code != http.StatusTemporaryRedirect {
		t.Fatalf("expected 307 redirect on /docs, got %d", rec.Code)
	}

	rec = httptest.NewRecorder()
	h.ServeHTTP(rec, httptest.NewRequest(http.MethodGet, "/api/openapi.json", nil))
	if rec.Code != http.StatusOK || !strings.Contains(rec.Body.String(), `"Prolixo API"`) {
		t.Fatalf("expected OpenAPI JSON, got %d", rec.Code)
	}
}

func TestLanguagesEndpoint(t *testing.T) {
	h, _ := newTestHandler()
	rec := httptest.NewRecorder()
	h.ServeHTTP(rec, httptest.NewRequest(http.MethodGet, "/api/languages", nil))
	if rec.Code != http.StatusOK {
		t.Fatalf("expected 200, got %d", rec.Code)
	}
	var body struct {
		Languages []languageItem `json:"languages"`
	}
	if err := json.NewDecoder(rec.Body).Decode(&body); err != nil {
		t.Fatal(err)
	}
	if len(body.Languages) != 5 {
		t.Fatalf("expected 5 languages, got %d", len(body.Languages))
	}
}

func TestThemesEndpoint(t *testing.T) {
	h, _ := newTestHandler()
	rec := httptest.NewRecorder()
	h.ServeHTTP(rec, httptest.NewRequest(http.MethodGet, "/api/themes", nil))
	if rec.Code != http.StatusOK {
		t.Fatalf("expected 200, got %d", rec.Code)
	}
	var body struct {
		Themes []themeItem `json:"themes"`
	}
	if err := json.NewDecoder(rec.Body).Decode(&body); err != nil {
		t.Fatal(err)
	}
	if len(body.Themes) != 7 {
		t.Fatalf("expected 7 themes, got %d", len(body.Themes))
	}
}

func TestGenerateEndpointSuccessAndErrors(t *testing.T) {
	h, _ := newTestHandler()

	// Success
	payload := `{"lang":"en","type":"sentences","theme":"technology","count":2,"grammar_correct":true,"orthography_correct":true}`
	rec := httptest.NewRecorder()
	h.ServeHTTP(rec, httptest.NewRequest(http.MethodPost, "/api/generate", strings.NewReader(payload)))
	if rec.Code != http.StatusOK {
		t.Fatalf("expected 200, got %d: %s", rec.Code, rec.Body.String())
	}
	var resp struct {
		Lang    string   `json:"lang"`
		Type    string   `json:"type"`
		Results []string `json:"results"`
	}
	if err := json.NewDecoder(rec.Body).Decode(&resp); err != nil {
		t.Fatal(err)
	}
	if resp.Lang != "en" || resp.Type != "sentences" || len(resp.Results) != 2 {
		t.Fatalf("unexpected generate response: %+v", resp)
	}

	// 422 out of bounds
	rec = httptest.NewRecorder()
	h.ServeHTTP(rec, httptest.NewRequest(http.MethodPost, "/api/generate", strings.NewReader(`{"lang":"en","type":"words","count":0}`)))
	if rec.Code != http.StatusUnprocessableEntity {
		t.Fatalf("expected 422, got %d", rec.Code)
	}

	// 400 unsupported language
	rec = httptest.NewRecorder()
	h.ServeHTTP(rec, httptest.NewRequest(http.MethodPost, "/api/generate", strings.NewReader(`{"lang":"unsupported","type":"words","count":5}`)))
	if rec.Code != http.StatusBadRequest {
		t.Fatalf("expected 400, got %d", rec.Code)
	}
}

func TestGenerateEndpointRateLimiting(t *testing.T) {
	h, lim := newTestHandler()
	lim.Reset()

	payload := []byte(`{"lang":"en","type":"words","theme":"technology","count":5}`)
	for i := 0; i < 30; i++ {
		req := httptest.NewRequest(http.MethodPost, "/api/generate", bytes.NewReader(payload))
		req.RemoteAddr = "203.0.113.50:1234"
		rec := httptest.NewRecorder()
		h.ServeHTTP(rec, req)
		if rec.Code != http.StatusOK {
			t.Fatalf("request %d failed with %d", i+1, rec.Code)
		}
	}

	req := httptest.NewRequest(http.MethodPost, "/api/generate", bytes.NewReader(payload))
	req.RemoteAddr = "203.0.113.50:1234"
	rec := httptest.NewRecorder()
	h.ServeHTTP(rec, req)

	if rec.Code != http.StatusTooManyRequests {
		t.Fatalf("expected 429 on 31st request, got %d", rec.Code)
	}
	if rec.Header().Get("Retry-After") == "" {
		t.Fatalf("expected Retry-After header on 429")
	}
	var errBody map[string]any
	if err := json.NewDecoder(rec.Body).Decode(&errBody); err != nil {
		t.Fatal(err)
	}
	if errBody["error"] != "too_many_requests" {
		t.Fatalf("expected error='too_many_requests', got %v", errBody["error"])
	}
}

func TestCORSHeaders(t *testing.T) {
	t.Setenv("CORS_ALLOWED_ORIGINS", "https://prolixo.vercel.app")
	h, _ := newTestHandler()

	// Allowed credentialed origin
	req := httptest.NewRequest(http.MethodGet, "/api/languages", nil)
	req.Header.Set("Origin", "https://prolixo.vercel.app")
	rec := httptest.NewRecorder()
	h.ServeHTTP(rec, req)
	if rec.Header().Get("Access-Control-Allow-Origin") != "https://prolixo.vercel.app" {
		t.Fatalf("expected echoed allowed origin, got %q", rec.Header().Get("Access-Control-Allow-Origin"))
	}
	if rec.Header().Get("Access-Control-Allow-Credentials") != "true" {
		t.Fatalf("expected Allow-Credentials=true for allowed origin")
	}
	if rec.Header().Get("Vary") != "Origin" {
		t.Fatalf("expected Vary=Origin, got %q", rec.Header().Get("Vary"))
	}

	// Disallowed origin falls back to non-credentialed wildcard
	req2 := httptest.NewRequest(http.MethodGet, "/api/languages", nil)
	req2.Header.Set("Origin", "https://evil.example")
	rec2 := httptest.NewRecorder()
	h.ServeHTTP(rec2, req2)
	if rec2.Header().Get("Access-Control-Allow-Origin") != "*" {
		t.Fatalf("expected '*' for non-credentialed origin, got %q", rec2.Header().Get("Access-Control-Allow-Origin"))
	}
	if rec2.Header().Get("Access-Control-Allow-Credentials") != "" {
		t.Fatalf("expected no Allow-Credentials for non-allowed origin")
	}
	if rec2.Header().Get("Access-Control-Allow-Headers") == "*" {
		t.Fatalf("expected explicit Allow-Headers, not '*'")
	}
}
