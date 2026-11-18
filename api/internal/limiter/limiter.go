package limiter

import (
	"fmt"
	"math"
	"net"
	"net/http"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"
)

// DefaultInternalSecret is used when INTERNAL_API_SECRET is not set.
const DefaultInternalSecret = "prolixo_internal_client_secret"

// Limiter implements a zero-dependency in-memory sliding-window rate limiter.
type Limiter struct {
	mu             sync.Mutex
	internalSecret string
	frontendLimit  int
	directLimit    int
	window         time.Duration
	records        map[string][]time.Time
	nowFunc        func() time.Time
}

// NewFromEnv initializes a Limiter from environment variables with defaults.
func NewFromEnv() *Limiter {
	secret := os.Getenv("INTERNAL_API_SECRET")
	if secret == "" {
		secret = DefaultInternalSecret
	}
	return New(
		secret,
		getEnvInt("RATE_LIMIT_FRONTEND", 30),
		getEnvInt("RATE_LIMIT_DIRECT", 30),
		time.Duration(getEnvInt("RATE_LIMIT_WINDOW", 60))*time.Second,
	)
}

// New creates a new Limiter with explicit settings.
func New(internalSecret string, frontendLimit, directLimit int, window time.Duration) *Limiter {
	return &Limiter{
		internalSecret: internalSecret,
		frontendLimit:  frontendLimit,
		directLimit:    directLimit,
		window:         window,
		records:        make(map[string][]time.Time),
		nowFunc:        time.Now,
	}
}

func getEnvInt(key string, fallback int) int {
	raw := os.Getenv(key)
	if raw == "" {
		return fallback
	}
	val, err := strconv.Atoi(raw)
	if err != nil || val <= 0 {
		return fallback
	}
	return val
}

func extractRemoteIP(r *http.Request) string {
	if forwarded := r.Header.Get("X-Forwarded-For"); forwarded != "" {
		first := strings.TrimSpace(strings.Split(forwarded, ",")[0])
		if first != "" {
			return first
		}
	}
	if r.RemoteAddr != "" {
		host, _, err := net.SplitHostPort(r.RemoteAddr)
		if err == nil && host != "" {
			return host
		}
		return r.RemoteAddr
	}
	return "127.0.0.1"
}

// GetClientKey determines the rate-limit key and whether the request is from a trusted frontend.
func (l *Limiter) GetClientKey(r *http.Request) (string, bool) {
	secret := r.Header.Get("X-Internal-Secret")
	isTrusted := secret != "" && secret == l.internalSecret

	if isTrusted {
		userIP := strings.TrimSpace(r.Header.Get("X-Forwarded-User-IP"))
		if userIP == "" {
			userIP = extractRemoteIP(r)
		}
		return fmt.Sprintf("%s:frontend", userIP), true
	}

	return fmt.Sprintf("%s:direct", extractRemoteIP(r)), false
}

// CheckRateLimit checks if the request is within the sliding-window quota.
// When blocked, it returns allowed=false and retryAfter in seconds (>= 1).
func (l *Limiter) CheckRateLimit(r *http.Request) (bool, int) {
	key, isTrusted := l.GetClientKey(r)
	maxAllowed := l.directLimit
	if isTrusted {
		maxAllowed = l.frontendLimit
	}

	l.mu.Lock()
	defer l.mu.Unlock()

	now := l.nowFunc()
	cutoff := now.Add(-l.window)

	existing := l.records[key]
	filtered := existing[:0]
	for _, ts := range existing {
		if ts.After(cutoff) {
			filtered = append(filtered, ts)
		}
	}

	if len(filtered) >= maxAllowed {
		earliest := filtered[0]
		remaining := earliest.Add(l.window).Sub(now).Seconds()
		retryAfter := int(math.Ceil(remaining))
		if retryAfter < 1 {
			retryAfter = 1
		}
		l.records[key] = filtered
		return false, retryAfter
	}

	filtered = append(filtered, now)
	l.records[key] = filtered
	return true, 0
}

// Reset clears all stored rate-limit records.
func (l *Limiter) Reset() {
	l.mu.Lock()
	defer l.mu.Unlock()
	l.records = make(map[string][]time.Time)
}

// InternalSecret returns the configured internal secret.
func (l *Limiter) InternalSecret() string {
	return l.internalSecret
}
