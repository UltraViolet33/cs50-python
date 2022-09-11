import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level >= 1 and isinstance(level, int):
            break
    except ValueError:
        pass

secret_number = random.randint(1, level)

while True:
    try:
        input_user = int(input("Guess: "))
        if input_user >= 1 and isinstance(level, int):
            if input_user > secret_number:
                print("Too large!")
            elif input_user < secret_number:
                print("Too small!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass

sys.exit()
