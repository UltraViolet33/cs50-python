import csv
import datetime
from multiprocessing.forkserver import read_signed


class Expense():

    def __init__(self, amount, kind):
        self.amount = amount
        self.kind = kind
        self.date = datetime.date.today()
        self.save_expense()

    def __str__(self):
        return f"amount: {self.amount}, kind: {self.kind}, date {self.date}"

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

    def save_expenses_to_file(self, expense):
        header = ["kind", "amount", "date"]
        all_expenses = self.get_expenses_from_file()
        all_expenses.append(expense)

        with open("expenses.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(all_expenses)
