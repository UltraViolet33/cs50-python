import project
import pytest
import mock
from unittest.mock import patch


def test_display_menu():
    
    menu_str = "-------- EXPENSES MANAGER -------- \n"
    menu_str += "-------- MENU -------- \n"
    menu_str += "1 - Add an expense \n"
    menu_str += "2 - See all expenses \n"
    menu_str += "3 - Exit program \n"
    
    assert project.display_menu() == menu_str
    

    
@patch('builtins.input', return_value=1)   
def test_get_user_choice(mock_input):
    assert project.get_user_choice() == 1
    
    

def test_system_exit():
    with pytest.raises(SystemExit):
        project.exit_program()
    
    