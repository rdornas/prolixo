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

const (
	evictCheckInterval = 32
	evictScanBudget    = 64
)

// Limiter implements a zero-dependency in-memory sliding-window rate limiter.
type Limiter struct {
	mu             sync.Mutex
	internalSecret string
	frontendLimit  int
	directLimit    int
	window         time.Duration
	trustedProxies []*net.IPNet
	records        map[string][]time.Time
	opsCount       int
	nowFunc        func() time.Time
}

// NewFromEnv initializes a Limiter from environment variables.
// If INTERNAL_API_SECRET is unset, trusted frontend classification is disabled.
func NewFromEnv() *Limiter {
	l := New(
		os.Getenv("INTERNAL_API_SECRET"),
		getEnvInt("RATE_LIMIT_FRONTEND", 30),
		getEnvInt("RATE_LIMIT_DIRECT", 30),
		time.Duration(getEnvInt("RATE_LIMIT_WINDOW", 60))*time.Second,
	)
	if raw := os.Getenv("TRUSTED_PROXIES"); raw != "" {
		l.SetTrustedProxies(strings.Split(raw, ","))
	}
	return l
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

// SetTrustedProxies configures IPs or CIDRs allowed to supply X-Forwarded-For.
func (l *Limiter) SetTrustedProxies(entries []string) {
	var nets []*net.IPNet
	for _, raw := range entries {
		s := strings.TrimSpace(raw)
		if s == "" {
			continue
		}
		if _, cidr, err := net.ParseCIDR(s); err == nil {
			nets = append(nets, cidr)
			continue
		}
		if ip := net.ParseIP(s); ip != nil {
			bits := 32
			if ip.To4() == nil {
				bits = 128
			}
			nets = append(nets, &net.IPNet{IP: ip, Mask: net.CIDRMask(bits, bits)})
		}
	}
	l.mu.Lock()
	l.trustedProxies = nets
	l.mu.Unlock()
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

func peerHost(r *http.Request) string {
	if r.RemoteAddr == "" {
		return ""
	}
	host, _, err := net.SplitHostPort(r.RemoteAddr)
	if err == nil && host != "" {
		return host
	}
	return r.RemoteAddr
}

func (l *Limiter) isTrustedPeer(host string) bool {
	if host == "" {
		return false
	}
	ip := net.ParseIP(host)
	if ip == nil {
		return false
	}
	l.mu.Lock()
	proxies := l.trustedProxies
	l.mu.Unlock()
	for _, cidr := range proxies {
		if cidr.Contains(ip) {
			return true
		}
	}
	return false
}

func (l *Limiter) extractRemoteIP(r *http.Request) string {
	peer := peerHost(r)
	if l.isTrustedPeer(peer) {
		if forwarded := r.Header.Get("X-Forwarded-For"); forwarded != "" {
			first := strings.TrimSpace(strings.Split(forwarded, ",")[0])
			if first != "" {
				return first
			}
		}
	}
	if peer != "" {
		return peer
	}
	return "127.0.0.1"
}

// GetClientKey determines the rate-limit key and whether the request is from a trusted frontend.
func (l *Limiter) GetClientKey(r *http.Request) (string, bool) {
	secret := r.Header.Get("X-Internal-Secret")
	isTrusted := l.internalSecret != "" && secret == l.internalSecret

	if isTrusted {
		userIP := strings.TrimSpace(r.Header.Get("X-Forwarded-User-IP"))
		if userIP == "" {
			userIP = l.extractRemoteIP(r)
		}
		return fmt.Sprintf("%s:frontend", userIP), true
	}

	return fmt.Sprintf("%s:direct", l.extractRemoteIP(r)), false
}

func (l *Limiter) evictExpiredBounded(cutoff time.Time) {
	scanned := 0
	for k, timestamps := range l.records {
		if scanned >= evictScanBudget {
			break
		}
		scanned++
		active := false
		for _, ts := range timestamps {
			if ts.After(cutoff) {
				active = true
				break
			}
		}
		if !active {
			delete(l.records, k)
		}
	}
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

	l.opsCount++
	if l.opsCount%evictCheckInterval == 0 {
		l.evictExpiredBounded(cutoff)
	}

	return true, 0
}

// Reset clears all stored rate-limit records.
func (l *Limiter) Reset() {
	l.mu.Lock()
	defer l.mu.Unlock()
	l.records = make(map[string][]time.Time)
	l.opsCount = 0
}
