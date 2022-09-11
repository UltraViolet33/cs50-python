input = input("Input: ")

vowels = "aeiou"


for letter in input:
    if letter.lower() in vowels:
        input = input.replace(letter, '')


print(input)
