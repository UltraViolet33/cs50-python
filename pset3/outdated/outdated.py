
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    date = get_date()
    print(date)


def get_date():
    while True:
        try:
            date = input("Date: ")
            date = date.strip()
            if "/" in date:
                dateList = date.split("/")
                year = dateList[2]
                month = check_month(int(dateList[0]))
                if not month:
                    pass
                else:
                    day = check_day(int(dateList[1]))
                    if not day:
                        pass
                    else:
                        return f"{year}-{month}-{day}"

            if "," in date:
                dateList = date.split(" ")
                year = dateList[2]

                month = check_month(dateList[0], letters=True)
                if not month:
                    pass
                else:
                    dayList = dateList[1].split(",")
                    day = int(dayList[0])
                    day = check_day(day)
                    if not day:
                        pass
                    else:
                        return f"{year}-{month}-{day}"
        except ValueError:
            pass


def check_month(month, letters=False):
    if letters:
        month = months.index(month) + 1
    if month > 12:
        return False
    elif month < 10:
        return "0" + str(month)
    else:
        return month


def check_day(day):
    if day > 31:
        return False
    elif day < 10:
        return "0" + str(day)
    else:
        return day


main()
