def main():
    time_input = input("What time is it ? ")
    time = convert(time_input)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    hours = time.split(":")[0]
    minutes = time.split(":")[1]
    minutes = int(minutes) / 60
    return int(hours) + minutes


if __name__ == "__main__":
    main()
