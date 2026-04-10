class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        balance = 0

        for entry in self.ledger:
            balance += entry["amount"]

        return balance

    def withdraw(self, amount, description=""):
        if amount <= self.get_balance():
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, category):
        withdraw_result = self.withdraw(amount, f"Transfer to: {category.name}")

        if withdraw_result:
            category.deposit(amount, f"Transfer from: {self.name}")
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

def create_spend_chart(categories):
    pass
