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
        
        
    def place_order(self, restaurant):
        restaurant.show_menu()
        print()
        order_items = {}
        while True:
            item = input("Enter food item (Enter 'end' for finish'): ")
            if item.lower() == 'end':
                break
            if item in restaurant.menu:
                quantity = int(input(f"Enter quantity for {item}: "))
                order_items[item] = order_items.get(item, 0) + quantity
            else:
                print("Item not found in menu.")
        
        total_cost = 0
        for item, quantity in order_items.items():
            total_cost += restaurant.menu[item] * quantity

        if total_cost > self.balance:
            print("You do not have enough balance. Please add more balance.")
        else:
            self.balance -= total_cost
            self.order_history.append(order_items)
            print(f"Order placed successfully! Total cost: {total_cost}TK")
            
            
    def view_order_history(self):
        if not self.order_history:
            print("No orders has made.")
        else:
            print("\nOrder History:")
            for i, order in enumerate(self.order_history, 1): 
                print(f"Order {i}:")
                for item, quantity in order.items():
                    print(f"{item} ({quantity})") 
                print()