class Customer:
    def __init__(self, name, email, address, password):
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.balance = 0.0
        self.order_history = []

    def add_funds(self, amount):
        self.balance += amount
        print(f"{amount}Tk added to your balance. New balance: {self.balance}Tk")

    def view_balance(self):
        print(f"Your current balance is {self.balance}TK")