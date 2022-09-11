
def main():
    word_user = input("Input: ")
    print(shorten(word_user))


def shorten(word_user):
    vowels = "aeiou"
    for letter in word_user:
        if letter.lower() in vowels:
            word_user = word_user.replace(letter, '')

    return word_user


if __name__ == "__main__":
    main()
