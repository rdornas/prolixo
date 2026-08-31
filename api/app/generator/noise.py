import random
import re

# Common LanguageTool-inspired spelling corruptions
SPELLING_REPLACEMENTS = {
    "pt": [
        (r"\bcom certeza\b", "concerteza"),
        (r"\bCom certeza\b", "Concerteza"),
        (r"\bexceção\b", "excessão"),
        (r"\bExceção\b", "Excessão"),
        (r"\bde repente\b", "derrepente"),
        (r"\bDe repente\b", "Derrepente"),
        (r"\ba partir de\b", "apartir de"),
        (r"\bA partir de\b", "Apartir de"),
        (r"\bem cima\b", "emcima"),
        (r"\bprivilégio\b", "previlégio"),
        (r"\breivindicar\b", "reinvindicar"),
        (r"\batravés\b", "atravez"),
        (r"\banálise\b", "analise"),
        (r"\bAnálise\b", "Analise"),
        (r"\bestratégico\b", "estrategico"),
        (r"\bestratégica\b", "estrategica"),
        (r"\bestratégicos\b", "estrategicos"),
        (r"\bestratégicas\b", "estrategicas"),
        (r"\beficiência\b", "eficiencia"),
        (r"\bdisrupção\b", "disrupçao"),
        (r"\bessencial\b", "ecencial"),
        (r"\bprocesso\b", "proceço"),
        (r"\bconsenso\b", "comcenso"),
        (r"\bnecessário\b", "necessario"),
        (r"\bnecessária\b", "necessaria"),
        (r"\binteligência\b", "inteligencia"),
        (r"\btecnológico\b", "tecnologico"),
        (r"\btecnológica\b", "tecnologica"),
    ],
    "en": [
        (r"\bdefinitely\b", "definately"),
        (r"\bDefinitely\b", "Definately"),
        (r"\bseparate\b", "seperate"),
        (r"\bSeparate\b", "Seperate"),
        (r"\breceive\b", "recieve"),
        (r"\bReceive\b", "Recieve"),
        (r"\blength\b", "lenght"),
        (r"\bLength\b", "Lenght"),
        (r"\bheight\b", "heigth"),
        (r"\bHeight\b", "Heigth"),
        (r"\bwidth\b", "widht"),
        (r"\bWidth\b", "Widht"),
        (r"\bdepth\b", "depht"),
        (r"\bDepth\b", "Depht"),
        (r"\bstrength\b", "strenght"),
        (r"\bStrength\b", "Strenght"),
        (r"\bweight\b", "weigth"),
        (r"\bWeight\b", "Weigth"),
        (r"\bstraight\b", "straigth"),
        (r"\bStraight\b", "Straigth"),
        (r"\bweird\b", "wierd"),
        (r"\bneighbor\b", "nieghbor"),
        (r"\bthroughput\b", "througput"),
        (r"\boccurrence\b", "occurance"),
        (r"\buntil\b", "untill"),
        (r"\bsuccessful\b", "succesful"),
        (r"\bnecessary\b", "neccessary"),
        (r"\benvironment\b", "enviroment"),
        (r"\bgovernment\b", "goverment"),
        (r"\bdevelopment\b", "developement"),
        (r"\baccommodate\b", "accomodate"),
        (r"\bmaintenance\b", "maintainance"),
        (r"\bcalendar\b", "calender"),
        (r"\bforeign\b", "foriegn"),
        (r"\btheir\b", "there"),
        (r"\bprinciple\b", "principal"),
    ],
    "es": [
        (r"\ba ver\b", "haber"),
        (r"\bA ver\b", "Haber"),
        (r"\bhecho\b", "echo"),
        (r"\btambién\b", "tambien"),
        (r"\bTambién\b", "Tambien"),
        (r"\banálisis\b", "analisis"),
        (r"\bAnálisis\b", "Analisis"),
        (r"\bdecisión\b", "decision"),
        (r"\bdesarrollo\b", "desarolo"),
        (r"\bexcepción\b", "escepción"),
        (r"\bnecesario\b", "necesário"),
        (r"\bhubiera\b", "hubiese sido"),
        (r"\beconómico\b", "economico"),
        (r"\beconómica\b", "economica"),
    ],
    "fr": [
        (r"\bdéveloppement\b", "dévelopement"),
        (r"\bévénement\b", "évènement"),
        (r"\bconnexion\b", "connection"),
        (r"\blangage\b", "language"),
        (r"\baccueil\b", "acceuil"),
        (r"\bintéressant\b", "interressant"),
        (r"\bchaque\b", "chaques"),
        (r"\bparmi\b", "parmis"),
        (r"\bmalgré\b", "malgrés"),
    ],
}


def inject_spelling_noise(sentence: str, lang: str) -> str:
    """
    Injects realistic spelling mistakes (misspellings, typo rules, missing accents).
    """
    if lang not in SPELLING_REPLACEMENTS:
        return sentence

    rules = SPELLING_REPLACEMENTS[lang]
    modified = sentence

    # Try applying 1 to 2 targeted replacements if present
    applied = 0
    shuffled_rules = list(rules)
    random.shuffle(shuffled_rules)

    for pattern, repl in shuffled_rules:
        if re.search(pattern, modified):
            modified = re.sub(pattern, repl, modified, count=1)
            applied += 1
            if applied >= 2:
                break

    # If no specific dictionary rule matched, apply a subtle vowel/letter substitution
    if applied == 0:
        words = modified.split()
        candidate_indices = [
            i for i, w in enumerate(words) if len(w) > 5 and w.isalpha()
        ]
        if candidate_indices:
            idx = random.choice(candidate_indices)
            w = words[idx]
            if lang == "en" and "ght" in w:
                words[idx] = w.replace("ght", "gth", 1)
            elif lang == "en" and "gth" in w:
                words[idx] = w.replace("gth", "ght", 1)
            elif lang == "en" and "ei" in w:
                words[idx] = w.replace("ei", "ie", 1)
            elif lang == "en" and "ie" in w:
                words[idx] = w.replace("ie", "ei", 1)
            elif "ss" in w:
                words[idx] = w.replace("ss", "s", 1)
            elif "ç" in w:
                words[idx] = w.replace("ç", "ss", 1)
            elif "é" in w:
                words[idx] = w.replace("é", "e", 1)
            elif "á" in w:
                words[idx] = w.replace("á", "a", 1)
            elif "ó" in w:
                words[idx] = w.replace("ó", "o", 1)
            elif "í" in w:
                words[idx] = w.replace("í", "i", 1)
            elif "ã" in w:
                words[idx] = w.replace("ã", "an", 1)
            elif len(w) > 4:
                pos = random.randint(1, len(w) - 3)
                words[idx] = w[:pos] + w[pos + 1] + w[pos] + w[pos + 2 :]
            modified = " ".join(words)

    return modified


def inject_grammar_noise(sentence: str, lang: str) -> str:
    """
    Injects grammatical discrepancies: consecutive duplicated tokens ("a a", "que que"),
    number disagreement ("os modelo"), verb agreement errors, or stylistic redundancies ("Para além disso").
    """
    if lang == "pt" and re.search(r'\balém disso\b', sentence, flags=re.IGNORECASE):
        if re.search(r'\bAlém disso\b', sentence):
            return re.sub(r'\bAlém disso\b', 'Para além disso', sentence, count=1)
        return re.sub(r'\balém disso\b', 'para além disso', sentence, count=1, flags=re.IGNORECASE)

    words = sentence.split()
    if len(words) < 4:
        return sentence

    noise_type = random.choice(["duplication", "disagreement", "gender_mismatch"])

    if noise_type == "duplication":
        dup_targets = {
            "pt": ["o", "a", "os", "as", "de", "em", "que", "para", "com", "no", "na"],
            "en": ["the", "a", "an", "of", "in", "to", "that", "for", "with", "and"],
            "es": ["el", "la", "los", "las", "de", "en", "que", "para", "con", "del"],
            "fr": ["le", "la", "les", "de", "en", "que", "pour", "avec", "du", "des"],
        }
        targets = dup_targets.get(lang, ["the", "de", "a"])
        candidate_indices = [
            i for i, w in enumerate(words) if w.lower().strip(".,;:!?") in targets
        ]

        if candidate_indices:
            idx = random.choice(candidate_indices)
            raw_word = words[idx]
            words.insert(idx, raw_word.lower().strip(".,;:!?"))
        else:
            idx = random.randint(1, min(4, len(words) - 1))
            words.insert(idx, words[idx].lower().strip(".,;:!?"))

    elif noise_type == "disagreement":
        if lang in ["pt", "es"]:
            for i, w in enumerate(words[:-1]):
                clean = w.lower()
                if clean in ["os", "as", "estes", "estas", "diversos", "diversas", "los", "las", "estos"]:
                    words[i] = "o" if clean in ["os", "estes", "los", "estos"] else "a"
                    break
                elif clean in ["o", "a", "este", "esta", "el", "la"]:
                    words[i] = "os" if clean in ["o", "este", "el"] else "as"
                    break
        elif lang == "en":
            for i, w in enumerate(words):
                if w.lower() in ["develops", "optimizes", "drives", "creates", "enables"]:
                    words[i] = w[:-1]
                    break
                elif w.lower() in ["develop", "optimize", "drive", "create", "enable"]:
                    words[i] = w + "s"
                    break

    elif noise_type == "gender_mismatch":
        if lang == "pt":
            for i, w in enumerate(words):
                if w.lower() == "o":
                    words[i] = "a"
                    break
                elif w.lower() == "a":
                    words[i] = "o"
                    break
                elif w.lower() == "um":
                    words[i] = "uma"
                    break
                elif w.lower() == "uma":
                    words[i] = "um"
                    break
        elif lang == "es":
            for i, w in enumerate(words):
                if w.lower() == "el":
                    words[i] = "la"
                    break
                elif w.lower() == "la":
                    words[i] = "el"
                    break
                elif w.lower() == "un":
                    words[i] = "una"
                    break
        elif lang == "fr":
            for i, w in enumerate(words):
                if w.lower() == "le":
                    words[i] = "la"
                    break
                elif w.lower() == "la":
                    words[i] = "le"
                    break

    return " ".join(words)
