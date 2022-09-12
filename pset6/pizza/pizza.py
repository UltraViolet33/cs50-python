import sys
import csv
from tabulate import tabulate


def main():
    filename = get_file()
    print_table(filename)


def get_file():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        name_file = sys.argv[1]
    except IndexError:
        sys.exit("Too few command-line arguments")

    if not "csv" in name_file:
        sys.exit("Not a CSV file")
    return name_file


def print_table(filename):
    pizzas = []

    try:
        with open(filename) as file:
            reader = csv.reader(file)
            for row in reader:
                pizzas.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(pizzas, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
