from typing import List, Dict
from csv import DictReader


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    with open(path, "r") as file:
        file_reader = DictReader(file, delimiter=",")
        industries = set()
        for row in file_reader:
            if len(row["industry"]) > 0:
                industries.add(row["industry"])
        return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError


# get_unique_industries("./data/jobs.csv")  # DEBUG
