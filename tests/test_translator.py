import pytest

from translator import translator, ismorse, islatin


def test_dummy():
    assert 2 + 2


def test_main_exception():
    sentence = '&^%$%^'

    with pytest.raises(ValueError) as exception:
        translator(sentence=sentence)

    assert sentence in str(exception.value)


def test_ismorse_valid():
    sentence = '-.-. .'

    result = ismorse(sentence=sentence)

    assert result is True


def test_ismorse_invalid():
    sentence = 'FOO BAR'

    result = ismorse(sentence=sentence)

    assert not result


def test_islatin_valid():
    sentence = 'FOO BAR'

    result = islatin(sentence=sentence)

    assert result is True


def test_islatin_invalid():
    sentence = '-.-. .'

    result = islatin(sentence=sentence)

    assert not result
