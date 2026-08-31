from app.generator.noise import inject_spelling_noise, inject_grammar_noise

def test_inject_spelling_noise_pt():
    sentence = "Com certeza a exceção de repente foi analisada de forma estratégica."
    noisy = inject_spelling_noise(sentence, "pt")
    assert isinstance(noisy, str)
    assert len(noisy) > 0

def test_inject_spelling_noise_en():
    sentence = "Definitely separate the throughput and accommodate development."
    noisy = inject_spelling_noise(sentence, "en")
    assert isinstance(noisy, str)
    assert len(noisy) > 0

def test_inject_spelling_noise_es():
    sentence = "A ver si el análisis de la decisión es necesario."
    noisy = inject_spelling_noise(sentence, "es")
    assert isinstance(noisy, str)
    assert len(noisy) > 0

def test_inject_spelling_noise_fr():
    sentence = "Le développement de cet événement est intéressant."
    noisy = inject_spelling_noise(sentence, "fr")
    assert isinstance(noisy, str)
    assert len(noisy) > 0

def test_inject_spelling_noise_unknown_lang():
    sentence = "Lorem ipsum dolor sit amet."
    assert inject_spelling_noise(sentence, "la") == sentence

def test_inject_grammar_noise_short_sentence():
    short = "A b c"
    assert inject_grammar_noise(short, "en") == short

def test_inject_grammar_noise_languages():
    for lang in ["pt", "en", "es", "fr"]:
        sentence = "The advanced system optimizes complex workflow integration seamlessly."
        noisy = inject_grammar_noise(sentence, lang)
        assert isinstance(noisy, str)
        assert len(noisy.split()) >= len(sentence.split()) - 1
