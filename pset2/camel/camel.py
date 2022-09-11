input_user = input("CameCase: ")

for c in input_user:
    if c.isupper():
        index = input_user.find(c)
        input_user = input_user[:index] + "_" + input_user[index:]

print(input_user.lower())
