from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    for job in result:
        assert job['title'] is not None
        assert job['salary'] is not None
        assert job['type'] is not None
        assert job['titulo'] is None
        assert job['salario'] is None
        assert job['tipo'] is None
