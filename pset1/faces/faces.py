def main():
    inputUser = input()
    print(convert(inputUser))


def convert(inputUser):

    while ':)' in inputUser:
        index = inputUser.find(':)')
        inputUser = inputUser[:index] + "🙂" + inputUser[index+2:]
    while ':(' in inputUser:
        index = inputUser.find(':(')
        inputUser = inputUser[:index] + "🙁" + inputUser[index+2:]

    return inputUser


main()
