import random


def main():
    level = get_level()
    count = 1
    score = 0
    while count < 10:
        number1 = generate_integer(level)
        number2 = generate_integer(level)
        user_try = 0
        while user_try < 3:
            try:
                answer = int(input(f"{number1} + {number2} = "))
                if answer != number1 + number2:
                    print("EEE")
                    user_try += 1
                else:
                    score += 1
                    print(score)
                    count += 1
                    break
            except ValueError:
                print("EEE")
                user_try += 1

        if user_try == 3:
            print(f"{number1} + {number2} = {number1 + number2} ")

    print("Score ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level < 4:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
