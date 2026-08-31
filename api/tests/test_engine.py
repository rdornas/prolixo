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
