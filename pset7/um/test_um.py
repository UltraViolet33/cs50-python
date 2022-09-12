import pytest
from um import count


invalid_strings = [
    ("instrumentation", 0),
    ("instrumentalist", 0),
    ("test", 0)
]


valid_strings_lowercase = [
    ("um. um", 2),
    ("um, thks", 1),
    (" um ", 1)
]

valid_strings_uppercase = [
    ("Um Um", 2),
    (" Um ", 1)
]


@pytest.mark.parametrize("test_input, expected", invalid_strings)
def test_invalid_strings(test_input, expected):
    assert count(test_input) == expected


@pytest.mark.parametrize("test_input, expected", valid_strings_lowercase)
def test_invalid_strings_lowercase(test_input, expected):
    assert count(test_input) == expected


@pytest.mark.parametrize("test_input, expected", valid_strings_uppercase)
def test_invalid_strings_uppercase(test_input, expected):
    assert count(test_input) == expected
