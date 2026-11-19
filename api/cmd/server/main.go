package main

import (
	"log"
	"net/http"
	"os"
	"time"

	"prolixo-api/internal/limiter"
	"prolixo-api/internal/server"
)

func main() {
	port := os.Getenv("API_PORT")
	if port == "" {
		port = os.Getenv("PORT")
	}
	if port == "" {
		port = "8000"
	}

	lim := limiter.NewFromEnv()
	srv := &http.Server{
		Addr:              ":" + port,
		Handler:           server.NewHandler(lim),
		ReadHeaderTimeout: 10 * time.Second,
		ReadTimeout:       15 * time.Second,
	}

	log.Printf("Prolixo Go API listening on :%s", port)
	if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
		log.Fatalf("server failed: %v", err)
	}
}
