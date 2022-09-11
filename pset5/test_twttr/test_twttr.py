from twttr import shorten


def main():
    test_upper_lower_case()
    test_str_number()
    test_ponctuation()


def test_upper_lower_case():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("Ulysse") == "lyss"
    assert shorten("test") == "tst"


def test_str_number():
    assert shorten('100') == '100'


def test_ponctuation():
    assert shorten(",;:!") == ",;:!"


if __name__ == "__main__":
    main()
