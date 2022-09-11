def main():
    input_user = input()
    print(convert(input_user))


def convert(input_user):

    while ':)' in input_user:
        index = input_user.find(':)')
        input_user = input_user[:index] + "🙂" + input_user[index+2:]
    while ':(' in input_user:
        index = input_user.find(':(')
        input_user = input_user[:index] + "🙁" + input_user[index+2:]

    return input_user


main()
