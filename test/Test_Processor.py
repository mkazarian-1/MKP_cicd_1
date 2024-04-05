import pytest

from src.Processor import Processor

@pytest.fixture
def processor():
    return Processor()

@pytest.mark.parametrize(
    "text, delimiters, sentence_endings, expected_words, expected_sentences",
    [
        ("Hello, world! This is a test.", [",", " "], [".", "!"], 6, 2),
        ("One;Two:Three,Four", [",", " ", ":", ";"], [".", "!"], 4, 1),
        ("Testing. testing. testing?", [",", " "], [".", "!", "?"], 3, 3),
        ("", [",", " "], [".", "!"], 0, 0),
        ("This is a sentence.", [",", " "], [".", "!"], 4, 1),
    ]
)
def test_count_division(processor, text, delimiters, sentence_endings, expected_words, expected_sentences):
    words, sentences = processor.count_division(text, delimiters, sentence_endings)

    assert words == expected_words
    assert sentences == expected_sentences
