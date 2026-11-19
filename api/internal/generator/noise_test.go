package generator

import (
	"strings"
	"testing"
)

func TestInjectSpellingNoisePT(t *testing.T) {
	s := "Com certeza a análise do processo é essencial."
	res := InjectSpellingNoise(s, "pt")
	if res == s {
		t.Fatalf("expected spelling noise to modify PT sentence, got %q", res)
	}
}

func TestInjectSpellingNoiseEN(t *testing.T) {
	s := "We definitely need to separate the length and height."
	res := InjectSpellingNoise(s, "en")
	if res == s {
		t.Fatalf("expected spelling noise to modify EN sentence, got %q", res)
	}
}

func TestInjectSpellingNoiseES(t *testing.T) {
	s := "También es necesario hacer un análisis de la decisión."
	res := InjectSpellingNoise(s, "es")
	if res == s {
		t.Fatalf("expected spelling noise to modify ES sentence, got %q", res)
	}
}

func TestInjectSpellingNoiseFR(t *testing.T) {
	s := "Le développement de chaque événement est intéressant."
	res := InjectSpellingNoise(s, "fr")
	if res == s {
		t.Fatalf("expected spelling noise to modify FR sentence, got %q", res)
	}
}

func TestInjectSpellingNoiseFRUnicodeBoundaries(t *testing.T) {
	// Direct rule matching for non-ASCII start/end words
	for _, tc := range []struct {
		in, want string
	}{
		{"événement majeur", "évènement majeur"},
		{"malgré tout", "malgrés tout"},
	} {
		ruleList := spellingRules["fr"]
		matched := false
		for _, r := range ruleList {
			if out, ok := replaceFirst(r.re, tc.in, r.repl); ok && out == tc.want {
				matched = true
				break
			}
		}
		if !matched {
			t.Fatalf("expected rule match for %q -> %q", tc.in, tc.want)
		}
	}
}

func TestInjectSpellingNoiseUnknownLang(t *testing.T) {
	s := "Lorem ipsum dolor sit amet."
	if res := InjectSpellingNoise(s, "la"); res != s {
		t.Fatalf("expected unknown lang 'la' to be unchanged, got %q", res)
	}
}

func TestInjectGrammarNoiseShortSentence(t *testing.T) {
	s := "Curto demais."
	if res := InjectGrammarNoise(s, "pt"); res != s {
		t.Fatalf("expected short sentence to remain unchanged, got %q", res)
	}
}

func TestInjectGrammarNoiseAlemDissoPT(t *testing.T) {
	s := "Além disso o sistema funciona muito bem."
	res := InjectGrammarNoise(s, "pt")
	if !strings.HasPrefix(res, "Para além disso") {
		t.Fatalf("expected 'Para além disso' redundancy, got %q", res)
	}
}

func TestInjectGrammarNoiseLanguages(t *testing.T) {
	for lang, s := range map[string]string{
		"pt": "O sistema desenvolve uma solução eficiente para o cliente.",
		"en": "The system develops an efficient solution for the client.",
		"es": "El sistema desarrolla una solución eficiente para el cliente.",
		"fr": "Le système développe une solution efficace pour le client.",
	} {
		res := InjectGrammarNoise(s, lang)
		if res == "" {
			t.Fatalf("expected non-empty output for %s", lang)
		}
	}
}
