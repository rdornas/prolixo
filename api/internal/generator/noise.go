package generator

import (
	"math/rand/v2"
	"regexp"
	"strings"
	"unicode"
)

type spellingRule struct {
	re   *regexp.Regexp
	repl string
}

var spellingRules map[string][]spellingRule

var (
	reAlemDissoLower = regexp.MustCompile(`(?i)\balém disso\b`)
	reAlemDissoCap   = regexp.MustCompile(`\bAlém disso\b`)
)

func init() {
	raw := map[string][][2]string{
		"pt": {
			{`\bcom certeza\b`, "concerteza"},
			{`\bCom certeza\b`, "Concerteza"},
			{`\bexceção\b`, "excessão"},
			{`\bExceção\b`, "Excessão"},
			{`\bde repente\b`, "derrepente"},
			{`\bDe repente\b`, "Derrepente"},
			{`\ba partir de\b`, "apartir de"},
			{`\bA partir de\b`, "Apartir de"},
			{`\bem cima\b`, "emcima"},
			{`\bprivilégio\b`, "previlégio"},
			{`\breivindicar\b`, "reinvindicar"},
			{`\batravés\b`, "atravez"},
			{`\banálise\b`, "analise"},
			{`\bAnálise\b`, "Analise"},
			{`\bestratégico\b`, "estrategico"},
			{`\bestratégica\b`, "estrategica"},
			{`\bestratégicos\b`, "estrategicos"},
			{`\bestratégicas\b`, "estrategicas"},
			{`\beficiência\b`, "eficiencia"},
			{`\bdisrupção\b`, "disrupçao"},
			{`\bessencial\b`, "ecencial"},
			{`\bprocesso\b`, "proceço"},
			{`\bconsenso\b`, "comcenso"},
			{`\bnecessário\b`, "necessario"},
			{`\bnecessária\b`, "necessaria"},
			{`\binteligência\b`, "inteligencia"},
			{`\btecnológico\b`, "tecnologico"},
			{`\btecnológica\b`, "tecnologica"},
		},
		"en": {
			{`\bdefinitely\b`, "definately"},
			{`\bDefinitely\b`, "Definately"},
			{`\bseparate\b`, "seperate"},
			{`\bSeparate\b`, "Seperate"},
			{`\breceive\b`, "recieve"},
			{`\bReceive\b`, "Recieve"},
			{`\blength\b`, "lenght"},
			{`\bLength\b`, "Lenght"},
			{`\bheight\b`, "heigth"},
			{`\bHeight\b`, "Heigth"},
			{`\bwidth\b`, "widht"},
			{`\bWidth\b`, "Widht"},
			{`\bdepth\b`, "depht"},
			{`\bDepth\b`, "Depht"},
			{`\bstrength\b`, "strenght"},
			{`\bStrength\b`, "Strenght"},
			{`\bweight\b`, "weigth"},
			{`\bWeight\b`, "Weigth"},
			{`\bstraight\b`, "straigth"},
			{`\bStraight\b`, "Straigth"},
			{`\bweird\b`, "wierd"},
			{`\bneighbor\b`, "nieghbor"},
			{`\bthroughput\b`, "througput"},
			{`\boccurrence\b`, "occurance"},
			{`\buntil\b`, "untill"},
			{`\bsuccessful\b`, "succesful"},
			{`\bnecessary\b`, "neccessary"},
			{`\benvironment\b`, "enviroment"},
			{`\bgovernment\b`, "goverment"},
			{`\bdevelopment\b`, "developement"},
			{`\baccommodate\b`, "accomodate"},
			{`\bmaintenance\b`, "maintainance"},
			{`\bcalendar\b`, "calender"},
			{`\bforeign\b`, "foriegn"},
			{`\btheir\b`, "there"},
			{`\bprinciple\b`, "principal"},
		},
		"es": {
			{`\ba ver\b`, "haber"},
			{`\bA ver\b`, "Haber"},
			{`\bhecho\b`, "echo"},
			{`\btambién\b`, "tambien"},
			{`\bTambién\b`, "Tambien"},
			{`\banálisis\b`, "analisis"},
			{`\bAnálisis\b`, "Analisis"},
			{`\bdecisión\b`, "decision"},
			{`\bdesarrollo\b`, "desarolo"},
			{`\bexcepción\b`, "escepción"},
			{`\bnecesario\b`, "necesário"},
			{`\bhubiera\b`, "hubiese sido"},
			{`\beconómico\b`, "economico"},
			{`\beconómica\b`, "economica"},
		},
		"fr": {
			{`\bdéveloppement\b`, "dévelopement"},
			{`\bévénement\b`, "évènement"},
			{`\bconnexion\b`, "connection"},
			{`\blangage\b`, "language"},
			{`\baccueil\b`, "acceuil"},
			{`\bintéressant\b`, "interressant"},
			{`\bchaque\b`, "chaques"},
			{`\bparmi\b`, "parmis"},
			{`\bmalgré\b`, "malgrés"},
		},
	}

	spellingRules = make(map[string][]spellingRule, len(raw))
	for lang, pairs := range raw {
		compiled := make([]spellingRule, 0, len(pairs))
		for _, p := range pairs {
			compiled = append(compiled, spellingRule{
				re:   regexp.MustCompile(p[0]),
				repl: p[1],
			})
		}
		spellingRules[lang] = compiled
	}
}

func replaceFirst(re *regexp.Regexp, s, repl string) (string, bool) {
	loc := re.FindStringIndex(s)
	if loc == nil {
		return s, false
	}
	return s[:loc[0]] + repl + s[loc[1]:], true
}

func isAlphaWord(w string) bool {
	if w == "" {
		return false
	}
	for _, r := range w {
		if !unicode.IsLetter(r) {
			return false
		}
	}
	return true
}

// InjectSpellingNoise injects realistic spelling mistakes into a sentence.
func InjectSpellingNoise(sentence, lang string) string {
	rules, ok := spellingRules[lang]
	if !ok {
		return sentence
	}

	shuffled := make([]spellingRule, len(rules))
	copy(shuffled, rules)
	rand.Shuffle(len(shuffled), func(i, j int) {
		shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
	})

	modified := sentence
	applied := 0
	for _, r := range shuffled {
		if next, changed := replaceFirst(r.re, modified, r.repl); changed {
			modified = next
			applied++
			if applied >= 2 {
				break
			}
		}
	}

	if applied == 0 {
		words := strings.Fields(modified)
		var candidates []int
		for i, w := range words {
			if len([]rune(w)) > 5 && isAlphaWord(w) {
				candidates = append(candidates, i)
			}
		}
		if len(candidates) > 0 {
			idx := candidates[rand.IntN(len(candidates))]
			w := words[idx]
			switch {
			case lang == "en" && strings.Contains(w, "ght"):
				words[idx] = strings.Replace(w, "ght", "gth", 1)
			case lang == "en" && strings.Contains(w, "gth"):
				words[idx] = strings.Replace(w, "gth", "ght", 1)
			case lang == "en" && strings.Contains(w, "ei"):
				words[idx] = strings.Replace(w, "ei", "ie", 1)
			case lang == "en" && strings.Contains(w, "ie"):
				words[idx] = strings.Replace(w, "ie", "ei", 1)
			case strings.Contains(w, "ss"):
				words[idx] = strings.Replace(w, "ss", "s", 1)
			case strings.Contains(w, "ç"):
				words[idx] = strings.Replace(w, "ç", "ss", 1)
			case strings.Contains(w, "é"):
				words[idx] = strings.Replace(w, "é", "e", 1)
			case strings.Contains(w, "á"):
				words[idx] = strings.Replace(w, "á", "a", 1)
			case strings.Contains(w, "ó"):
				words[idx] = strings.Replace(w, "ó", "o", 1)
			case strings.Contains(w, "í"):
				words[idx] = strings.Replace(w, "í", "i", 1)
			case strings.Contains(w, "ã"):
				words[idx] = strings.Replace(w, "ã", "an", 1)
			default:
				runes := []rune(w)
				if len(runes) > 4 {
					pos := 1 + rand.IntN(len(runes)-3)
					runes[pos], runes[pos+1] = runes[pos+1], runes[pos]
					words[idx] = string(runes)
				}
			}
			modified = strings.Join(words, " ")
		}
	}

	return modified
}

var dupTargets = map[string]map[string]bool{
	"pt": {"o": true, "a": true, "os": true, "as": true, "de": true, "em": true, "que": true, "para": true, "com": true, "no": true, "na": true},
	"en": {"the": true, "a": true, "an": true, "of": true, "in": true, "to": true, "that": true, "for": true, "with": true, "and": true},
	"es": {"el": true, "la": true, "los": true, "las": true, "de": true, "en": true, "que": true, "para": true, "con": true, "del": true},
	"fr": {"le": true, "la": true, "les": true, "de": true, "en": true, "que": true, "pour": true, "avec": true, "du": true, "des": true},
}

// InjectGrammarNoise injects grammatical discrepancies or stylistic redundancies.
func InjectGrammarNoise(sentence, lang string) string {
	if lang == "pt" && reAlemDissoLower.MatchString(sentence) {
		if reAlemDissoCap.MatchString(sentence) {
			out, _ := replaceFirst(reAlemDissoCap, sentence, "Para além disso")
			return out
		}
		out, _ := replaceFirst(reAlemDissoLower, sentence, "para além disso")
		return out
	}

	words := strings.Fields(sentence)
	if len(words) < 4 {
		return sentence
	}

	noiseTypes := [3]string{"duplication", "disagreement", "gender_mismatch"}
	noiseType := noiseTypes[rand.IntN(len(noiseTypes))]

	switch noiseType {
	case "duplication":
		targets, ok := dupTargets[lang]
		if !ok {
			targets = map[string]bool{"the": true, "de": true, "a": true}
		}
		var candidates []int
		for i, w := range words {
			clean := strings.Trim(strings.ToLower(w), ".,;:!?")
			if targets[clean] {
				candidates = append(candidates, i)
			}
		}
		var idx int
		if len(candidates) > 0 {
			idx = candidates[rand.IntN(len(candidates))]
		} else {
			upper := min(4, len(words)-1)
			idx = 1 + rand.IntN(upper)
		}
		inserted := strings.Trim(strings.ToLower(words[idx]), ".,;:!?")
		words = append(words[:idx], append([]string{inserted}, words[idx:]...)...)

	case "disagreement":
		if lang == "pt" || lang == "es" {
			for i := 0; i < len(words)-1; i++ {
				clean := strings.ToLower(words[i])
				switch clean {
				case "os", "estes", "los", "estos":
					words[i] = "o"
					return strings.Join(words, " ")
				case "as", "estas", "diversos", "diversas", "las":
					words[i] = "a"
					return strings.Join(words, " ")
				case "o", "este", "el":
					words[i] = "os"
					return strings.Join(words, " ")
				case "a", "esta", "la":
					words[i] = "as"
					return strings.Join(words, " ")
				}
			}
		} else if lang == "en" {
			for i, w := range words {
				clean := strings.ToLower(w)
				switch clean {
				case "develops", "optimizes", "drives", "creates", "enables":
					words[i] = w[:len(w)-1]
					return strings.Join(words, " ")
				case "develop", "optimize", "drive", "create", "enable":
					words[i] = w + "s"
					return strings.Join(words, " ")
				}
			}
		}

	case "gender_mismatch":
		switch lang {
		case "pt":
			for i, w := range words {
				switch strings.ToLower(w) {
				case "o":
					words[i] = "a"
					return strings.Join(words, " ")
				case "a":
					words[i] = "o"
					return strings.Join(words, " ")
				case "um":
					words[i] = "uma"
					return strings.Join(words, " ")
				case "uma":
					words[i] = "um"
					return strings.Join(words, " ")
				}
			}
		case "es":
			for i, w := range words {
				switch strings.ToLower(w) {
				case "el":
					words[i] = "la"
					return strings.Join(words, " ")
				case "la":
					words[i] = "el"
					return strings.Join(words, " ")
				case "un":
					words[i] = "una"
					return strings.Join(words, " ")
				}
			}
		case "fr":
			for i, w := range words {
				switch strings.ToLower(w) {
				case "le":
					words[i] = "la"
					return strings.Join(words, " ")
				case "la":
					words[i] = "le"
					return strings.Join(words, " ")
				}
			}
		}
	}

	return strings.Join(words, " ")
}
