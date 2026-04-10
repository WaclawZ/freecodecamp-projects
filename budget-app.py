class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, descrption=""):
        self.ledger.append({"amount": amount, "description": descrption})


def create_spend_chart(categories):
    pass