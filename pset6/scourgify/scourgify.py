import sys
import csv


def main():
    file_before, file_after = get_filenames()
    data = get_data_from_file(file_before)
    students = update_data(data)
    write_data_to_file(students, file_after)


def get_filenames():
    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        file_before = sys.argv[1]
        file_after = sys.argv[2]
    except IndexError:
        sys.exit("Too few command-line arguments")

    return [file_before, file_after]


def get_data_from_file(filename):
    students = []
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {filename}")

    return students


def update_data(data):
    students = []
    for student in data:
        last, first = student["name"].split(",")
        first = first.lstrip()
        house = student["house"]
        students.append({"first": first, "last": last, "house": house})
    return students


def write_data_to_file(data, filename):

    with open(filename, "w") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in data:
            writer.writerow(student)


if __name__ == "__main__":
    main()
