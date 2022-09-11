expression = input("Expression: ")

if "-" in expression:
    number1 = int(expression.split("-")[0])
    number2 = int(expression.split("-")[1])
    print(float(number1 - number2))
elif "+" in expression:
    number1 = int(expression.split("+")[0])
    number2 = int(expression.split("+")[1])
    print(float(number1 + number2))
if "*" in expression:
    number1 = int(expression.split("*")[0])
    number2 = int(expression.split("*")[1])
    print(float(number1 * number2))
if "/" in expression:
    number1 = int(expression.split("/")[0])
    number2 = int(expression.split("/")[1])
    print(float(number1 / number2))
