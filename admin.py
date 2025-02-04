from restaurant import Restaurant
from customer import Customer

class Admin:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def manage_menu(self, restaurant):
        while True:
            print("\nAdmin Menu:\n1. Add Menu Item\n2. Remove Menu Item\n3. Update Menu Item Price\n4. View Menu\n5. View Customers\n6. Add Customer\n7. Remove Customer\n8. Logout")
            choice = input("Select an option: ")
            if choice == "1":
                item = input("Enter food name: ")
                price = float(input("Enter price: "))
                restaurant.add_menu_item(item, price)
            elif choice == "2":
                item = input("Enter food name: ")
                restaurant.remove_menu_item(item)
            elif choice == "3":
                item = input("Enter food name: ")
                new_price = float(input("Enter new price: "))
                restaurant.update_menu_item(item, new_price)
            elif choice == "4":
                restaurant.show_menu()
            elif choice == "5":
                restaurant.show_customers()
            elif choice == "6":
                name = input("Enter customer name: ")
                email = input("Enter customer email: ")
                address = input("Enter customer address: ")
                password = input("Enter password: ")
                restaurant.customers[email] = Customer(name, email, address, password)
                print("Customer added successfully.")
            elif choice == "7":
                email = input("Enter customer email to remove: ")
                if email in restaurant.customers:
                    del restaurant.customers[email]
                    print(f"Customer with email {email} removed.")
                else:
                    print("Customer not found.")
            elif choice == "8":
                break
            else:
                print("Invalid choice.")