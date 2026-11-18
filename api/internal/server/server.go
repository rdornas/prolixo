package server

import (
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"strconv"

	"prolixo-api/internal/generator"
	"prolixo-api/internal/limiter"
	"prolixo-api/internal/models"
)

type languageItem struct {
	Code string `json:"code"`
	Name string `json:"name"`
}

type themeItem struct {
	Code        string `json:"code"`
	Name        string `json:"name"`
	Description string `json:"description"`
}

var supportedLanguages = []languageItem{
	{Code: "en", Name: "English"},
	{Code: "fr", Name: "French"},
	{Code: "la", Name: "Latin"},
	{Code: "pt", Name: "Portuguese"},
	{Code: "es", Name: "Spanish"},
}

var supportedThemes = []themeItem{
	{Code: "business", Name: "Business", Description: "Strategy, finance, governance, and management"},
	{Code: "ecology", Name: "Ecology", Description: "Environment, sustainability, and biomes"},
	{Code: "law", Name: "Law", Description: "Jurisprudence, norms, and legal procedures"},
	{Code: "medicine", Name: "Medicine", Description: "Clinical diagnostics, healthcare, and pharmacology"},
	{Code: "mining", Name: "Mining", Description: "Geology, mineral processing, and extraction"},
	{Code: "politics", Name: "Politics", Description: "Governance, legislation, and public policy"},
	{Code: "technology", Name: "Technology", Description: "Software engineering, AI, and cloud computing"},
}

// NewHandler constructs the HTTP router with CORS and rate limiting.
func NewHandler(lim *limiter.Limiter) http.Handler {
	mux := http.NewServeMux()

	mux.HandleFunc("GET /", handleRoot)
	mux.HandleFunc("GET /docs", handleDocsRedirect)
	mux.HandleFunc("GET /api/docs", handleSwaggerUI)
	mux.HandleFunc("GET /api/openapi.json", handleOpenAPI)
	mux.HandleFunc("GET /api/languages", handleLanguages)
	mux.HandleFunc("GET /api/themes", handleThemes)
	mux.HandleFunc("POST /api/generate", handleGenerate(lim))

	return withCORS(mux)
}

func withCORS(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Access-Control-Allow-Origin", "*")
		w.Header().Set("Access-Control-Allow-Credentials", "true")
		w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
		w.Header().Set("Access-Control-Allow-Headers", "*")

		if r.Method == http.MethodOptions {
			w.WriteHeader(http.StatusNoContent)
			return
		}
		next.ServeHTTP(w, r)
	})
}

func writeJSON(w http.ResponseWriter, status int, payload any) {
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	w.WriteHeader(status)
	_ = json.NewEncoder(w).Encode(payload)
}

func handleRoot(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		writeJSON(w, http.StatusNotFound, map[string]string{"detail": "Not Found"})
		return
	}
	writeJSON(w, http.StatusOK, map[string]string{
		"name":   "Prolixo API",
		"status": "online",
	})
}

func handleDocsRedirect(w http.ResponseWriter, r *http.Request) {
	http.Redirect(w, r, "/api/docs", http.StatusTemporaryRedirect)
}

func handleSwaggerUI(w http.ResponseWriter, _ *http.Request) {
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	w.WriteHeader(http.StatusOK)
	_, _ = w.Write([]byte(swaggerHTML))
}

func handleOpenAPI(w http.ResponseWriter, _ *http.Request) {
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	w.WriteHeader(http.StatusOK)
	_, _ = w.Write([]byte(openAPISpec))
}

func handleLanguages(w http.ResponseWriter, _ *http.Request) {
	writeJSON(w, http.StatusOK, map[string]any{"languages": supportedLanguages})
}

func handleThemes(w http.ResponseWriter, _ *http.Request) {
	writeJSON(w, http.StatusOK, map[string]any{"themes": supportedThemes})
}

func handleGenerate(lim *limiter.Limiter) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if allowed, retryAfter := lim.CheckRateLimit(r); !allowed {
			w.Header().Set("Retry-After", strconv.Itoa(retryAfter))
			writeJSON(w, http.StatusTooManyRequests, map[string]any{
				"error":       "too_many_requests",
				"message":     fmt.Sprintf("Rate limit exceeded. Please try again in %d seconds.", retryAfter),
				"retry_after": retryAfter,
			})
			return
		}

		req, err := models.DecodeGenerateRequest(r.Body)
		if err != nil {
			writeJSON(w, http.StatusUnprocessableEntity, map[string]string{"detail": err.Error()})
			return
		}

		results, err := generator.GenerateContent(
			req.Lang,
			req.Type,
			req.Theme,
			req.Count,
			req.GrammarCorrect,
			req.OrthographyCorrect,
		)
		if err != nil {
			var invalidErr generator.ErrInvalidInput
			if errors.As(err, &invalidErr) {
				writeJSON(w, http.StatusBadRequest, map[string]string{"detail": invalidErr.Error()})
				return
			}
			writeJSON(w, http.StatusInternalServerError, map[string]string{
				"detail": fmt.Sprintf("Internal generation error: %v", err),
			})
			return
		}

		writeJSON(w, http.StatusOK, models.GenerateResponse{
			Lang:               req.Lang,
			Type:               req.Type,
			Theme:              req.Theme,
			Count:              req.Count,
			GrammarCorrect:     req.GrammarCorrect,
			OrthographyCorrect: req.OrthographyCorrect,
			Results:            results,
		})
	}
}
