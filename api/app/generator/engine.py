import random
import re
from app.generator.dicts import pt, en, es, fr, la
from app.generator.dicts.themes import THEME_DICTS
from app.generator.noise import inject_grammar_noise, inject_spelling_noise

class ShuffledDeck:
    """
    Manages random string draws without immediate replacement.
    Shuffles a copy of the items list and draws sequentially.
    When the deck is exhausted, it automatically resets and reshuffles.
    """
    def __init__(self, items: list[str]):
        self.items = items
        self.deck = []
        self.reset()

    def reset(self):
        self.deck = list(self.items)
        random.shuffle(self.deck)

    def draw(self) -> str:
        if not self.deck:
            self.reset()
        return self.deck.pop()


class CFGEngine:
    """
    Context-Free Grammar (CFG) text generation engine.
    Uses ShuffledDecks for terminal symbols to avoid proximate lexical repetitions.
    """
    def __init__(self, grammar: dict, lexicon: dict):
        self.grammar = grammar
        self.decks = {key: ShuffledDeck(values) for key, values in lexicon.items()}

    def expand(self, symbol: str) -> str:
        # Extract attached punctuation (e.g., "S_BODY.", "circ,")
        has_punctuation = False
        punctuation = ""
        clean_symbol = symbol
        if symbol.endswith(".") or symbol.endswith(","):
            has_punctuation = True
            punctuation = symbol[-1]
            clean_symbol = symbol[:-1]

        if clean_symbol in self.grammar:
            # Non-terminal rule: randomly select a production
            production = random.choice(self.grammar[clean_symbol])
            expanded = [self.expand(sym) for sym in production]
            result = " ".join([e for e in expanded if e])
        elif clean_symbol in self.decks:
            # Lexical terminal: draw from shuffled deck
            result = self.decks[clean_symbol].draw()
        else:
            # Literal string
            result = clean_symbol

        # Reconnect punctuation if needed
        if has_punctuation:
            return result.rstrip() + punctuation
        return result

    def generate_sentence(
        self,
        lang: str = "en",
        grammar_correct: bool = True,
        orthography_correct: bool = True
    ) -> str:
        # Expand from root symbol "S"
        text = self.expand("S")
        # Post-processing spaces and punctuation
        text = re.sub(r'\s+([.,])', r'\1', text)
        text = re.sub(r'\s+', ' ', text).strip()

        if grammar_correct:
            # Collapse consecutive duplicate words (e.g. "a a" -> "a", "de de" -> "de")
            text = re.sub(r'\b([A-Za-zÀ-ÿ]+)(?:\s+\1\b)+', r'\1', text, flags=re.IGNORECASE)

            # Contract Romance preposition collisions if present
            if lang == "pt":
                # Preposition 'de'
                text = re.sub(r'\bde o\b', 'do', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde a\b', 'da', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde os\b', 'dos', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde as\b', 'das', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde este\b', 'deste', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde esta\b', 'desta', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde estes\b', 'destes', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde estas\b', 'destas', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde isto\b', 'disto', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde esse\b', 'desse', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde essa\b', 'dessa', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde esses\b', 'desses', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde essas\b', 'dessas', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde isso\b', 'disso', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde aquele\b', 'daquele', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde aquela\b', 'daquela', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde aqueles\b', 'daqueles', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde aquelas\b', 'daquelas', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde aquilo\b', 'daquilo', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde ele\b', 'dele', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde ela\b', 'dela', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde eles\b', 'deles', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde elas\b', 'delas', text, flags=re.IGNORECASE)

                # Preposition 'em'
                text = re.sub(r'\bem o\b', 'no', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem a\b', 'na', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem os\b', 'nos', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem as\b', 'nas', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem este\b', 'neste', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem esta\b', 'nesta', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem estes\b', 'nestes', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem estas\b', 'nestas', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem isto\b', 'nisto', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem esse\b', 'nesse', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem essa\b', 'nessa', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem esses\b', 'nesses', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem essas\b', 'nessas', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem isso\b', 'nisso', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem aquele\b', 'naquele', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem aquela\b', 'naquela', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem aqueles\b', 'naqueles', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem aquelas\b', 'naquelas', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem aquilo\b', 'naquilo', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem ele\b', 'nele', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem ela\b', 'nela', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem eles\b', 'neles', text, flags=re.IGNORECASE)
                text = re.sub(r'\bem elas\b', 'nelas', text, flags=re.IGNORECASE)

                # Preposition 'a'
                text = re.sub(r'\ba a\b', 'à', text, flags=re.IGNORECASE)
                text = re.sub(r'\ba as\b', 'às', text, flags=re.IGNORECASE)
                text = re.sub(r'\ba o\b', 'ao', text, flags=re.IGNORECASE)
                text = re.sub(r'\ba os\b', 'aos', text, flags=re.IGNORECASE)
                text = re.sub(r'\ba aquele\b', 'àquele', text, flags=re.IGNORECASE)
                text = re.sub(r'\ba aquela\b', 'àquela', text, flags=re.IGNORECASE)
                text = re.sub(r'\ba aqueles\b', 'àqueles', text, flags=re.IGNORECASE)
                text = re.sub(r'\ba aquelas\b', 'àquelas', text, flags=re.IGNORECASE)
                text = re.sub(r'\ba aquilo\b', 'àquilo', text, flags=re.IGNORECASE)

                # Preposition 'por'
                text = re.sub(r'\bpor o\b', 'pelo', text, flags=re.IGNORECASE)
                text = re.sub(r'\bpor a\b', 'pela', text, flags=re.IGNORECASE)
                text = re.sub(r'\bpor os\b', 'pelos', text, flags=re.IGNORECASE)
                text = re.sub(r'\bpor as\b', 'pelas', text, flags=re.IGNORECASE)

            elif lang == "es":
                text = re.sub(r'\bde el\b', 'del', text, flags=re.IGNORECASE)
                text = re.sub(r'\ba el\b', 'al', text, flags=re.IGNORECASE)

            elif lang == "fr":
                text = re.sub(r'\bde le\b', 'du', text, flags=re.IGNORECASE)
                text = re.sub(r'\bde les\b', 'des', text, flags=re.IGNORECASE)
                text = re.sub(r'\bà le\b', 'au', text, flags=re.IGNORECASE)
                text = re.sub(r'\bà les\b', 'aux', text, flags=re.IGNORECASE)
        else:
            text = inject_grammar_noise(text, lang)

        if not orthography_correct:
            text = inject_spelling_noise(text, lang)

        # Capitalize first character
        text = text.strip()
        if text:
            text = text[0].upper() + text[1:]
        return text


class MarkovEngine:
    """
    Markov Chain (Order 2) text generation engine.
    Trained on classical corpus sentences to generate natural variations.
    """
    def __init__(self, sentences: list[str], order: int = 2):
        self.order = order
        self.transitions = {}
        self.start_states = []
        
        for sentence in sentences:
            words = sentence.split()
            if len(words) <= order:
                continue
            self.start_states.append(tuple(words[:order]))
            
            for i in range(len(words) - order):
                state = tuple(words[i:i+order])
                next_word = words[i+order]
                if state not in self.transitions:
                    self.transitions[state] = []
                self.transitions[state].append(next_word)

    def generate_sentence(self) -> str:
        if not self.transitions or not self.start_states:
            return "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        
        state = random.choice(self.start_states)
        words = list(state)
        
        max_words = random.randint(8, 16)
        for _ in range(max_words - self.order):
            if state in self.transitions:
                next_word = random.choice(self.transitions[state])
                words.append(next_word)
                state = tuple(words[-self.order:])
                if next_word.endswith((".", "?", "!")):
                    break
            else:
                break
                
        sentence = " ".join(words)
        sentence = sentence[0].upper() + sentence[1:]
        if not sentence.endswith((".", "?", "!")):
            sentence += "."
        return sentence


# Definition of Structural Grammars (CFGs)
romance_grammar = {
    "S": [
        ["INTRO", "S_BODY."],
        ["CIRC_INTRO", "S_BODY."],
        ["S_BODY."]
    ],
    "INTRO": [["intro"]],
    "CIRC_INTRO": [["circ,"]],
    "S_BODY": [
        ["NP_s", "VP_s"],
        ["NP_p", "VP_p"],
        ["NP_s", "VP_s", "CONJ", "NP_s", "VP_s"],
        ["NP_p", "VP_p", "CONJ", "NP_p", "VP_p"]
    ],
    "CONJ": [["conj"]],
    "NP_s": [["NP_ms"], ["NP_fs"]],
    "NP_p": [["NP_mp"], ["NP_fp"]],
    "NP_ms": [["art_ms", "n_ms"], ["art_ms", "n_ms", "adj_ms"], ["n_ms", "PP_s"]],
    "NP_fs": [["art_fs", "n_fs"], ["art_fs", "n_fs", "adj_fs"], ["n_fs", "PP_s"]],
    "NP_mp": [["art_mp", "n_mp"], ["art_mp", "n_mp", "adj_mp"], ["n_mp", "PP_p"]],
    "NP_fp": [["art_fp", "n_fp"], ["art_fp", "n_fp", "adj_fp"], ["n_fp", "PP_p"]],
    "VP_s": [["v_trans_s", "NP_s"], ["v_trans_s", "NP_p"], ["v_intrans_s"]],
    "VP_p": [["v_trans_p", "NP_s"], ["v_trans_p", "NP_p"], ["v_intrans_p"]],
    "PP_s": [["prep", "NP_ms"], ["prep", "NP_fs"]],
    "PP_p": [["prep", "NP_mp"], ["prep", "NP_fp"]]
}

english_grammar = {
    "S": [
        ["INTRO", "S_BODY."],
        ["CIRC_INTRO", "S_BODY."],
        ["S_BODY."]
    ],
    "INTRO": [["intro"]],
    "CIRC_INTRO": [["circ,"]],
    "S_BODY": [
        ["NP_s", "VP_s"],
        ["NP_p", "VP_p"],
        ["NP_s", "VP_s", "CONJ", "NP_s", "VP_s"],
        ["NP_p", "VP_p", "CONJ", "NP_p", "VP_p"]
    ],
    "CONJ": [["conj"]],
    "NP_s": [["art_s", "n_s"], ["art_s", "adj", "n_s"], ["n_s", "PP"]],
    "NP_p": [["art_p", "n_p"], ["art_p", "adj", "n_p"], ["n_p", "PP"]],
    "VP_s": [["v_trans_s", "NP_s"], ["v_trans_s", "NP_p"], ["v_intrans_s"]],
    "VP_p": [["v_trans_p", "NP_s"], ["v_trans_p", "NP_p"], ["v_intrans_p"]],
    "PP": [["prep", "NP_s"], ["prep", "NP_p"]]
}


STOP_WORDS = {
    "pt": {
        "o", "a", "os", "as", "um", "uma", "uns", "umas", "de", "do", "da", "dos", "das",
        "em", "no", "na", "nos", "nas", "para", "por", "com", "sob", "sobre", "ante",
        "até", "após", "contra", "desde", "entre", "perante", "sem", "e", "ou", "mas",
        "que", "se", "ao", "aos", "à", "às", "pelo", "pela", "pelos", "pelas", "este",
        "esta", "estes", "estas", "qualquer", "determinado", "determinada", "certos", "certas",
        "diversos", "diversas", "respectivo", "respectiva"
    },
    "en": {
        "a", "an", "the", "this", "that", "these", "those", "any", "each", "some", "several",
        "various", "of", "for", "in", "on", "at", "to", "from", "with", "by", "about", "against",
        "between", "into", "through", "during", "before", "after", "above", "below", "and",
        "but", "if", "or", "because", "as", "until", "while", "which", "who", "whom", "respective"
    },
    "es": {
        "el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al", "en", "para",
        "por", "con", "sin", "sobre", "entre", "hacia", "hasta", "durante", "mediante", "y",
        "o", "pero", "que", "si", "como", "este", "esta", "estos", "estas", "cualquier",
        "determinado", "determinada", "ciertos", "ciertas", "diversos", "diversas", "respectivo", "respectiva"
    },
    "fr": {
        "de", "la", "le", "les", "un", "une", "des", "du", "au", "aux", "en", "pour", "par", "sur",
        "dans", "avec", "sans", "sous", "et", "ou", "mais", "que", "qui", "comme", "ce", "cette",
        "ces", "tout", "toute", "tous", "toutes", "certains", "certaines", "plusieurs", "respectif", "respective"
    },
    "la": {
        "et", "in", "ad", "ac", "ut", "ex", "a", "ab", "is", "ea", "id", "sed", "si", "cum", "per", "non", "nec"
    }
}


def extract_content_words(lang: str, theme: str = "technology") -> list[str]:
    import re
    raw_sources = []
    
    if lang in THEME_DICTS and theme in THEME_DICTS[lang]:
        theme_data = THEME_DICTS[lang][theme]
        if isinstance(theme_data, list):
            raw_sources.extend(theme_data)
        elif isinstance(theme_data, dict):
            for k, v in theme_data.items():
                if isinstance(v, list):
                    raw_sources.extend(v)
    else:
        if lang == "pt":
            lists = [pt.n_ms, pt.n_fs, pt.n_mp, pt.n_fp, pt.adj_ms, pt.adj_fs, pt.adj_mp, pt.adj_fp, pt.v_trans_s, pt.v_trans_p, pt.v_intrans_s, pt.v_intrans_p]
            for l in lists: raw_sources.extend(l)
        elif lang == "es":
            lists = [es.n_ms, es.n_fs, es.n_mp, es.n_fp, es.adj_ms, es.adj_fs, es.adj_mp, es.adj_fp, es.v_trans_s, es.v_trans_p, es.v_intrans_s, es.v_intrans_p]
            for l in lists: raw_sources.extend(l)
        elif lang == "fr":
            lists = [fr.n_ms, fr.n_fs, fr.n_mp, fr.n_fp, fr.adj_ms, fr.adj_fs, fr.adj_mp, fr.adj_fp, fr.v_trans_s, fr.v_trans_p, fr.v_intrans_s, fr.v_intrans_p]
            for l in lists: raw_sources.extend(l)
        elif lang == "en":
            lists = [en.n_s, en.n_p, en.adj, en.v_trans_s, en.v_trans_p, en.v_intrans_s, en.v_intrans_p]
            for l in lists: raw_sources.extend(l)
        elif lang == "la":
            raw_sources.extend(la.sentences)

    stop_words = STOP_WORDS.get(lang, set())
    words = []
    for text in raw_sources:
        tokens = text.split()
        for token in tokens:
            clean_token = re.sub(r'[^\w\-]', '', token, flags=re.UNICODE).lower().strip()
            if clean_token and len(clean_token) > 2 and clean_token not in stop_words:
                words.append(clean_token)
    
    return list(dict.fromkeys(words))


def get_stem(word: str, lang: str) -> str:
    import unicodedata, re
    w = word.lower().strip()
    w_no_acc = unicodedata.normalize('NFD', w).encode('ascii', 'ignore').decode('utf-8')
    
    if lang in ['pt', 'es']:
        w_no_acc = re.sub(r'(oes|ao|on)$', '', w_no_acc)
        w_no_acc = re.sub(r'(ando|endo|indo|aram|eram|iram|avam|evam|ivam|am|em|ou|ar|er|ir)$', '', w_no_acc)
        w_no_acc = re.sub(r'(ico|ica|icos|icas|ia|ias)$', '', w_no_acc)
        w_no_acc = re.sub(r'(es|os|as|is|s)$', '', w_no_acc)
        w_no_acc = re.sub(r'(o|a|e)$', '', w_no_acc)
    elif lang == 'fr':
        w_no_acc = re.sub(r'(ement|ment|issant|ant|ent|er|ir|re|ait|aient|ont|eaux|aux|es|e|s)$', '', w_no_acc)
        w_no_acc = re.sub(r'(ique|iques|isme|ismes|iste|istes|tion|tions)$', '', w_no_acc)
    elif lang == 'en':
        w_no_acc = re.sub(r'(ing|edly|ed|es|s|ly|ic|ical)$', '', w_no_acc)
    elif lang == 'la':
        w_no_acc = re.sub(r'(orum|arum|ibus|um|am|em|os|as|es|is|us|a|e|o)$', '', w_no_acc)
        
    return w_no_acc


def generate_content(
    lang: str,
    output_type: str,
    count: int,
    theme: str = "business",
    grammar_correct: bool = True,
    orthography_correct: bool = True
) -> list[str]:
    """
    Generates words, sentences, or paragraphs with stem deduplication and thematic vocabulary.
    Supports clean mode (grammar_correct=True, orthography_correct=True) or noisy mode.
    """
    if lang not in {"pt", "en", "es", "fr", "la"}:
        raise ValueError(f"Unsupported language: {lang}")

    if output_type not in {"words", "sentences", "paragraphs"}:
        raise ValueError(f"Invalid output type: {output_type}")

    # Latin is strictly classical Lorem Ipsum without themes or noise injection
    if lang == "la":
        if output_type == "words":
            content_words = extract_content_words("la", "business")
            deck = ShuffledDeck(content_words)
            drawn = []
            while len(drawn) < count:
                drawn.append(deck.draw())
            return [" ".join(drawn)]

        engine = MarkovEngine(la.sentences)
        if output_type == "sentences":
            return [engine.generate_sentence() for _ in range(count)]
        elif output_type == "paragraphs":
            paragraphs = []
            for _ in range(count):
                num_sentences = random.randint(3, 5)
                sentences = [engine.generate_sentence() for _ in range(num_sentences)]
                paragraphs.append(" ".join(sentences))
            return paragraphs
        else:
            raise ValueError(f"Invalid output type: {output_type}")

    # 1. Output format: 'words'
    if output_type == "words":
        content_words = extract_content_words(lang, theme)
        deck = ShuffledDeck(content_words)
        drawn = []
        used_stems = set()
        max_attempts = len(content_words) * 4
        attempts = 0
        while len(drawn) < count and attempts < max_attempts:
            attempts += 1
            w = deck.draw()
            stem = get_stem(w, lang)
            if stem not in used_stems:
                used_stems.add(stem)
                drawn.append(w)
        while len(drawn) < count:
            drawn.append(deck.draw())
        return [" ".join(drawn)]

    # 2. Engine setup for sentences and paragraphs
    if lang in THEME_DICTS and theme in THEME_DICTS[lang]:
        t_data = THEME_DICTS[lang][theme]
        if lang in ["pt", "es", "fr"]:
            base_module = pt if lang == "pt" else es if lang == "es" else fr
            lexicon = {
                "art_ms": base_module.art_ms, "art_fs": base_module.art_fs,
                "art_mp": base_module.art_mp, "art_fp": base_module.art_fp,
                "n_ms": t_data.get("n_ms", base_module.n_ms),
                "n_fs": t_data.get("n_fs", base_module.n_fs),
                "n_mp": t_data.get("n_mp", base_module.n_mp),
                "n_fp": t_data.get("n_fp", base_module.n_fp),
                "adj_ms": t_data.get("adj_ms", base_module.adj_ms),
                "adj_fs": t_data.get("adj_fs", base_module.adj_fs),
                "adj_mp": t_data.get("adj_mp", base_module.adj_mp),
                "adj_fp": t_data.get("adj_fp", base_module.adj_fp),
                "v_trans_s": t_data.get("v_trans_s", base_module.v_trans_s),
                "v_trans_p": t_data.get("v_trans_p", base_module.v_trans_p),
                "v_intrans_s": t_data.get("v_intrans_s", base_module.v_intrans_s),
                "v_intrans_p": t_data.get("v_intrans_p", base_module.v_intrans_p),
                "prep": base_module.prep, "conj": base_module.conj,
                "intro": t_data.get("intro", base_module.intro),
                "circ": t_data.get("circ", base_module.circ)
            }
            engine = CFGEngine(romance_grammar, lexicon)

        elif lang == "en":
            lexicon = {
                "art_s": en.art_s, "art_p": en.art_p,
                "n_s": t_data.get("n_s", en.n_s),
                "n_p": t_data.get("n_p", en.n_p),
                "adj": t_data.get("adj", en.adj),
                "v_trans_s": t_data.get("v_trans_s", en.v_trans_s),
                "v_trans_p": t_data.get("v_trans_p", en.v_trans_p),
                "v_intrans_s": t_data.get("v_intrans_s", en.v_intrans_s),
                "v_intrans_p": t_data.get("v_intrans_p", en.v_intrans_p),
                "prep": en.prep, "conj": en.conj,
                "intro": t_data.get("intro", en.intro),
                "circ": t_data.get("circ", en.circ)
            }
            engine = CFGEngine(english_grammar, lexicon)

    else:
        # Fallback to base dictionaries if needed
        if lang == "pt":
            lexicon = {
                "art_ms": pt.art_ms, "art_fs": pt.art_fs, "art_mp": pt.art_mp, "art_fp": pt.art_fp,
                "n_ms": pt.n_ms, "n_fs": pt.n_fs, "n_mp": pt.n_mp, "n_fp": pt.n_fp,
                "adj_ms": pt.adj_ms, "adj_fs": pt.adj_fs, "adj_mp": pt.adj_mp, "adj_fp": pt.adj_fp,
                "v_trans_s": pt.v_trans_s, "v_trans_p": pt.v_trans_p,
                "v_intrans_s": pt.v_intrans_s, "v_intrans_p": pt.v_intrans_p,
                "prep": pt.prep, "conj": pt.conj, "intro": pt.intro, "circ": pt.circ
            }
            engine = CFGEngine(romance_grammar, lexicon)

        elif lang == "es":
            lexicon = {
                "art_ms": es.art_ms, "art_fs": es.art_fs, "art_mp": es.art_mp, "art_fp": es.art_fp,
                "n_ms": es.n_ms, "n_fs": es.n_fs, "n_mp": es.n_mp, "n_fp": es.n_fp,
                "adj_ms": es.adj_ms, "adj_fs": es.adj_fs, "adj_mp": es.adj_mp, "adj_fp": es.adj_fp,
                "v_trans_s": es.v_trans_s, "v_trans_p": es.v_trans_p,
                "v_intrans_s": es.v_intrans_s, "v_intrans_p": es.v_intrans_p,
                "prep": es.prep, "conj": es.conj, "intro": es.intro, "circ": es.circ
            }
            engine = CFGEngine(romance_grammar, lexicon)

        elif lang == "fr":
            lexicon = {
                "art_ms": fr.art_ms, "art_fs": fr.art_fs, "art_mp": fr.art_mp, "art_fp": fr.art_fp,
                "n_ms": fr.n_ms, "n_fs": fr.n_fs, "n_mp": fr.n_mp, "n_fp": fr.n_fp,
                "adj_ms": fr.adj_ms, "adj_fs": fr.adj_fs, "adj_mp": fr.adj_mp, "adj_fp": fr.adj_fp,
                "v_trans_s": fr.v_trans_s, "v_trans_p": fr.v_trans_p,
                "v_intrans_s": fr.v_intrans_s, "v_intrans_p": fr.v_intrans_p,
                "prep": fr.prep, "conj": fr.conj, "intro": fr.intro, "circ": fr.circ
            }
            engine = CFGEngine(romance_grammar, lexicon)

        elif lang == "en":
            lexicon = {
                "art_s": en.art_s, "art_p": en.art_p,
                "n_s": en.n_s, "n_p": en.n_p, "adj": en.adj,
                "v_trans_s": en.v_trans_s, "v_trans_p": en.v_trans_p,
                "v_intrans_s": en.v_intrans_s, "v_intrans_p": en.v_intrans_p,
                "prep": en.prep, "conj": en.conj, "intro": en.intro, "circ": en.circ
            }
            engine = CFGEngine(english_grammar, lexicon)

        else:
            raise ValueError(f"Unsupported language: {lang}")

    if output_type == "sentences":
        return [
            engine.generate_sentence(
                lang=lang,
                grammar_correct=grammar_correct,
                orthography_correct=orthography_correct
            )
            for _ in range(count)
        ]

    elif output_type == "paragraphs":
        paragraphs = []
        for _ in range(count):
            num_sentences = random.randint(3, 5)
            sentences = [
                engine.generate_sentence(
                    lang=lang,
                    grammar_correct=grammar_correct,
                    orthography_correct=orthography_correct
                )
                for _ in range(num_sentences)
            ]
            paragraphs.append(" ".join(sentences))
        return paragraphs

    else:
        raise ValueError(f"Invalid output type: {output_type}")
