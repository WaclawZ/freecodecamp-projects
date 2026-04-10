class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        balance = 0

        for entry in self.ledger:
            balance += entry['amount']

        return balance
    
    def withdraw(self, amount, description=""):
        if amount <= self.get_balance():
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False


def create_spend_chart(categories):
    pass