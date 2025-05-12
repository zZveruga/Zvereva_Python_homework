import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("Skypro", "Skypro"),
    ("test 37", "Test 37"),
    ("python", "Python")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("275", "275"),
    ("", ""),
    ("!", "!")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("string_str, expected", [
    (" Skypro", "Skypro"),
    (" Hello world", "Hello world"),
    (" Python", "Python")
])
def test_trim_positive(string_str, expected):
    assert string_utils.trim(string_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("string_str, expected", [
    (" ", ""),
    (" 37", "37")
])
def test_trim_negative(string_str, expected):
    assert string_utils.trim(string_str) == expected


@pytest.mark.positive_test
@pytest.mark.parametrize("string_str, symbol_str, result", [
    ("SkyPro", "S", True),
    ("Мир", "и", True),
    ("test 37", "37", True)
])
def test_contains_positive(string_str, symbol_str, result):
    assert string_utils.contains(string_str, symbol_str) == result


@pytest.mark.negative_test
@pytest.mark.parametrize("string_str, symbol_str, result", [
    ("SkyPro", "7", False),
    ("SkyPro", "п", False),
    ("237", "A", False)
])
def test_contains_negative(string_str, symbol_str, result):
    assert string_utils.contains(string_str, symbol_str) == result


@pytest.mark.positive_test
@pytest.mark.parametrize("string_str, symbol_str, expected", [
    ("Skypro", "Sky", "pro"),
    ("test 37", "7", "test 3"),
    ("Python", "h", "Pyton")
])
def test_delete_symbol_positive(string_str, symbol_str, expected):
    assert string_utils.delete_symbol(string_str, symbol_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("string_str, symbol_str, expected", [
        ("Skypro", "0", "Skypro"),
        ("test 37", "v", "test 37"),
        ("Python", "", "Python")
])
def test_delete_symbol_negative(string_str, symbol_str, expected):
    assert string_utils.delete_symbol(string_str, symbol_str) == expected