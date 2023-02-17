from typing import Union, List, Dict
from csv import DictReader


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    with open(path, "r") as file:
        file_reader = DictReader(file, delimiter=",")
        salaries = []
        for row in file_reader:
            if row["max_salary"].isnumeric():
                salaries.append(int(row["max_salary"]))
        return max(salaries)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    with open(path, "r") as file:
        file_reader = DictReader(file, delimiter=",")
        salaries = []
        for row in file_reader:
            if row["min_salary"].isnumeric():
                salaries.append(int(row["min_salary"]))
        return min(salaries)


def validate_salary_range_inputs(job: Dict, salary: Union[int, str]) -> bool:
    """Validate matches_salary_range params

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job


    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    min_salary = job["min_salary"]
    max_salary = job["max_salary"]
    inputs = [min_salary, max_salary, salary]
    all_numeric = all(
        isinstance(salary, int) or str(salary).isdigit() for salary in inputs
    )
    if not all_numeric:
        raise ValueError
    if int(min_salary) > int(max_salary):
        raise ValueError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise
    """

    validate_salary_range_inputs(job, salary)
    min_salary = int(job["min_salary"])
    max_salary = int(job["max_salary"])
    return min_salary <= int(salary) <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """

    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            continue

    return filtered_jobs


# print(get_min_salary("./data/jobs.csv"))  # DEBUG
