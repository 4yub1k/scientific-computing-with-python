from itertools import zip_longest


class Category:

    def __init__(self, category_name):
        self.ledger = []
        self.category_name = category_name
        self.current_balance = 0

    def deposit(self, amount, description=""):
        self.current_balance = amount
        self.ledger.append(dict(
            amount=amount,
            description=description
        ))

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.current_balance -= amount
            return True
        return False

    def get_balance(self):
        return self.current_balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category_name}")
            category.deposit(amount, f"Transfer from {self.category_name}")
            return True
        return False

    def check_funds(self, amount):
        return True if self.get_balance() >= amount else False

    def __str__(self):
        top = self.category_name.center(30, '*')
        for item in self.ledger:
            top += f'\n{(item["description"][:23]):<23}{float(item["amount"]):7.2f}'
        return f"{top}\nTotal: {self.get_balance()}"


def create_spend_chart(categories=None):
    total_spent = list(map(lambda category: category.ledger[0]["amount"] - category.get_balance(), categories))
    percent_spent = list(map(lambda amount: int(amount/sum(total_spent) * 10), total_spent))

    spend_bar_chart = "Percentage spent by category\n"
    for per_range in range(100, -1, -10):
        spend_bar_chart += f"{per_range:>3}|"
        for per_spent in percent_spent:
            if per_spent * 10 >= per_range:
                spend_bar_chart += " o "
            else:
                spend_bar_chart += "   "
        spend_bar_chart += " \n"

    spend_bar_chart += f"{' ' * 4}{'-' * (len(percent_spent) * len(percent_spent) + 1)}\n"  # -----

    categories_name = list(map(lambda category: category.category_name, categories))
    for chars in zip_longest(*categories_name, fillvalue=' '):
        spend_bar_chart += f"{' ' * 5 +'  '.join(chars)}  \n"   # Category names, char wise.
    return spend_bar_chart[:-1]
