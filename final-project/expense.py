import csv
import datetime
from tabulate import tabulate


class Expense():

    def __init__(self, amount, kind):
        self.amount = amount
        self.kind = kind
        self.date = datetime.date.today()
        self.save_expense()

    def __str__(self):
        return f"amount: {self.amount}, kind: {self.kind}, date: {self.date}"

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, kind):
        self._kind = kind

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @classmethod
    def get(cls):
        while True:
            try:
                amount = int(input("Amount: "))
                kind = input("Kind: ")
                return cls(amount, kind)
            except ValueError:
                print("A positive integer")

    @classmethod
    def see_total_expenses_amount(self):
        expenses = self.get_expenses_from_file(self)
        total_amount = 0
        for item in expenses:
            total_amount += int(item["amount"])

        return total_amount

    @classmethod
    def read_all_expenses(self):
        all_expenses = self.get_expenses_from_file(self)
        print(tabulate(all_expenses, headers="keys", tablefmt="grid"))

    @classmethod
    def read_single_expense(self, id_expense):
        expense = self.get_single_expense(id_expense)
        list_single_expense = [expense]
        print(tabulate(list_single_expense, headers="keys", tablefmt="grid"))
        return expense

    @classmethod
    def get_single_expense(self, id_expense):
        expense = {}
        id_expense = str(id_expense)
        all_expenses = self.get_expenses_from_file(self)
        for item in all_expenses:
            if item['id'] == id_expense:
                expense = item
        return expense

    @classmethod
    def delete_expense(self, id_expense):
        id_expense = str(id_expense)
        all_expenses = self.get_expenses_from_file(self)
        for item in all_expenses:
            if item['id'] == id_expense:
                all_expenses.remove(item)
        self.write_expense_to_file(all_expenses)

    def save_expense(self):
        expense = self.to_dict()
        self.save_expenses_to_file(expense)

    def to_dict(self):
        return {"kind": self.kind, "amount": self.amount, "date": self.date}

    def get_expenses_from_file(self):
        all_expenses = []
        with open("expenses.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                all_expenses.append(row)

        return all_expenses

    @classmethod
    def write_expense_to_file(self, expenses):
        header = ["id", "kind", "amount", "date"]

        with open("expenses.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(expenses)

    def save_expenses_to_file(self, expense):
        all_expenses = self.get_expenses_from_file()
        if len(all_expenses) == 0:
            id = 1
        else:
            id = int(all_expenses[len(all_expenses) - 1]['id']) + 1

        expense['id'] = id
        all_expenses.append(expense)

        self.write_expense_to_file(all_expenses)
