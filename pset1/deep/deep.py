input_user = input("What is the answer to the Great Question of Life ?")

if input_user.strip() == "42":
    print("Yes")
elif input_user.lower().strip() == "forty-two":
    print("Yes")
elif input_user.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")
