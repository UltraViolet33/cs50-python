from expense import Expense
from typing import Union
import sys


def main() -> None:
    """Main function, display the main menu and get the user choice"""
    print(display_menu("main_menu"))

    # get the user choice
    user_choice_main_menu: int = get_user_choice()
    main_menu(user_choice_main_menu)


def display_menu(menu: str) -> str:
    """display a particular menu"""

    main_menu: str = "---------- EXPENSES MANAGER ---------- \n ---------- MAIN MENU ---------- \n 1 - Add an expense \n 2 - See all expenses \n 3 - Exit program \n"
    menu_all_expenses: str = "---------- EXPENSES MANAGER ---------- \n ---------- MENU ALL EXPENSES ---------- \n 1 - See a particular expense \n 2 - Back to main menu \n 3 - Exit program \n"
    menu_single_expense: str = "---------- EXPENSES MANAGER ---------- \n ---------- MENU SINGLE EXPENSE ---------- \n 1 - Back to main menu \n 2 - Delete this expense \n 3 - Exit program \n"

    if menu == "main_menu":
        return main_menu
    elif menu == "menu_all_expenses":
        return menu_all_expenses
    elif menu == "menu_single_expense":
        return menu_single_expense
    else:
        raise ValueError("Invalid menu")


def exit_program() -> None:
    """Exit the programm"""
    sys.exit("Good Bye ! See you soon !")


def get_user_choice() -> int:
    """Get the user choice for a menu"""
    while True:
        try:
            user_choice: int = (int(input("User choice: ")))
            if user_choice not in [1, 2, 3]:
                raise ValueError
            return user_choice
        except ValueError:
            print("Please type 1 or 2 or 3")


def main_menu(user_choice: int) -> None:
    """Call the action from the user choice in the main menu"""
    if user_choice == 1:
        Expense.get()
    elif user_choice == 2:
        Expense.read_all_expenses()
        print(display_menu("menu_all_expenses"))
        user_choice_all_expenses_menu: int = get_user_choice()
        menu_all_expenses(user_choice_all_expenses_menu)
    else:
        exit_program()


def menu_all_expenses(user_choice: int) -> None:
    """Call the action from the user choice in the menu all expenses"""
    if user_choice == 1:
        while True:
            try:
                id_expense: int = int(input("What ID ? "))
                break
            except ValueError:
                print("ID must be an integer")
        Expense.read_single_expense(id_expense)
        print(display_menu("menu_single_expense"))
        user_choice_single_expense_menu: int = get_user_choice()
        menu_single_expense(user_choice_single_expense_menu, id_expense)
    elif user_choice == 2:
        main()
    else:
        exit_program()


def menu_single_expense(user_choice: int,
                        id_expense: Union[int, None] = None) -> None:
    """Call the action from the user choice in the menu single expense"""
    if user_choice == 1:
        main()
    elif user_choice == 2:
        Expense.delete_expense(id_expense)
        main()
    else:
        exit_program()
        
        


if __name__ == "__main__":
    main()
