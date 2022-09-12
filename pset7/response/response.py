from validator_collection import validators, checkers, errors


def main():
    print(validate_email(input("What's your email address? ")))


def validate_email(email):
    try:
        email = validators.email(email)
        return "Valid"
    except ValueError:
        return "Invalid"


if __name__ == "__main__":
    main()
