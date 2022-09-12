import pytest
from working import convert


invalid_string_hours = [
    ("09:00 AM - 17:00 PM"),
    ("9 AM - 5 PM"),
    ("9:60 AM to 5:60 PM"),
    ("9h30 AM to 5h20 PM")
]


valid_string_hours_begins_with_am = [
    ("10 AM to 5 PM", "10:00 to 17:00"),
    ("9:00 AM to 5:00 PM", "09:00 to 17:00"),
    ("12:00 AM to 12:00 PM", "00:00 to 12:00"),
    ("12 AM to 12 PM", "00:00 to 12:00"),
    ("12 PM to 12 AM", "12:00 to 00:00")
]

valid_string_hours_begins_with_pm = [
    ("9 PM to 5 AM", "21:00 to 05:00"),
    ("9:00 PM to 5:00 AM", "21:00 to 05:00")
]


@pytest.mark.parametrize("test_input", invalid_string_hours)
def test_invalid_string_hours(test_input):
    with pytest.raises(ValueError):
        assert convert(test_input)


@pytest.mark.parametrize("test_input, expected", valid_string_hours_begins_with_am)
def test_valid_string_hour_begins_with_am(test_input, expected):
    assert convert(test_input) == expected


@pytest.mark.parametrize("test_input, expected", valid_string_hours_begins_with_pm)
def test_valid_string_hour_begins_with_pm(test_input, expected):
    assert convert(test_input) == expected
