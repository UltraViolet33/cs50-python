import pytest
import fuel


def main():
    test_inputs_integers()
    test_zero_division()
    test_return_integer()


def test_inputs_integers():
    with pytest.raises(ValueError):
        fuel.convert("10/5")
        fuel.convert("T/R")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("-2/0")


def test_return_integer():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("4/4") == 100


def test_less_than_one():
    assert fuel.gauge(1) == "E"


def test_greate_than_ninety_nine():
    assert fuel.gauge(99) == "F"


def test_between_one_and_ninety_one():
    assert fuel.gauge(25) == "25%"
    assert fuel.gauge(75) == "75%"


if __name__ == "__main__":
    main()
