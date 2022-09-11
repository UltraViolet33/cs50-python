import re


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not starts_two_letters(s) or not check_min_and_max(s) or not numbers_at_the_end(s) or not check_other_characters(s):
        return False

    return True


def starts_two_letters(s):
    return s[0:2].isalpha()


def check_min_and_max(s):
    return len(s) <= 6 and len(s) >= 2


def numbers_at_the_end(s):
    m = re.search(r"\d", s)
    if m:
        digit_part = s[m.start():]
        if digit_part[0] == "0":
            return False
        for char in digit_part:
            if not char.isdigit():
                return False
    return True


def check_other_characters(s):
    for char in s:
        if not char.isalpha() and not char.isdigit():
            return False
    return True


main()
