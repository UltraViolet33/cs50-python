
def main():
    percentage = get_percentage()
    print(percentage)


def get_percentage():
    while True:
        try:
            fraction = input("Fraction: ")
            if "/" not in fraction:
                pass
            else:
                fraction_list = fraction.split("/")

                x = int(fraction_list[0])
                y = int(fraction_list[1])

                percentage = x/y * 100
                percentage = round(percentage)
                if x > y:
                    pass
                else:
                    if percentage >= 99:
                        return 'F'
                    elif percentage <= 1:
                        return 'E'
                    else:
                        return f'{percentage}%'

        except ValueError:
            print("Value error")
            pass
        except ZeroDivisionError:
            print("Zero division Error")
            pass


main()
