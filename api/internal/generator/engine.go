package generator

import (
	"errors"
	"fmt"
	"math/rand/v2"
	"regexp"
	"strings"
	"unicode"
	"unicode/utf8"
)

// ErrInvalidInput indicates a client-side validation error (HTTP 400).
type ErrInvalidInput struct {
	Msg string
}

func (e ErrInvalidInput) Error() string {
	return e.Msg
}

// ShuffledDeck manages random string draws without immediate replacement.
type ShuffledDeck struct {
	items []string
	deck  []string
}

// NewShuffledDeck creates and shuffles a new deck from items.
func NewShuffledDeck(items []string) *ShuffledDeck {
	d := &ShuffledDeck{items: items}
	d.Reset()
	return d
}

// Reset refills and shuffles the deck.
func (d *ShuffledDeck) Reset() {
	d.deck = make([]string, len(d.items))
	copy(d.deck, d.items)
	rand.Shuffle(len(d.deck), func(i, j int) {
		d.deck[i], d.deck[j] = d.deck[j], d.deck[i]
	})
}

// Draw pops the next item, reshuffling automatically when exhausted.
func (d *ShuffledDeck) Draw() string {
	if len(d.deck) == 0 {
		d.Reset()
	}
	n := len(d.deck) - 1
	val := d.deck[n]
	d.deck = d.deck[:n]
	return val
}

// CFGEngine generates sentences from a Context-Free Grammar and lexicon decks.
type CFGEngine struct {
	grammar map[string][][]string
	decks   map[string]*ShuffledDeck
}

// NewCFGEngine builds a CFGEngine with ShuffledDecks for each lexical category.
func NewCFGEngine(grammar map[string][][]string, lexicon map[string][]string) *CFGEngine {
	decks := make(map[string]*ShuffledDeck, len(lexicon))
	for k, v := range lexicon {
		decks[k] = NewShuffledDeck(v)
	}
	return &CFGEngine{
		grammar: grammar,
		decks:   decks,
	}
}

// Expand recursively expands a CFG symbol.
func (e *CFGEngine) Expand(symbol string) string {
	hasPunct := false
	punct := ""
	clean := symbol
	if strings.HasSuffix(symbol, ".") || strings.HasSuffix(symbol, ",") {
		hasPunct = true
		punct = symbol[len(symbol)-1:]
		clean = symbol[:len(symbol)-1]
	}

	var result string
	if prods, ok := e.grammar[clean]; ok {
		prod := prods[rand.IntN(len(prods))]
		parts := make([]string, 0, len(prod))
		for _, sym := range prod {
			exp := e.Expand(sym)
			if exp != "" {
				parts = append(parts, exp)
			}
		}
		result = strings.Join(parts, " ")
	} else if deck, ok := e.decks[clean]; ok {
		result = deck.Draw()
	} else {
		result = clean
	}

	if hasPunct {
		return strings.TrimRight(result, " \t\n\r") + punct
	}
	return result
}

type contractionRule struct {
	re   *regexp.Regexp
	repl string
}

var (
	reSpaceBeforePunct = regexp.MustCompile(`\s+([.,])`)
	reMultiSpace       = regexp.MustCompile(`\s+`)
	ptContractions     []contractionRule
	esContractions     []contractionRule
	frContractions     []contractionRule
)

func compileContractions(pairs [][2]string) []contractionRule {
	out := make([]contractionRule, 0, len(pairs))
	for _, p := range pairs {
		out = append(out, contractionRule{
			re:   regexp.MustCompile(`(?i)\b` + p[0] + `\b`),
			repl: p[1],
		})
	}
	return out
}

func init() {
	ptContractions = compileContractions([][2]string{
		{"de o", "do"}, {"de a", "da"}, {"de os", "dos"}, {"de as", "das"},
		{"de este", "deste"}, {"de esta", "desta"}, {"de estes", "destes"}, {"de estas", "destas"}, {"de isto", "disto"},
		{"de esse", "desse"}, {"de essa", "dessa"}, {"de esses", "desses"}, {"de essas", "dessas"}, {"de isso", "disso"},
		{"de aquele", "daquele"}, {"de aquela", "daquela"}, {"de aqueles", "daqueles"}, {"de aquelas", "daquelas"}, {"de aquilo", "daquilo"},
		{"de ele", "dele"}, {"de ela", "dela"}, {"de eles", "deles"}, {"de elas", "delas"},
		{"em o", "no"}, {"em a", "na"}, {"em os", "nos"}, {"em as", "nas"},
		{"em este", "neste"}, {"em esta", "nesta"}, {"em estes", "nestes"}, {"em estas", "nestas"}, {"em isto", "nisto"},
		{"em esse", "nesse"}, {"em essa", "nessa"}, {"em esses", "nesses"}, {"em essas", "nessas"}, {"em isso", "nisso"},
		{"em aquele", "naquele"}, {"em aquela", "naquela"}, {"em aqueles", "naqueles"}, {"em aquelas", "naquelas"}, {"em aquilo", "naquilo"},
		{"em ele", "nele"}, {"em ela", "nela"}, {"em eles", "neles"}, {"em elas", "nelas"},
		{"a a", "à"}, {"a as", "às"}, {"a o", "ao"}, {"a os", "aos"},
		{"a aquele", "àquele"}, {"a aquela", "àquela"}, {"a aqueles", "àqueles"}, {"a aquelas", "àquelas"}, {"a aquilo", "àquilo"},
		{"por o", "pelo"}, {"por a", "pela"}, {"por os", "pelos"}, {"por as", "pelas"},
	})

	esContractions = compileContractions([][2]string{
		{"de el", "del"},
		{"a el", "al"},
	})

	frContractions = []contractionRule{
		{re: regexp.MustCompile(`(?i)\bde le\b`), repl: "du"},
		{re: regexp.MustCompile(`(?i)\bde les\b`), repl: "des"},
		// 'à' is non-ASCII so RE2 \b does not match before it; match start or whitespace
		{re: regexp.MustCompile(`(?i)(^|\s)à le\b`), repl: "${1}au"},
		{re: regexp.MustCompile(`(?i)(^|\s)à les\b`), repl: "${1}aux"},
	}
}

func collapseDuplicateWords(text string) string {
	tokens := strings.Fields(text)
	if len(tokens) < 2 {
		return text
	}
	out := make([]string, 0, len(tokens))
	for _, tok := range tokens {
		core := strings.TrimRight(tok, ".,;:!?")
		if len(out) > 0 && core != "" && isAlphaWord(core) {
			prev := out[len(out)-1]
			prevCore := strings.TrimRight(prev, ".,;:!?")
			if prevCore == prev && strings.EqualFold(prevCore, core) {
				// Replace previous bare duplicate with current token (keeping any trailing punct)
				out[len(out)-1] = prev[:len(prevCore)] + tok[len(core):]
				continue
			}
		}
		out = append(out, tok)
	}
	return strings.Join(out, " ")
}

func capitalizeFirst(s string) string {
	s = strings.TrimSpace(s)
	if s == "" {
		return s
	}
	r, size := utf8.DecodeRuneInString(s)
	return string(unicode.ToUpper(r)) + s[size:]
}

// GenerateSentence produces a single sentence with optional grammar/orthography noise.
func (e *CFGEngine) GenerateSentence(lang string, grammarCorrect, orthographyCorrect bool) string {
	text := e.Expand("S")
	text = reSpaceBeforePunct.ReplaceAllString(text, "$1")
	text = strings.TrimSpace(reMultiSpace.ReplaceAllString(text, " "))

	if grammarCorrect {
		text = collapseDuplicateWords(text)
		var rules []contractionRule
		switch lang {
		case "pt":
			rules = ptContractions
		case "es":
			rules = esContractions
		case "fr":
			rules = frContractions
		}
		for _, r := range rules {
			text = r.re.ReplaceAllString(text, r.repl)
		}
	} else {
		text = InjectGrammarNoise(text, lang)
	}

	if !orthographyCorrect {
		text = InjectSpellingNoise(text, lang)
	}

	return capitalizeFirst(text)
}

// MarkovEngine generates classical Latin sentences using an Order-2 Markov chain.
type MarkovEngine struct {
	order       int
	transitions map[[2]string][]string
	startStates [][2]string
}

// NewMarkovEngine trains an Order-2 Markov chain on the given sentences.
func NewMarkovEngine(sentences []string) *MarkovEngine {
	m := &MarkovEngine{
		order:       2,
		transitions: make(map[[2]string][]string),
	}
	for _, s := range sentences {
		words := strings.Fields(s)
		if len(words) <= m.order {
			continue
		}
		start := [2]string{words[0], words[1]}
		m.startStates = append(m.startStates, start)
		for i := 0; i < len(words)-m.order; i++ {
			state := [2]string{words[i], words[i+1]}
			m.transitions[state] = append(m.transitions[state], words[i+2])
		}
	}
	return m
}

// GenerateSentence generates a single Latin sentence.
func (m *MarkovEngine) GenerateSentence() string {
	if len(m.transitions) == 0 || len(m.startStates) == 0 {
		return "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
	}

	state := m.startStates[rand.IntN(len(m.startStates))]
	words := []string{state[0], state[1]}

	maxWords := 8 + rand.IntN(9) // [8, 16]
	for i := 0; i < maxWords-m.order; i++ {
		nextOpts, ok := m.transitions[state]
		if !ok || len(nextOpts) == 0 {
			break
		}
		nextWord := nextOpts[rand.IntN(len(nextOpts))]
		words = append(words, nextWord)
		state = [2]string{words[len(words)-2], words[len(words)-1]}
		if strings.HasSuffix(nextWord, ".") || strings.HasSuffix(nextWord, "?") || strings.HasSuffix(nextWord, "!") {
			break
		}
	}

	sentence := capitalizeFirst(strings.Join(words, " "))
	if !strings.HasSuffix(sentence, ".") && !strings.HasSuffix(sentence, "?") && !strings.HasSuffix(sentence, "!") {
		sentence += "."
	}
	return sentence
}

var romanceGrammar = map[string][][]string{
	"S":          {{"INTRO", "S_BODY."}, {"CIRC_INTRO", "S_BODY."}, {"S_BODY."}},
	"INTRO":      {{"intro"}},
	"CIRC_INTRO": {{"circ,"}},
	"S_BODY":     {{"NP_s", "VP_s"}, {"NP_p", "VP_p"}, {"NP_s", "VP_s", "CONJ", "NP_s", "VP_s"}, {"NP_p", "VP_p", "CONJ", "NP_p", "VP_p"}},
	"CONJ":       {{"conj"}},
	"NP_s":       {{"NP_ms"}, {"NP_fs"}},
	"NP_p":       {{"NP_mp"}, {"NP_fp"}},
	"NP_ms":      {{"art_ms", "n_ms"}, {"art_ms", "n_ms", "adj_ms"}, {"n_ms", "PP_s"}},
	"NP_fs":      {{"art_fs", "n_fs"}, {"art_fs", "n_fs", "adj_fs"}, {"n_fs", "PP_s"}},
	"NP_mp":      {{"art_mp", "n_mp"}, {"art_mp", "n_mp", "adj_mp"}, {"n_mp", "PP_p"}},
	"NP_fp":      {{"art_fp", "n_fp"}, {"art_fp", "n_fp", "adj_fp"}, {"n_fp", "PP_p"}},
	"VP_s":       {{"v_trans_s", "NP_s"}, {"v_trans_s", "NP_p"}, {"v_intrans_s"}},
	"VP_p":       {{"v_trans_p", "NP_s"}, {"v_trans_p", "NP_p"}, {"v_intrans_p"}},
	"PP_s":       {{"prep", "NP_ms"}, {"prep", "NP_fs"}},
	"PP_p":       {{"prep", "NP_mp"}, {"prep", "NP_fp"}},
}

var englishGrammar = map[string][][]string{
	"S":          {{"INTRO", "S_BODY."}, {"CIRC_INTRO", "S_BODY."}, {"S_BODY."}},
	"INTRO":      {{"intro"}},
	"CIRC_INTRO": {{"circ,"}},
	"S_BODY":     {{"NP_s", "VP_s"}, {"NP_p", "VP_p"}, {"NP_s", "VP_s", "CONJ", "NP_s", "VP_s"}, {"NP_p", "VP_p", "CONJ", "NP_p", "VP_p"}},
	"CONJ":       {{"conj"}},
	"NP_s":       {{"art_s", "n_s"}, {"art_s", "adj", "n_s"}, {"n_s", "PP"}},
	"NP_p":       {{"art_p", "n_p"}, {"art_p", "adj", "n_p"}, {"n_p", "PP"}},
	"VP_s":       {{"v_trans_s", "NP_s"}, {"v_trans_s", "NP_p"}, {"v_intrans_s"}},
	"VP_p":       {{"v_trans_p", "NP_s"}, {"v_trans_p", "NP_p"}, {"v_intrans_p"}},
	"PP":         {{"prep", "NP_s"}, {"prep", "NP_p"}},
}

var stopWords = map[string]map[string]bool{
	"pt": {
		"o": true, "a": true, "os": true, "as": true, "um": true, "uma": true, "uns": true, "umas": true,
		"de": true, "do": true, "da": true, "dos": true, "das": true, "em": true, "no": true, "na": true,
		"nos": true, "nas": true, "para": true, "por": true, "com": true, "sob": true, "sobre": true,
		"ante": true, "até": true, "após": true, "contra": true, "desde": true, "entre": true, "perante": true,
		"sem": true, "e": true, "ou": true, "mas": true, "que": true, "se": true, "ao": true, "aos": true,
		"à": true, "às": true, "pelo": true, "pela": true, "pelos": true, "pelas": true, "este": true,
		"esta": true, "estes": true, "estas": true, "qualquer": true, "determinado": true, "determinada": true,
		"certos": true, "certas": true, "diversos": true, "diversas": true, "respectivo": true, "respectiva": true,
	},
	"en": {
		"a": true, "an": true, "the": true, "this": true, "that": true, "these": true, "those": true,
		"any": true, "each": true, "some": true, "several": true, "various": true, "of": true, "for": true,
		"in": true, "on": true, "at": true, "to": true, "from": true, "with": true, "by": true, "about": true,
		"against": true, "between": true, "into": true, "through": true, "during": true, "before": true,
		"after": true, "above": true, "below": true, "and": true, "but": true, "if": true, "or": true,
		"because": true, "as": true, "until": true, "while": true, "which": true, "who": true, "whom": true,
		"respective": true,
	},
	"es": {
		"el": true, "la": true, "los": true, "las": true, "un": true, "una": true, "unos": true, "unas": true,
		"de": true, "del": true, "al": true, "en": true, "para": true, "por": true, "con": true, "sin": true,
		"sobre": true, "entre": true, "hacia": true, "hasta": true, "durante": true, "mediante": true, "y": true,
		"o": true, "pero": true, "que": true, "si": true, "como": true, "este": true, "esta": true, "estos": true,
		"estas": true, "cualquier": true, "determinado": true, "determinada": true, "ciertos": true,
		"ciertas": true, "diversos": true, "diversas": true, "respectivo": true, "respectiva": true,
	},
	"fr": {
		"de": true, "la": true, "le": true, "les": true, "un": true, "une": true, "des": true, "du": true,
		"au": true, "aux": true, "en": true, "pour": true, "par": true, "sur": true, "dans": true, "avec": true,
		"sans": true, "sous": true, "et": true, "ou": true, "mais": true, "que": true, "qui": true, "comme": true,
		"ce": true, "cette": true, "ces": true, "tout": true, "toute": true, "tous": true, "toutes": true,
		"certains": true, "certaines": true, "plusieurs": true, "respectif": true, "respective": true,
	},
	"la": {
		"et": true, "in": true, "ad": true, "ac": true, "ut": true, "ex": true, "a": true, "ab": true,
		"is": true, "ea": true, "id": true, "sed": true, "si": true, "cum": true, "per": true, "non": true, "nec": true,
	},
}

func cleanToken(tok string) string {
	var b strings.Builder
	for _, r := range tok {
		if unicode.IsLetter(r) || unicode.IsDigit(r) || r == '_' || r == '-' {
			b.WriteRune(unicode.ToLower(r))
		}
	}
	return strings.TrimSpace(b.String())
}

// ExtractContentWords extracts deduplicated content words for a language and theme.
func ExtractContentWords(lang, theme string) []string {
	var rawSources []string
	if langThemes, ok := themesData[lang]; ok {
		if tEntry, ok := langThemes[theme]; ok {
			rawSources = append(rawSources, tEntry.List...)
			for _, list := range tEntry.Map {
				rawSources = append(rawSources, list...)
			}
		}
	}

	if len(rawSources) == 0 {
		switch lang {
		case "pt", "es", "fr":
			d := romanceDictFor(lang)
			keys := []string{"n_ms", "n_fs", "n_mp", "n_fp", "adj_ms", "adj_fs", "adj_mp", "adj_fp", "v_trans_s", "v_trans_p", "v_intrans_s", "v_intrans_p"}
			for _, k := range keys {
				rawSources = append(rawSources, d[k]...)
			}
		case "en":
			keys := []string{"n_s", "n_p", "adj", "v_trans_s", "v_trans_p", "v_intrans_s", "v_intrans_p"}
			for _, k := range keys {
				rawSources = append(rawSources, enDict[k]...)
			}
		case "la":
			rawSources = append(rawSources, laDict.Sentences...)
		}
	}

	sw := stopWords[lang]
	seen := make(map[string]bool)
	var words []string
	for _, text := range rawSources {
		for _, tok := range strings.FieldsFunc(text, func(r rune) bool {
			return unicode.IsSpace(r) || r == '\'' || r == '’'
		}) {
			ct := cleanToken(tok)
			if len([]rune(ct)) > 2 && !sw[ct] && !seen[ct] {
				seen[ct] = true
				words = append(words, ct)
			}
		}
	}
	return words
}

func stripAccents(s string) string {
	var b strings.Builder
	for _, r := range s {
		switch r {
		case 'á', 'à', 'â', 'ã', 'ä', 'å':
			b.WriteByte('a')
		case 'é', 'è', 'ê', 'ë':
			b.WriteByte('e')
		case 'í', 'ì', 'î', 'ï':
			b.WriteByte('i')
		case 'ó', 'ò', 'ô', 'õ', 'ö':
			b.WriteByte('o')
		case 'ú', 'ù', 'û', 'ü':
			b.WriteByte('u')
		case 'ç':
			b.WriteByte('c')
		case 'ñ':
			b.WriteByte('n')
		case 'ý', 'ÿ':
			b.WriteByte('y')
		default:
			if r < 128 {
				b.WriteRune(r)
			}
		}
	}
	return b.String()
}

var (
	stemPTES1 = regexp.MustCompile(`(oes|ao|on)$`)
	stemPTES2 = regexp.MustCompile(`(ando|endo|indo|aram|eram|iram|avam|evam|ivam|am|em|ou|ar|er|ir)$`)
	stemPTES3 = regexp.MustCompile(`(ico|ica|icos|icas|ia|ias)$`)
	stemPTES4 = regexp.MustCompile(`(es|os|as|is|s)$`)
	stemPTES5 = regexp.MustCompile(`(o|a|e)$`)

	stemFR1 = regexp.MustCompile(`(ement|ment|issant|ant|ent|er|ir|re|ait|aient|ont|eaux|aux|es|e|s)$`)
	stemFR2 = regexp.MustCompile(`(ique|iques|isme|ismes|iste|istes|tion|tions)$`)

	stemEN = regexp.MustCompile(`(ing|edly|ed|es|s|ly|ic|ical)$`)
	stemLA = regexp.MustCompile(`(orum|arum|ibus|um|am|em|os|as|es|is|us|a|e|o)$`)
)

// GetStem computes a lightweight morphological stem for word deduplication.
func GetStem(word, lang string) string {
	w := stripAccents(strings.ToLower(strings.TrimSpace(word)))
	switch lang {
	case "pt", "es":
		w = stemPTES1.ReplaceAllString(w, "")
		w = stemPTES2.ReplaceAllString(w, "")
		w = stemPTES3.ReplaceAllString(w, "")
		w = stemPTES4.ReplaceAllString(w, "")
		w = stemPTES5.ReplaceAllString(w, "")
	case "fr":
		w = stemFR1.ReplaceAllString(w, "")
		w = stemFR2.ReplaceAllString(w, "")
	case "en":
		w = stemEN.ReplaceAllString(w, "")
	case "la":
		w = stemLA.ReplaceAllString(w, "")
	}
	return w
}

func romanceDictFor(lang string) romanceDict {
	switch lang {
	case "pt":
		return ptDict
	case "es":
		return esDict
	case "fr":
		return frDict
	default:
		return nil
	}
}

func getOrFallback(tData map[string][]string, base map[string][]string, key string) []string {
	if tData != nil {
		if v, ok := tData[key]; ok && len(v) > 0 {
			return v
		}
	}
	return base[key]
}

// GenerateContent generates words, sentences, or paragraphs for the given parameters.
func GenerateContent(lang, outputType, theme string, count int, grammarCorrect, orthographyCorrect bool) ([]string, error) {
	switch lang {
	case "pt", "en", "es", "fr", "la":
	default:
		return nil, ErrInvalidInput{Msg: fmt.Sprintf("Unsupported language: %s", lang)}
	}

	switch outputType {
	case "words", "sentences", "paragraphs":
	default:
		return nil, ErrInvalidInput{Msg: fmt.Sprintf("Invalid output type: %s", outputType)}
	}

	if lang == "la" {
		if outputType == "words" {
			contentWords := ExtractContentWords("la", "business")
			deck := NewShuffledDeck(contentWords)
			drawn := make([]string, 0, count)
			for len(drawn) < count {
				drawn = append(drawn, deck.Draw())
			}
			return []string{strings.Join(drawn, " ")}, nil
		}

		engine := NewMarkovEngine(laDict.Sentences)
		if outputType == "sentences" {
			out := make([]string, count)
			for i := 0; i < count; i++ {
				out[i] = engine.GenerateSentence()
			}
			return out, nil
		}

		paragraphs := make([]string, count)
		for i := 0; i < count; i++ {
			numSentences := 3 + rand.IntN(3) // [3, 5]
			sents := make([]string, numSentences)
			for j := 0; j < numSentences; j++ {
				sents[j] = engine.GenerateSentence()
			}
			paragraphs[i] = strings.Join(sents, " ")
		}
		return paragraphs, nil
	}

	if outputType == "words" {
		contentWords := ExtractContentWords(lang, theme)
		if len(contentWords) == 0 {
			return nil, errors.New("no content words available")
		}
		deck := NewShuffledDeck(contentWords)
		drawn := make([]string, 0, count)
		usedStems := make(map[string]bool)
		maxAttempts := len(contentWords) * 4
		for attempts := 0; len(drawn) < count && attempts < maxAttempts; attempts++ {
			w := deck.Draw()
			stem := GetStem(w, lang)
			if !usedStems[stem] {
				usedStems[stem] = true
				drawn = append(drawn, w)
			}
		}
		for len(drawn) < count {
			drawn = append(drawn, deck.Draw())
		}
		return []string{strings.Join(drawn, " ")}, nil
	}

	var tData map[string][]string
	if langThemes, ok := themesData[lang]; ok {
		if entry, ok := langThemes[theme]; ok {
			tData = entry.Map
		}
	}

	var engine *CFGEngine
	if lang == "en" {
		lexicon := map[string][]string{
			"art_s":       enDict["art_s"],
			"art_p":       enDict["art_p"],
			"n_s":         getOrFallback(tData, enDict, "n_s"),
			"n_p":         getOrFallback(tData, enDict, "n_p"),
			"adj":         getOrFallback(tData, enDict, "adj"),
			"v_trans_s":   getOrFallback(tData, enDict, "v_trans_s"),
			"v_trans_p":   getOrFallback(tData, enDict, "v_trans_p"),
			"v_intrans_s": getOrFallback(tData, enDict, "v_intrans_s"),
			"v_intrans_p": getOrFallback(tData, enDict, "v_intrans_p"),
			"prep":        enDict["prep"],
			"conj":        enDict["conj"],
			"intro":       getOrFallback(tData, enDict, "intro"),
			"circ":        getOrFallback(tData, enDict, "circ"),
		}
		engine = NewCFGEngine(englishGrammar, lexicon)
	} else {
		base := romanceDictFor(lang)
		lexicon := map[string][]string{
			"art_ms":      base["art_ms"],
			"art_fs":      base["art_fs"],
			"art_mp":      base["art_mp"],
			"art_fp":      base["art_fp"],
			"n_ms":        getOrFallback(tData, base, "n_ms"),
			"n_fs":        getOrFallback(tData, base, "n_fs"),
			"n_mp":        getOrFallback(tData, base, "n_mp"),
			"n_fp":        getOrFallback(tData, base, "n_fp"),
			"adj_ms":      getOrFallback(tData, base, "adj_ms"),
			"adj_fs":      getOrFallback(tData, base, "adj_fs"),
			"adj_mp":      getOrFallback(tData, base, "adj_mp"),
			"adj_fp":      getOrFallback(tData, base, "adj_fp"),
			"v_trans_s":   getOrFallback(tData, base, "v_trans_s"),
			"v_trans_p":   getOrFallback(tData, base, "v_trans_p"),
			"v_intrans_s": getOrFallback(tData, base, "v_intrans_s"),
			"v_intrans_p": getOrFallback(tData, base, "v_intrans_p"),
			"prep":        base["prep"],
			"conj":        base["conj"],
			"intro":       getOrFallback(tData, base, "intro"),
			"circ":        getOrFallback(tData, base, "circ"),
		}
		engine = NewCFGEngine(romanceGrammar, lexicon)
	}

	if outputType == "sentences" {
		out := make([]string, count)
		for i := 0; i < count; i++ {
			out[i] = engine.GenerateSentence(lang, grammarCorrect, orthographyCorrect)
		}
		return out, nil
	}

	paragraphs := make([]string, count)
	for i := 0; i < count; i++ {
		numSentences := 3 + rand.IntN(3) // [3, 5]
		sents := make([]string, numSentences)
		for j := 0; j < numSentences; j++ {
			sents[j] = engine.GenerateSentence(lang, grammarCorrect, orthographyCorrect)
		}
		paragraphs[i] = strings.Join(sents, " ")
	}
	return paragraphs, nil
}
