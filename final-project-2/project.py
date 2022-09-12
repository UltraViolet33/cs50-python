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
        print(display_menu_all_expenses())
        user_choice = get_user_choice()
        menu_all_expenses(user_choice)

    else:
        exit_program()


def display_menu_all_expenses():
    menu = "-------- EXPENSES MANAGER -------- \n"
    menu += "-------- MENU SINGLE EXPENSE -------- \n"
    menu += "1 --See a particular expense --- \n"
    menu += "2 -- go back to the menu --- \n"
    menu += "2 -- Exit program--- \n"

    return menu


def menu_all_expenses(user_choice):
    if user_choice == 1:
        # see particular expense
        while True:
            try:
                id_expense = int(input("What ID ? "))
                break
            except ValueError:
                print("ID must be an integer")
        print(id_expense)
        Expense.read_single_expense(id_expense)
        print(display_menu_single_expense())
        user_choice = get_user_choice()
        menu_single_expense(user_choice, id_expense)
        pass
    elif user_choice == 2:
        main()
    else:
        exit_program()


def display_menu_single_expense():
    menu = "-------- EXPENSES MANAGER -------- \n"
    menu += "-------- MENU SINGLE EXPENSE -------- \n"
    menu += "1 -- GO back to the menu --- \n"
    menu += "2 -- DELETE this expense --- \n"
    menu += "3 -- Exit program--- \n"

    return menu


def menu_single_expense(user_choice, id_expense=None):
    if user_choice == 1:
        main()
    elif user_choice == 2:
        Expense.delete_expense(id_expense)
        main()
        
    else:
        exit_program()


if __name__ == "__main__":
    main()
