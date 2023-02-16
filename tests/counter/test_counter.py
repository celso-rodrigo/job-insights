from src.pre_built.counter import count_ocurrences
from pytest import raises


def test_counter():
    assert count_ocurrences("data/jobs.csv", 'JaVaScRiPt') == 122
    assert count_ocurrences("data/jobs.csv", 'python') == 1639
    assert count_ocurrences("data/jobs.csv", 'invalid_word') == 0

    with raises(FileNotFoundError):
        assert count_ocurrences("invalid_path", '')

    with raises(TypeError):
        assert count_ocurrences()

    with raises(AttributeError):
        assert count_ocurrences("data/jobs.csv", True)
