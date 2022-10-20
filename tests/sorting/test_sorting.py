from datetime import date
from src.sorting import sort_by
from src.jobs import read


def test_sort_by_criteria():
    result_min_salary = sort_by(read('tests/mocks/jobs.csv'), 'min_salary')
    result_max_salary = sort_by(read('tests/mocks/jobs.csv'), 'max_salary')
    result_date = sort_by(read('tests/mocks/jobs.csv'), 'date_posted')
    assert result_min_salary[0]['min_salary'] < result_min_salary[1]['min_salary']
    assert result_max_salary[0]['max_salary'] > result_max_salary[1]['max_salary']
    assert date(result_date[0]['date_posted']) > date(result_date[1]['date_posted'])
