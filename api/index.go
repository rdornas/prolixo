package handler

import (
	"net/http"

	"prolixo-api/internal/limiter"
	"prolixo-api/internal/server"
)

var defaultHandler = server.NewHandler(limiter.NewFromEnv())

// Handler is the Vercel Go Serverless Function entrypoint.
func Handler(w http.ResponseWriter, r *http.Request) {
	defaultHandler.ServeHTTP(w, r)
}
