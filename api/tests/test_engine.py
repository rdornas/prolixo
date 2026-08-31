import pytest
from app.generator.engine import (
    ShuffledDeck,
    CFGEngine,
    MarkovEngine,
    get_stem,
    extract_content_words,
    generate_content,
    romance_grammar,
    english_grammar,
)
from app.generator.dicts import pt, en, es, fr, la

def test_shuffled_deck_basic():
    items = ["alpha", "beta", "gamma"]
    deck = ShuffledDeck(items)
    drawn = [deck.draw() for _ in range(6)]
    assert len(drawn) == 6
    assert set(drawn) == {"alpha", "beta", "gamma"}

def test_get_stem():
    assert get_stem("computadores", "pt") == "computador"
    assert get_stem("sistemas", "pt") == "sistem"
    assert get_stem("running", "en") == "runn"
    assert get_stem("acciones", "es") == "accion"
    assert get_stem("développement", "fr") == "developp"
    assert get_stem("omnibus", "la") == "omn"

def test_extract_content_words():
    for lang in ["pt", "en", "es", "fr", "la"]:
        words = extract_content_words(lang, "business")
        assert isinstance(words, list)
        assert len(words) > 0
        assert len(words) == len(set(words))

def test_cfg_engine_sentence_generation():
    lexicon = {
        "art_s": ["the"],
        "art_p": ["the"],
        "n_s": ["system"],
        "n_p": ["systems"],
        "adj": ["scalable"],
        "v_trans_s": ["enhances"],
        "v_trans_p": ["enhance"],
        "v_intrans_s": ["works"],
        "v_intrans_p": ["work"],
        "prep": ["with"],
        "conj": ["and"],
        "intro": ["In fact,"],
        "circ": ["globally"],
    }
    engine = CFGEngine(english_grammar, lexicon)
    sentence = engine.generate_sentence(lang="en")
    assert isinstance(sentence, str)
    assert len(sentence) > 0
    assert sentence[0].isupper()

def test_markov_engine_latin():
    engine = MarkovEngine(la.sentences, order=2)
    sentence = engine.generate_sentence()
    assert isinstance(sentence, str)
    assert len(sentence) > 0
    assert sentence[0].isupper()
    assert sentence.endswith((".", "?", "!"))

def test_generate_content_words():
    for lang in ["pt", "en", "es", "fr", "la"]:
        result = generate_content(lang=lang, output_type="words", count=15, theme="technology")
        assert len(result) == 1
        words = result[0].split()
        assert len(words) == 15

def test_generate_content_sentences():
    for lang in ["pt", "en", "es", "fr", "la"]:
        result = generate_content(lang=lang, output_type="sentences", count=3, theme="business")
        assert len(result) == 3
        for s in result:
            assert len(s) > 0
            assert s[0].isupper()

def test_generate_content_paragraphs():
    for lang in ["pt", "en", "es", "fr", "la"]:
        result = generate_content(lang=lang, output_type="paragraphs", count=2, theme="ecology")
        assert len(result) == 2
        for p in result:
            assert len(p.split()) > 5

def test_generate_content_all_themes():
    themes = ["business", "ecology", "law", "medicine", "mining", "politics", "technology"]
    for theme in themes:
        result = generate_content(lang="pt", output_type="sentences", count=1, theme=theme)
        assert len(result) == 1
        assert len(result[0]) > 0

def test_generate_content_invalid_type_or_lang():
    with pytest.raises(ValueError):
        generate_content(lang="invalid_lang", output_type="words", count=5)
    with pytest.raises(ValueError):
        generate_content(lang="en", output_type="invalid_type", count=5)

def test_portuguese_demonstrative_preposition_contractions():
    grammar = {
        "S": [["TEST_DE_ESTES."], ["TEST_EM_ESTE."], ["TEST_DE_AQUELE."]],
        "TEST_DE_ESTES": [["prep_de", "art_estes", "noun"]],
        "TEST_EM_ESTE": [["prep_em", "art_este", "noun"]],
        "TEST_DE_AQUELE": [["prep_de", "art_aquele", "noun"]],
    }
    lexicon = {
        "prep_de": ["de"],
        "prep_em": ["em"],
        "art_estes": ["estes"],
        "art_este": ["este"],
        "art_aquele": ["aquele"],
        "noun": ["projetos"],
    }
    engine = CFGEngine(grammar, lexicon)
    
    # Test individual rules via generate_sentence
    s1 = engine.generate_sentence(lang="pt", grammar_correct=True)
    assert "de estes" not in s1.lower()
    assert "em este" not in s1.lower()
    assert "de aquele" not in s1.lower()
    assert any(c in s1.lower() for c in ["destes projetos", "neste projetos", "daquele projetos"])

def test_portuguese_mining_no_uncontracted_prepositions():
    import re
    # Run multiple Portuguese sentences across themes to guarantee no uncontracted prepositions
    for _ in range(50):
        sentences = generate_content(lang="pt", output_type="sentences", count=5, theme="mining", grammar_correct=True)
        for s in sentences:
            s_lower = s.lower()
            assert not re.search(r'\bde este\b', s_lower)
            assert not re.search(r'\bde estes\b', s_lower)
            assert not re.search(r'\bde esta\b', s_lower)
            assert not re.search(r'\bde estas\b', s_lower)
            assert not re.search(r'\bem este\b', s_lower)
            assert not re.search(r'\bem estes\b', s_lower)
            assert not re.search(r'\bem esta\b', s_lower)
            assert not re.search(r'\bem estas\b', s_lower)
            assert not re.search(r'\bde aquele\b', s_lower)
            assert not re.search(r'\bde o\b', s_lower)
            assert not re.search(r'\bde a\b', s_lower)
            assert not re.search(r'\bde os\b', s_lower)
            assert not re.search(r'\bde as\b', s_lower)

def test_spanish_and_french_contractions():
    import re
    grammar_es = {"S": [["prep", "art_ms", "noun."]]}
    lexicon_es = {"prep": ["de", "a"], "art_ms": ["el"], "noun": ["modelo"]}
    engine_es = CFGEngine(grammar_es, lexicon_es)
    s_es = engine_es.generate_sentence(lang="es", grammar_correct=True)
    assert not re.search(r'\bde el\b', s_es.lower())
    assert not re.search(r'\ba el\b', s_es.lower())
    assert "del modelo." in s_es.lower() or "al modelo." in s_es.lower()

    grammar_fr = {"S": [["prep", "art_ms", "noun."]]}
    lexicon_fr = {"prep": ["de", "à"], "art_ms": ["le"], "noun": ["modèle"]}
    engine_fr = CFGEngine(grammar_fr, lexicon_fr)
    s_fr = engine_fr.generate_sentence(lang="fr", grammar_correct=True)
    assert not re.search(r'\bde le\b', s_fr.lower())
    assert not re.search(r'\bà le\b', s_fr.lower())
    assert "du modèle." in s_fr.lower() or "au modèle." in s_fr.lower()



