from plates import is_valid


def main():
    test_doesnt_starts_with_two_letters()
    test_length()
    test_number_placement()
    test_ponctuation()


def test_doesnt_starts_with_two_letters():
    assert is_valid("4d") == False
    assert is_valid("65") == False


def test_length():
    assert is_valid("e") == False
    assert is_valid("cstestest") == False


def test_number_placement():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False


def test_ponctuation():
    assert is_valid("AAA,22") == False
    assert is_valid("  ACS50") == False


if __name__ == "__main__":
    main()
