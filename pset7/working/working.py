import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    conversion = {"1": "13", "2": "14", "3": "15",
                  "4": "16", "5": "17", "6": "18",
                  "7": "19", "8": "20", "9": "21",
                  "10": "22", "11": "13", "12": "12"}

    string_is_correct = re.search(
        r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)

    if not string_is_correct:
        raise ValueError

    split_string = string_is_correct.groups()

    if split_string[3] == "AM":

        am_hour = split_string[1]
        am_minutes = split_string[2]

        pm_hour = split_string[5]
        pm_minutes = split_string[6]

        if am_minutes != None:
            am_hour = int(am_hour)
            if am_hour == 12:
                am_hour = "00"
            elif am_hour < 10:
                am_hour = f"{am_hour:02}"
            else:
                pass
            new_string_am = f"{am_hour}:{am_minutes}"
            new_pm_hour = conversion[pm_hour]
            new_string_pm = f"{new_pm_hour}:{pm_minutes}"
            new_string_hour = f"{new_string_am} to {new_string_pm}"
            return new_string_hour
        else:
            am_hour = int(am_hour)
            if am_hour == 12:
                am_hour = "00"
            elif am_hour < 10:
                am_hour = f"{am_hour:02}"
            else:
                pass
            new_string_am = f"{am_hour}:00"
            new_pm_hour = conversion[pm_hour]
            new_string_pm = f"{new_pm_hour}:00"
            new_string_hour = f"{new_string_am} to {new_string_pm}"
            return new_string_hour

    else:
        am_hour = split_string[5]
        am_minutes = split_string[6]

        pm_hour = split_string[1]
        pm_minutes = split_string[2]

        if am_minutes != None:
            am_hour = int(am_hour)
            if am_hour == 12:
                am_hour = "00"
            elif am_hour < 10:
                am_hour = f"{am_hour:02}"
            else:
                pass
            new_string_am = f"{am_hour}:{am_minutes}"
            new_pm_hour = conversion[pm_hour]
            new_string_pm = f"{new_pm_hour}:{pm_minutes}"

            new_string_hour = f"{new_string_pm} to {new_string_am}"
            return new_string_hour

        else:
            am_hour = int(am_hour)
            if am_hour == 12:
                am_hour = "00"
            elif am_hour < 10:
                am_hour = f"{am_hour:02}"
            else:
                pass
            new_string_am = f"{am_hour}:00"
            new_pm_hour = conversion[pm_hour]
            new_string_pm = f"{new_pm_hour}:00"
            new_string_hour = f"{new_string_pm} to {new_string_am}"
            return new_string_hour


if __name__ == "__main__":
    main()
