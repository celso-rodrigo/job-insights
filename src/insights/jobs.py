from functools import lru_cache
from typing import List, Dict
from csv import DictReader


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, "r") as file:
        file_reader = DictReader(file, delimiter=",")
        file_dict = []
        for row in file_reader:
            file_dict.append(row)
        return file_dict


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    with open(path, "r") as file:
        file_reader = DictReader(file, delimiter=",")
        job_types = set()
        for row in file_reader:
            job_types.add(row["job_type"])
        return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError


# get_unique_job_types("./data/jobs.csv")  # DEBUG
