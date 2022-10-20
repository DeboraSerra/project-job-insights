from datetime import date
from src.sorting import sort_by
from src.jobs import read


def test_sort_by_criteria():
    dict_file = read("src/jobs.csv")
    result_min_salary = sort_by(dict_file, "min_salary")
    result_max_salary = sort_by(dict_file, "max_salary")
    result_date = sort_by(dict_file, "date_posted")
    date1 = result_date[0]["date_posted"]
    date2 = result_date[1]["date_posted"]
    assert int(
        result_min_salary[0]["min_salary"] < result_min_salary[1]["min_salary"]
    )
    assert int(
        result_max_salary[0]["max_salary"] > result_max_salary[1]["max_salary"]
    )
    assert date.fromisoformat(date1) > date.fromisoformat(date2)
