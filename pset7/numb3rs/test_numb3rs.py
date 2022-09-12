import pytest
import numb3rs


@pytest.mark.parametrize("test_input,expected", [("127.0.0.1", True), ("255.255.255.255", True)])
def test_valid_IP_adresses(test_input, expected):
    assert numb3rs.validate(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("512.512.512.512", False), ("75.456.76.65", False)])
def test_invalid_IP_adresses(test_input, expected):
    assert numb3rs.validate(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("cat", False), ("foo bar", False)])
def test_random_string_input(test_input, expected):
    assert numb3rs.validate(test_input) == expected
