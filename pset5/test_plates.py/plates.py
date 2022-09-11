import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    print(s[:2])
    if not s[:2].isalpha():
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[len(s)-2:].isdigit():
        return False

    m = re.search(r"\d", s)
    if m:
        digit_part = s[m.start():]
        if digit_part[0] == "0":
            return False
        for char in digit_part:
            if not char.isdigit():
                return False
    for char in s:
        if not char.isalpha() and not char.isdigit():
            return False

    return True


if __name__ == "__main__":
    main()
