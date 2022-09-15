import pytest
from seasons import format_time


valid_dates = [
    ("2021-01-01", "Eight hundred eighty-eight thousand, four hundred eighty minutes"),
    ("1998-02-28", "Twelve million, nine hundred two thousand, four hundred minutes")

]

invalid_dates = [
    ("bla"),
    ("January 1, 1999")

]


@pytest.mark.parametrize("test_input, expected", valid_dates)
def test_valid_dates(test_input, expected):
    assert format_time(test_input) == expected


@pytest.mark.parametrize("test_input", invalid_dates)
def test_invalid_dates(test_input):
    with pytest.raises(SystemExit):
        assert format_time(test_input)
