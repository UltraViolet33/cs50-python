import datetime
import unittest
from expense import Expense


class TestExpense(unittest.TestCase):

    def test_str(self):
        expense = Expense(10, "test")
        date_today = datetime.date.today()
        str_expense = expense.__str__()
        self.assertEqual(str_expense,
                         f"amount: 10, kind: test, date: {date_today}")
