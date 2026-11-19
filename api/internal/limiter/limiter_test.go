package limiter

import (
	"net/http"
	"net/http/httptest"
	"testing"
	"time"
)

const testInternalSecret = "test_internal_secret"

func TestDefaultLimitsAreThirty(t *testing.T) {
	t.Setenv("RATE_LIMIT_DIRECT", "")
	t.Setenv("RATE_LIMIT_FRONTEND", "")
	t.Setenv("RATE_LIMIT_WINDOW", "")
	t.Setenv("INTERNAL_API_SECRET", "")

	l := NewFromEnv()
	if l.frontendLimit != 30 || l.directLimit != 30 {
		t.Fatalf("expected default limits 30/30, got %d/%d", l.frontendLimit, l.directLimit)
	}
	if l.window != 60*time.Second {
		t.Fatalf("expected 60s window, got %v", l.window)
	}

	req := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
	req.Header.Set("X-Internal-Secret", "prolixo_internal_client_secret")
	if _, trusted := l.GetClientKey(req); trusted {
		t.Fatalf("expected unset INTERNAL_API_SECRET to disable trusted classification")
	}
}

func TestUntrustedPeerIgnoresXForwardedFor(t *testing.T) {
	l := New(testInternalSecret, 30, 2, 60*time.Second)

	req1 := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
	req1.RemoteAddr = "198.51.100.10:1111"
	req1.Header.Set("X-Forwarded-For", "203.0.113.1")

	req2 := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
	req2.RemoteAddr = "198.51.100.10:2222"
	req2.Header.Set("X-Forwarded-For", "203.0.113.2")

	key1, _ := l.GetClientKey(req1)
	key2, _ := l.GetClientKey(req2)
	if key1 != "198.51.100.10:direct" || key1 != key2 {
		t.Fatalf("expected untrusted peer to ignore X-Forwarded-For, got %q and %q", key1, key2)
	}
}

func TestTrustedProxyHonorsXForwardedFor(t *testing.T) {
	l := New(testInternalSecret, 30, 3, 60*time.Second)
	l.SetTrustedProxies([]string{"10.0.0.0/8"})

	for i := 0; i < 3; i++ {
		req := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
		req.RemoteAddr = "10.0.0.5:4321"
		req.Header.Set("X-Forwarded-For", "198.51.100.10")
		allowed, _ := l.CheckRateLimit(req)
		if !allowed {
			t.Fatalf("request %d should be allowed", i+1)
		}
	}

	req := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
	req.RemoteAddr = "10.0.0.5:4321"
	req.Header.Set("X-Forwarded-For", "198.51.100.10")
	allowed, retryAfter := l.CheckRateLimit(req)
	if allowed || retryAfter < 1 {
		t.Fatalf("4th request should be blocked with retryAfter >= 1")
	}
}

func TestFrontendAndDirectCountersAreIsolated(t *testing.T) {
	l := New(testInternalSecret, 2, 2, 60*time.Second)

	for i := 0; i < 2; i++ {
		req := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
		req.RemoteAddr = "203.0.113.1:5000"
		if ok, _ := l.CheckRateLimit(req); !ok {
			t.Fatalf("direct request %d should be allowed", i+1)
		}
	}

	req := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
	req.Header.Set("X-Internal-Secret", testInternalSecret)
	req.Header.Set("X-Forwarded-User-IP", "203.0.113.1")
	if ok, _ := l.CheckRateLimit(req); !ok {
		t.Fatalf("frontend request for same IP should be isolated and allowed")
	}
}

func TestRateLimitResetsAndEvictsExpiredRecords(t *testing.T) {
	now := time.Unix(1700000000, 0)
	l := New(testInternalSecret, 1, 1, 10*time.Second)
	l.nowFunc = func() time.Time { return now }

	req := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
	req.RemoteAddr = "192.0.2.1:12345"

	if ok, _ := l.CheckRateLimit(req); !ok {
		t.Fatalf("first request should be allowed")
	}
	if ok, _ := l.CheckRateLimit(req); ok {
		t.Fatalf("second request within window should be blocked")
	}

	// Advance past window; add an active record and trigger bounded eviction
	now = now.Add(11 * time.Second)
	req2 := httptest.NewRequest(http.MethodPost, "/api/generate", nil)
	req2.RemoteAddr = "192.0.2.2:12345"
	if ok, _ := l.CheckRateLimit(req2); !ok {
		t.Fatalf("active request should be allowed")
	}

	l.mu.Lock()
	l.evictExpiredBounded(now.Add(-l.window))
	_, expiredPresent := l.records["192.0.2.1:direct"]
	_, activePresent := l.records["192.0.2.2:direct"]
	l.mu.Unlock()

	if expiredPresent {
		t.Fatalf("expected expired record to be evicted")
	}
	if !activePresent {
		t.Fatalf("expected active record to be preserved")
	}
}
