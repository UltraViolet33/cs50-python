import sys


def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):

    if "/" not in fraction:
        raise (ValueError)
    else:
        fraction_list = fraction.split("/")
        x = int(fraction_list[0])
        y = int(fraction_list[1])
        if x > y:
            raise (ValueError)
        percentage = x/y * 100
        percentage = round(percentage)
        return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
