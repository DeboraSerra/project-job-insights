from datetime import date
from src.sorting import sort_by
import pytest

dict_jobs = [
    {
        "job_title": "Diesel Mechanic",
        "company": "Kingdom Associates",
        "state": "NY",
        "city": "Maspeth",
        "min_salary": "46298",
        "max_salary": "55893",
        "industry": "Construction, Repair & Maintenance",
        "rating": "3.5",
        "date_posted": "2020-05-01",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "338",
    },
    {
        "job_title": "OT/ICS Systems Engineer",
        "company": "Forescout Technologies Inc.",
        "state": "NY",
        "city": "New York",
        "min_salary": "122296",
        "max_salary": "148734",
        "industry": "Information Technology",
        "rating": "3.4",
        "date_posted": "2020-04-28",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "340",
    },
    {
        "job_title": "Paid Search Director",
        "company": "National Debt Relief",
        "state": "NY",
        "city": "New York",
        "min_salary": "91572",
        "max_salary": "114484",
        "industry": "Finance",
        "rating": "4.0",
        "date_posted": "2020-04-25",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "341",
    },
    {
        "job_title": "Emergency Veterinary Technician",
        "company": "Veterinary Emergency Group",
        "state": "NJ",
        "city": "Paramus",
        "min_salary": "38471",
        "max_salary": "43006",
        "industry": "Health Care",
        "rating": "4.9",
        "date_posted": "2020-05-08",
        "valid_until": "2020-06-07",
        "job_type": "PART_TIME",
        "id": "343",
    },
    {
        "job_title": "Principal, Sr. Consultant – Creative Technologist",
        "company": "TEECOM",
        "state": "NY",
        "city": "New York",
        "min_salary": "64829",
        "max_salary": "104769",
        "industry": "Telecommunications",
        "rating": "4.1",
        "date_posted": "2020-05-08",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "344",
    },
    {
        "job_title": "RN/LPN (PRN)",
        "company": "Friedwald Center for Rehabilitation and Nursing",
        "state": "NY",
        "city": "New York",
        "min_salary": "65665",
        "max_salary": "87057",
        "industry": "Biotech & Pharmaceuticals",
        "rating": "2.5",
        "date_posted": "2020-04-28",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "345",
    },
    {
        "job_title": "Regional Vice President",
        "company": "PlanMember Financial",
        "state": "NY",
        "city": "New York",
        "min_salary": "84236",
        "max_salary": "162105",
        "industry": "Finance",
        "rating": "3.6",
        "date_posted": "2020-04-27",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "348",
    },
    {
        "job_title": "Doctor of Veterinary Medicine",
        "company": "Banfield Pet Hospital",
        "state": "NY",
        "city": "Staten Island",
        "min_salary": "81991",
        "max_salary": "120117",
        "industry": "Health Care",
        "rating": "3.2",
        "date_posted": "2020-05-02",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "353",
    },
    {
        "job_title": "Hair Stylist",
        "company": "JK Salon and Spa",
        "state": "NJ",
        "city": "Fort Lee",
        "min_salary": "",
        "max_salary": "",
        "industry": "",
        "rating": "",
        "date_posted": "2020-05-07",
        "valid_until": "2020-06-07",
        "job_type": "PART_TIME",
        "id": "354",
    },
    {
        "job_title": "RN / LPN",
        "company": "Star Pediatric Home Care Agency",
        "state": "NJ",
        "city": "Jersey City",
        "min_salary": "48000",
        "max_salary": "75000",
        "industry": "Health Care",
        "rating": "4.5",
        "date_posted": "2020-04-29",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "355",
    },
    {
        "job_title": "Ultrasound Technologist",
        "company": "Middle Village Radiology",
        "state": "NY",
        "city": "Rego Park",
        "min_salary": "55069",
        "max_salary": "74745",
        "industry": "",
        "rating": "3.0",
        "date_posted": "2020-05-07",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "356",
    },
    {
        "job_title": "Experienced A level mechanic",
        "company": "Motorwerks inc",
        "state": "NY",
        "city": "Mamaroneck",
        "min_salary": "21402",
        "max_salary": "52210",
        "industry": "Retail",
        "rating": "3.9",
        "date_posted": "2020-05-05",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "359",
    },
]


def test_sort_by_criteria():
    min_salary_tests()
    max_salary_tests()
    date_posted_tests()
    wrong_criteria_test()


def min_salary_tests():
    result_min_salary = sort_by(dict_jobs, "min_salary")
    if not result_min_salary:
        return False
    for index in range(len(result_min_salary) + 1):
        if index < len(result_min_salary) - 1:
            assert (
                result_min_salary[index]["min_salary"]
                <= result_min_salary[index + 1]["min_salary"]
            )
        else:
            assert result_min_salary[index] == ""


def max_salary_tests():
    result_max_salary = sort_by(dict_jobs, "max_salary")
    if not result_max_salary:
        return False
    for index in range(len(result_max_salary) + 1):
        if index < len(result_max_salary) - 1:
            assert (
                result_max_salary[index]["max_salary"]
                >= result_max_salary[index + 1]["max_salary"]
            )
        else:
            assert result_max_salary[index]["max_salary"] == ""


def date_posted_tests():
    result_date = sort_by(dict_jobs, "date_posted")
    if not result_date:
        return False
    for index in range(len(result_date) + 1):
        assert date.fromisoformat(
            result_date[index]["date_posted"]
        ) >= date.fromisoformat(result_date[index + 1]["date_posted"])


def wrong_criteria_test():
    result_wrong_criteria = sort_by(dict_jobs, 'wrong')
    assert result_wrong_criteria is None
