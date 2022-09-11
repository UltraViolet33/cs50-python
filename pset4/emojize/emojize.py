import emoji

emoji_input = input("Input: ")


print(emoji.emojize(f"Python is {emoji_input}", language="alias"))
