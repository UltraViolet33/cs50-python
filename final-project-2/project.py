from expense import Expense
import sys


def main():
    user_choice = display_menu()
    print(display_menu())

    # get the user choice
    user_choice = get_user_choice()
    print(user_choice)
    menu(user_choice)


def display_menu() -> str:
    menu = "-------- EXPENSES MANAGER -------- \n"
    menu += "-------- MENU -------- \n"
    menu += "1 - Add an expense \n"
    menu += "2 - See all expenses \n"
    menu += "3 - Exit program \n"
    return menu


def exit_program():
    sys.exit("Good Bye ! See you soon !")


def get_user_choice():
    while True:
        try:
            user_choice = (int(input("User choice: ")))
            if user_choice not in [1, 2, 3]:
                raise ValueError
            return user_choice
        except ValueError:
            print("Please type 1 or 2 or 3")


def menu(user_choice):
    if user_choice == 1:
        Expense.get()
    elif user_choice == 2:
        Expense.read_all_expenses()
        print(display_menu_single_expense())
        user_choice = get_user_choice()

    else:
        exit_program()


def display_menu_single_expense():
    menu = "-------- EXPENSES MANAGER -------- \n"
    menu += "-------- MENU SINGLE EXPENSE -------- \n"
    menu += "1 --See a particular expense --- \n"
    menu += "2 -- go back to the menu --- \n"
    return menu


if __name__ == "__main__":
    main()
