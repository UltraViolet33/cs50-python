from datetime import date, datetime
from operator import sub
import inflect
import sys


def main():
    print(format_time(input("Date of Birth: ")))


def format_time(date_birth):

    p = inflect.engine()

# get the birth date

    try:
        birth_date = date.fromisoformat(date_birth)
    except ValueError:
        sys.exit("Invalid date")

    current_date = date.today()
    diff = sub(current_date, birth_date)
    minutes = int(diff.total_seconds() / 60)
    string_minutes = p.number_to_words(minutes, andword="")
    return f"{string_minutes.capitalize()} minutes"


if __name__ == "__main__":
    main()
