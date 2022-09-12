from expense import Expense
import sys


def main():
    # user_choice = display_menu()
    print(display_menu())
    
    # get the user choice
    user_choice = get_user_choice()
    print(user_choice)
            
    



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


if __name__ == "__main__":
    main()
