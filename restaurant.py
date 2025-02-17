class Restaurant:
    def __init__(self):
        self.menu = {}
        self.customers = {}
        self.admins = {}

    def show_menu(self):
        if not self.menu:
            print("The menu is empty.")
        else:
            print("\nRestaurant Menu:")
            for item, price in self.menu.items():
                print(f"{item}: {price}Tk")

    def add_menu_item(self, item, price):
        self.menu[item] = price
        print(f"Added {item} to menu for {price}Tk")

    def remove_menu_item(self, item):
        if item in self.menu:
            del self.menu[item]
            print(f"Removed {item} from menu.")
        else:
            print("Item not found in menu.")

    def update_menu_item(self, item, new_price):
        if item in self.menu:
            self.menu[item] = new_price
            print(f"Updated {item} price to {new_price}TK")
        else:
            print("Item not found in menu.")

    def show_customers(self):
        if not self.customers:
            print("No registered customers.")
        else:
            print("\nRegistered Customers:")
            for email, customer in self.customers.items():
                print(f"Name: {customer.name}, Email: {email}, Address: {customer.address}, Balance: {customer.balance}TK")
