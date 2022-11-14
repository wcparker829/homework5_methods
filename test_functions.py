import pytest
from functions import *

def geninputs():
    inputs = ["10", "2", "5", "10", "0.8", "0.2"]
    for item in inputs:
        yield item

def genzero():
    inputs = ["4", "0"]
    for item in inputs:
        yield item


GEN = geninputs()
@pytest.mark.parametrize("expected", ["5.0", "0.5", "4.0"])
def test_divide(capsys, monkeypatch, expected):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    divide()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip().rsplit(" ", 1)[1] == expected

GENZ = genzero()
def test_divide_zero(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GENZ))
    with pytest.raises(ZeroDivisionError):
        divide()

@pytest.mark.parametrize("values, expected", [(9, 3), (0.64, 0.8)])
def test_sq(values, expected):
    assert sq(values) == expected

@pytest.mark.parametrize("values", [(-9)])
def test_sq_negative(values):
    with pytest.raises(ValueError):
        sq(values)

@pytest.mark.parametrize("values", [("25")])
def test_sq_string(values):
    with pytest.raises(TypeError):
        sq(values)     

@pytest.mark.parametrize("first, middle, last, expected", [("John", "Isaac", "Dyess", "Hello!\nWelcome to the program John Isaac Dyess\nGlad to have you!"), ("", "", "", "Hello!\nWelcome to the program   \nGlad to have you!")])
def test_greetUser(capsys, first, middle, last, expected):
    greetUser(first, middle, last)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected

@pytest.mark.parametrize("first, middle, last", [("John", 5, False)])
def test_greetUser_nonstring(first, middle, last):
    with pytest.raises(ValueError):
        greetUser(first, middle, last)

@pytest.mark.parametrize("numbers, index, expected", [([1, 2, 3], 1, "Your item at 1 index is 2"), ([1, 2, "Pass"], -1, "Your item at -1 index is Pass")])
def test_displayItem(capsys, numbers, index, expected):
    displayItem(numbers, index)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected

@pytest.mark.parametrize("numbers, index", [([1, 2, 3], 5)])
def test_displayItem_outofindex(numbers, index):
    with pytest.raises(IndexError):
        displayItem(numbers, index)

@pytest.mark.parametrize("numbers, index", [([], 0.5)])
def test_displayItem_decindex(numbers, index):
    with pytest.raises(TypeError):
        displayItem(numbers, index)