from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def jobs():
    return [
        {
            "title": "Back end developer",
            "min_salary": 3000,
            "max_salary": 4000,
            "date_posted": "2022-04-12",
        },
        {
            "title": "Front end developer",
            "min_salary": 1000,
            "max_salary": 5000,
            "date_posted": "2022-08-12",
        },
        {
            "title": "Web developer",
            "min_salary": 500,
            "max_salary": 1500,
            "date_posted": "2022-09-12",
        },
        {
            "title": "Full stack developer",
            "min_salary": 4000,
            "max_salary": 8000,
            "date_posted": "2022-12-12",
        },
    ]


@pytest.fixture
def sorted_min_salary():
    return [
        {
            "title": "Web developer",
            "min_salary": 500,
            "max_salary": 1500,
            "date_posted": "2022-09-12",
        },
        {
            "title": "Front end developer",
            "min_salary": 1000,
            "max_salary": 5000,
            "date_posted": "2022-08-12",
        },
        {
            "title": "Back end developer",
            "min_salary": 3000,
            "max_salary": 4000,
            "date_posted": "2022-04-12",
        },
        {
            "title": "Full stack developer",
            "min_salary": 4000,
            "max_salary": 8000,
            "date_posted": "2022-12-12",
        },
    ]


@pytest.fixture
def sorted_by_date_posted():
    return [
        {
            "title": "Full stack developer",
            "min_salary": 4000,
            "max_salary": 8000,
            "date_posted": "2022-12-12",
        },
        {
            "title": "Web developer",
            "min_salary": 500,
            "max_salary": 1500,
            "date_posted": "2022-09-12",
        },
        {
            "title": "Front end developer",
            "min_salary": 1000,
            "max_salary": 5000,
            "date_posted": "2022-08-12",
        },
        {
            "title": "Back end developer",
            "min_salary": 3000,
            "max_salary": 4000,
            "date_posted": "2022-04-12",
        },
    ]


def test_sort_by_criteria(jobs, sorted_min_salary, sorted_by_date_posted):
    sort_by(jobs, criteria="min_salary")
    assert jobs == sorted_min_salary
    sort_by(jobs, "date_posted")
    assert jobs == sorted_by_date_posted

    with pytest.raises(TypeError):
        assert sort_by()

    with pytest.raises(AssertionError):
        assert sort_by([], "min_salary")

    with pytest.raises(ValueError):
        assert sort_by(jobs, "invalid_sort")
