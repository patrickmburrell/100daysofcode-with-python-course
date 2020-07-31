import pytest
import app

NUMBER_1 = 10
NUMBER_2 = 2


@pytest.fixture(scope="module")
def numbers_setup():
    print("numbers_setup")


def test_add(numbers_setup):
    result = app.add(NUMBER_1, NUMBER_2)
    assert result == 12


def test_subtract(numbers_setup):
    result = app.subtract(NUMBER_1, NUMBER_2)
    assert result == 8


def test_multiply(numbers_setup):
    result = app.multiply(NUMBER_1, NUMBER_2)
    assert result == 20


def test_divide(numbers_setup):
    result = app.divide(NUMBER_1, NUMBER_2)
    assert result == 5


def test_maximum(numbers_setup):
    result = app.maximum(NUMBER_1, NUMBER_2)
    assert result == NUMBER_1


def test_minimum(numbers_setup):
    result = app.minimum(NUMBER_1, NUMBER_2)
    assert result == NUMBER_2
