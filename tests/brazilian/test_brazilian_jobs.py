from src.pre_built.brazilian_jobs import read_brazilian_file
from pytest import raises


def test_brazilian_jobs():
    assert len(read_brazilian_file("tests/mocks/brazilians_jobs.csv")) == 15

    assert read_brazilian_file("tests/mocks/brazilians_jobs.csv")[0] == {
        "salary": "2000",
        "title": "Maquinista",
        "type": "trainee",
    }

    with raises(FileNotFoundError):
        assert read_brazilian_file("invalid_path")

    with raises(TypeError):
        assert read_brazilian_file()