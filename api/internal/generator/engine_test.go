package generator

import (
	"regexp"
	"strings"
	"testing"
)

func TestShuffledDeckBasic(t *testing.T) {
	items := []string{"a", "b", "c"}
	deck := NewShuffledDeck(items)
	seen := map[string]bool{}
	for i := 0; i < 3; i++ {
		seen[deck.Draw()] = true
	}
	if len(seen) != 3 {
		t.Fatalf("expected all 3 items before reshuffle, got %v", seen)
	}
	// 4th draw reshuffles and returns a valid item
	next := deck.Draw()
	if !seen[next] {
		t.Fatalf("unexpected item %q after reshuffle", next)
	}
}

func TestGetStem(t *testing.T) {
	if s := GetStem("Ações", "pt"); s != "ac" {
		t.Fatalf("expected stem 'ac', got %q", s)
	}
	if s := GetStem("Running", "en"); s != "runn" {
		t.Fatalf("expected stem 'runn', got %q", s)
	}
}

func TestExtractContentWords(t *testing.T) {
	words := ExtractContentWords("en", "technology")
	if len(words) < 10 {
		t.Fatalf("expected at least 10 EN technology content words, got %d", len(words))
	}
	for _, w := range words {
		if len([]rune(w)) <= 2 {
			t.Fatalf("unexpected short word %q", w)
		}
	}

	frWords := ExtractContentWords("fr", "technology")
	for _, w := range frWords {
		if strings.HasPrefix(w, "d") && strings.Contains(w, "innovation") && w != "innovation" {
			t.Fatalf("unexpected merged elision token %q", w)
		}
	}
}

func TestGenerateContentAllLanguagesAndThemes(t *testing.T) {
	langs := []string{"pt", "en", "es", "fr", "la"}
	themes := []string{"business", "ecology", "law", "medicine", "mining", "politics", "technology"}
	types := []string{"words", "sentences", "paragraphs"}

	for _, lang := range langs {
		for _, theme := range themes {
			for _, outType := range types {
				res, err := GenerateContent(lang, outType, theme, 2, true, true)
				if err != nil {
					t.Fatalf("GenerateContent(%s, %s, %s) failed: %v", lang, outType, theme, err)
				}
				if outType == "words" {
					if len(res) != 1 || len(strings.Fields(res[0])) != 2 {
						t.Fatalf("expected 1 string with 2 words for (%s, %s), got %v", lang, theme, res)
					}
				} else if len(res) != 2 {
					t.Fatalf("expected 2 items for (%s, %s, %s), got %d", lang, outType, theme, len(res))
				}
			}
		}
	}
}

func TestGenerateContentInvalidTypeOrLang(t *testing.T) {
	if _, err := GenerateContent("de", "words", "business", 1, true, true); err == nil {
		t.Fatalf("expected error for unsupported language")
	}
	if _, err := GenerateContent("en", "poems", "business", 1, true, true); err == nil {
		t.Fatalf("expected error for invalid output type")
	}
}

func TestPortugueseContractionsAndNoConsecutiveSpaces(t *testing.T) {
	reDoubleSpace := regexp.MustCompile(`\s{2,}`)
	reSpacePunct := regexp.MustCompile(`\s+[.,]`)
	reBadPT := regexp.MustCompile(`(?i)\b(de o|de a|de os|de as|em o|em a|em os|em as|por o|por a|de este|de esta|em este|em esta)\b`)

	for i := 0; i < 30; i++ {
		res, err := GenerateContent("pt", "sentences", "mining", 3, true, true)
		if err != nil {
			t.Fatalf("unexpected error: %v", err)
		}
		for _, s := range res {
			if reDoubleSpace.MatchString(s) {
				t.Fatalf("consecutive spaces found in %q", s)
			}
			if reSpacePunct.MatchString(s) {
				t.Fatalf("space before punctuation found in %q", s)
			}
			if reBadPT.MatchString(s) {
				t.Fatalf("uncontracted PT preposition found in %q", s)
			}
		}
	}
}

func TestFrenchAndSpanishContractions(t *testing.T) {
	reBadES := regexp.MustCompile(`(?i)\b(de el|a el)\b`)
	reBadFR := regexp.MustCompile(`(?i)(^|\s)(de le|de les|à le|à les)\b`)

	for i := 0; i < 20; i++ {
		esRes, _ := GenerateContent("es", "sentences", "law", 3, true, true)
		for _, s := range esRes {
			if reBadES.MatchString(s) {
				t.Fatalf("uncontracted ES preposition in %q", s)
			}
		}
		frRes, _ := GenerateContent("fr", "sentences", "business", 3, true, true)
		for _, s := range frRes {
			if reBadFR.MatchString(s) {
				t.Fatalf("uncontracted FR preposition in %q", s)
			}
		}
	}
}

func TestNoisyModeProducesValidOutput(t *testing.T) {
	for _, lang := range []string{"pt", "en", "es", "fr"} {
		res, err := GenerateContent(lang, "paragraphs", "technology", 2, false, false)
		if err != nil || len(res) != 2 {
			t.Fatalf("noisy generation failed for %s: %v", lang, err)
		}
	}
}
