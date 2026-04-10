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
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def __str__(self):
        name_length = len(self.name)
        result = (
            "*" * (15 - name_length // 2)
            + self.name
            + "*" * (15 - name_length // 2)
            + "\n"
        )

        for entry in self.ledger:
            des = entry["description"][:23]
            amo = str(format(entry["amount"], ".2f"))
            result += des + " " * (30 - len(des) - len(amo)) + amo + "\n"

        result += f"Total: {self.get_balance()}"

        return result


def create_spend_chart(categories):
    categories_summary = []
    total_spent = 0
    max_name_length = 0

    # Prepare data for printing chart
    for category in categories:
        amount = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                amount += -entry["amount"]
        total_spent += amount
        categories_summary.append({"name": category.name, "spent": round(amount, 2)})

        if len(category.name) > max_name_length:
            max_name_length = len(category.name)

    for cat in categories_summary:
        percentage = int(round(cat["spent"] / total_spent * 100, -1))
        cat.update({"percentage": percentage})
        cat.pop("spent")

    # Print chart
    result = ""

    for i in range(100, -1, -10):
        result += " " * (3 - len(str(i))) + str(i) + "|" + " "

        for cat in categories_summary:
            if cat["percentage"] >= i:
                result += "o  "
        result += "\n"

    result += "    " + "-" * 3 * len(categories_summary) + "-\n"

    # TODO implement printing labels belows columns

    print(result)


food = Category("Food")
clothing = Category("Clothing")
utilities = Category("Utilities")
health = Category("Health")
categories = [food, clothing, utilities, health]
food.deposit(1000, "initial deposit")
utilities.deposit(400)
health.deposit(600)
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
food.transfer(300, clothing)
clothing.withdraw(10.15, "socks")
clothing.withdraw(30.64)
utilities.withdraw(240, "electric bill")
health.withdraw(100, "supplements")
create_spend_chart(categories)
