import pytest
from response import validate_email

valid_emails = [
    ("malan@harvard.edu", "Valid"),
    ("test@gmail.com", "Valid")
]

invalid_emails = [
    ("malan@@@harvard.edu", "Invalid"),
    ("test@gmail..com", "Invalid")
]


@pytest.mark.parametrize("test_input, expected", valid_emails)
def test_valid_emails(test_input, expected):
    assert validate_email(test_input) == expected


@pytest.mark.parametrize("test_input, expected", invalid_emails)
def test_invalid_emails(test_input, expected):
    assert validate_email(test_input) == expected
