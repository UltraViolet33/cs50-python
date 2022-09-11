from bank import value


def main():
    test_starts_with_hello()
    test_starts_with_h()
    test_starts_with_no_h()


def test_starts_with_hello():
    assert value("hello") == 0
    assert value("Hello") == 0


def test_starts_with_h():
    assert value("Hey") == 20
    assert value("hey") == 20


def test_starts_with_no_h():
    assert value('test') == 100


if __name__ == "__main__":
    main()
