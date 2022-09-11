def main():
    user_amount = 0
    while user_amount < 50:
        amount = user_pay()
        user_amount += int(amount)
        due = 50 - user_amount
        if due >= 0:
            print("Amount due: ", 50 - user_amount)
    change = user_amount - 50
    print("Change owed: ", change)


def user_pay():
    pay_list = [25, 10, 5]
    amount = int(input("pay: "))
    if amount not in pay_list:
        amount = 0
    return amount


if __name__ == "__main__":
    main()
