class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, descrption=""):
        self.ledger.append({"amount": amount, "description": descrption})

    def get_balance(self):
        balance = 0

        for entry in self.ledger:
            print(entry)
            balance += entry['amount']

        return balance


def create_spend_chart(categories):
    pass