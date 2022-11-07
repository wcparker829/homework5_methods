import pytest
from functions import *

def geninputs():
    inputs = ["10", "2", "5", "10"]
    for item in inputs:
        yield item

def genzero():
    inputs = ["4", "0"]
    for item in inputs:
        yield item

def gendecimal():
    inputs = ["0.8", "0.2"]
    for item in inputs:
        yield item

GEN = geninputs()
@pytest.mark.parametrize("expected", ["5.0", "0.5"])
def test_divide(capsys, monkeypatch, expected):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    try:
        divide()
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip().rsplit(" ", 1)[1] == expected
    except ZeroDivisionError as exc:
        assert False, f"'4 / 0' raised an exception {exc}"
    except ValueError as exc:
        assert False, f"'4 / 0' raised an exception {exc}"


@pytest.mark.parametrize("values, expected", [(9, 3), (23, 4.795831523312719), (-9, "ValueError"), ("Apple", "NonNumberError")])
def test_sq(values, expected):
    assert sq(values) == expected


@pytest.mark.parametrize("first, middle, last, expected", [("John", "Isaac", "Dyess", "Hello!\nWelcome to the program John Isaac Dyess\nGlad to have you!"), ("John", 5, False, ""), ("", "", "", "Hello!\nWelcome to the program   \nGlad to have you!")])
def test_greetUser(capsys, first, middle, last, expected):
    greetUser(first, middle, last)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected


@pytest.mark.parametrize("numbers, index, expected", [([1, 2, 3], 1, "Your item at 1 index is 2"), ([1, 2, 3], -1, "Your item at -1 index is 3"), ([1, 2, 3], 5, "IndexError"), ([], 0, "IndexError")])
def test_displayItem(capsys, numbers, index, expected):
    displayItem(numbers, index)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected