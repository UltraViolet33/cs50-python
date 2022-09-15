from importlib.resources import path
from unittest import mock
import project
import pytest
from unittest.mock import patch


def test_display_menu():
    main_menu: str = "---------- EXPENSES MANAGER ---------- \n ---------- MAIN MENU ---------- \n 1 - Add an expense \n 2 - See all expenses \n 3 - Exit program \n"
    menu_all_expenses: str = "---------- EXPENSES MANAGER ---------- \n ---------- MENU ALL EXPENSES ---------- \n 1 - See a particular expense \n 2 - Back to main menu \n 3 - Exit program \n"
    menu_single_expense: str = "---------- EXPENSES MANAGER ---------- \n ---------- MENU SINGLE EXPENSE ---------- \n 1 - Back to main menu \n 2 - Delete this expense \n 3 - Exit program \n"

    assert project.display_menu("main_menu") == main_menu
    assert project.display_menu("menu_all_expenses") == menu_all_expenses
    assert project.display_menu("menu_single_expense") == menu_single_expense

    with pytest.raises(ValueError):
        project.display_menu("invalid menu")


@patch('builtins.input', return_value=1)
def test_get_user_choice_1(mock_input):
    assert project.get_user_choice() == 1


@patch('builtins.input', return_value=2)
def test_get_user_choice_2(mock_input):
    assert project.get_user_choice() == 2


@patch('builtins.input', return_value=3)
def test_get_user_choice_3(mock_input):
    assert project.get_user_choice() == 3


def test_system_exit():
    with pytest.raises(SystemExit):
        project.exit_program()
        



@patch("project.main")
def test_menu_all_expenses(mock_main):
    project.menu_all_expenses(2)
    mock_main.assert_called_once()

    with pytest.raises(SystemExit):
        project.menu_all_expenses(3)
        
        
@patch("project.main")
def test_menu_single_expense(mock_main):
    project.menu_single_expense(1)
    mock_main.assert_called_once()
    

    with pytest.raises(SystemExit):
        project.menu_single_expense(3)


    
    
    
