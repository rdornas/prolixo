package limiter

import (
	"net/http"
	"net/http/httptest"
	"testing"
	"time"
)

func TestDefaultLimitsAreThirty(t *testing.T) {
	l := NewFromEnv()
	if l.frontendLimit != 30 || l.directLimit != 30 {
		t.Fatalf("expected default limits 30/30, got %d/%d", l.frontendLimit, l.directLimit)
	}
	if l.window != 60*time.Second {
		t.Fatalf("expected 60s window, got %v", l.window)
	}
}

func TestDirectAPIRateLimitExceeded(t *testing.T) {
	l := New(DefaultInternalSecret, 30, 3, 60*time.Second)
	for i := 0; i < 3; i++ {
		req := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
		req.Header.Set("X-Forwarded-For", "198.51.100.10")
		allowed, _ := l.CheckRateLimit(req)
		if !allowed {
			t.Fatalf("request %d should be allowed", i+1)
		}
	}

	req := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
	req.Header.Set("X-Forwarded-For", "198.51.100.10")
	allowed, retryAfter := l.CheckRateLimit(req)
	if allowed {
		t.Fatalf("4th request should be blocked")
	}
	if retryAfter < 1 {
		t.Fatalf("expected retryAfter >= 1, got %d", retryAfter)
	}
}

func TestFrontendAndDirectCountersAreIsolated(t *testing.T) {
	l := New(DefaultInternalSecret, 2, 2, 60*time.Second)

	for i := 0; i < 2; i++ {
		req := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
		req.Header.Set("X-Forwarded-For", "203.0.113.1")
		if ok, _ := l.CheckRateLimit(req); !ok {
			t.Fatalf("direct request %d should be allowed", i+1)
		}
	}

	// Direct is now exhausted, but trusted frontend for same IP must still have quota
	req := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
	req.Header.Set("X-Internal-Secret", DefaultInternalSecret)
	req.Header.Set("X-Forwarded-User-IP", "203.0.113.1")
	if ok, _ := l.CheckRateLimit(req); !ok {
		t.Fatalf("frontend request for same IP should be isolated and allowed")
	}
}

func TestRateLimitResetsAfterWindow(t *testing.T) {
	now := time.Unix(1700000000, 0)
	l := New(DefaultInternalSecret, 1, 1, 10*time.Second)
	l.nowFunc = func() time.Time { return now }

	req := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
	req.RemoteAddr = "192.0.2.1:12345"

	if ok, _ := l.CheckRateLimit(req); !ok {
		t.Fatalf("first request should be allowed")
	}
	if ok, _ := l.CheckRateLimit(req); ok {
		t.Fatalf("second request within window should be blocked")
	}

	now = now.Add(11 * time.Second)
	if ok, _ := l.CheckRateLimit(req); !ok {
		t.Fatalf("request after window expiration should be allowed")
	}
}
