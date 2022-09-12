import sys


def main():
    filename = get_file()
    print(count_lines(filename))


def get_file():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        name_file = sys.argv[1]
    except IndexError:
        sys.exit("Too few command-line arguments")

    extension = name_file.split(".")[1]
    if not extension == "py":
        sys.exit("Not a Python file")
    return name_file


def count_lines(filename):
    count = 0
    try:
        with open(filename) as file:
            for line in file:
                if line.rstrip() == "":
                    pass
                elif line.lstrip().startswith("#"):
                    pass
                else:
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return count


if __name__ == "__main__":
    main()
