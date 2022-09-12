import project
import pytest
from unittest.mock import patch


def test_display_menu():
    menu_str = "-------- EXPENSES MANAGER -------- \n"
    menu_str += "-------- MENU -------- \n"
    menu_str += "1 - Add an expense \n"
    menu_str += "2 - See all expenses \n"
    menu_str += "3 - Exit program \n"

    assert project.display_menu() == menu_str


@patch('builtins.input', return_value=1)
def test_get_user_choice_1(mock_input):
    assert project.get_user_choice() == 1


@patch('builtins.input', return_value=2)
def test_get_user_choice_2(mock_input):
    assert project.get_user_choice() == 2


@patch('builtins.input', return_value=3)
def test_get_user_choice_3(mock_input):
    assert project.get_user_choice() == 3


@patch('builtins.input', return_value=4)
def test_get_user_choice_4(mock_input):
    with pytest.raises(ValueError):
        project.get_user_choice()


def test_system_exit():
    with pytest.raises(SystemExit):
        project.exit_program()
