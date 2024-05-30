import pytest
from utils import string_to_boolean


def test_it_should_return_true_when_value_is_true():
    result = string_to_boolean("true")
    assert result == True
    assert type(result) == bool


def test_it_should_return_false_when_value_is_false():
    result = string_to_boolean("false")
    assert result == False
    assert type(result) == bool


def test_it_should_return_true_when_value_is_t():
    result = string_to_boolean("t")
    assert result == True
    assert type(result) == bool


def test_it_should_return_false_when_value_is_f():
    result = string_to_boolean("f")
    assert result == False
    assert type(result) == bool


def test_it_should_return_true_when_value_is_1():
    result = string_to_boolean("1")
    assert result == True
    assert type(result) == bool


def test_it_should_return_false_when_value_is_0():
    result = string_to_boolean("0")
    assert result == False
    assert type(result) == bool


def test_it_should_return_false_when_value_is_empty():
    result = string_to_boolean("")
    assert result == False
    assert type(result) == bool


def test_it_should_return_false_when_value_is_none():
    result = string_to_boolean(None)
    assert result == False
    assert type(result) == bool


def test_it_should_raise_value_error_when_value_is_invalid():
    with pytest.raises(ValueError) as e:
        string_to_boolean("invalid")

    assert str(e.value) == "invalid is not a valid boolean value"
