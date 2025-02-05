from restaurant import Restaurant
from customer import Customer
from admin import Admin


def main():
    baperHotel = Restaurant()
    while True:
        print("\n1. Register as Admin\n2. Register as Customer\n3. Admin Login\n4. Customer Login\n5. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            name = input("Enter admin name: ")
            email = input("Enter admin email: ")
            password = input("Enter password: ")
            baperHotel.admins[email] = Admin(name, email, password)
            print("Admin registered successfully.")
        
        elif choice == "2":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            address = input("Enter customer address: ")
            password = input("Enter password: ")
            baperHotel.customers[email] = Customer(name, email, address, password)
            print("Customer registered successfully.")
        
        elif choice == "3":
            email = input("Enter admin email: ")
            password = input("Enter password: ")
            if email in baperHotel.admins and baperHotel.admins[email].password == password:
                baperHotel.admins[email].manage_menu(baperHotel)
            else:
                print("Invalid login.")
        
        elif choice == "4":
            email = input("Enter customer email: ")
            password = input("Enter password: ")
            if email in baperHotel.customers and baperHotel.customers[email].password == password:
                customer = baperHotel.customers[email]
                while True:
                    print("\nCustomer Menu:\n1. View Menu\n2. Place Order\n3. View Balance\n4. Add Balance\n5. View Order History\n6. Logout")
                    customer_choice = input("Select an option: ")
                    if customer_choice == "1":
                        baperHotel.show_menu()
                    elif customer_choice == "2":
                        customer.place_order(baperHotel)
                    elif customer_choice == "3":
                        customer.view_balance()
                    elif customer_choice == "4":
                        amount = float(input("Enter amount to add: "))
                        customer.add_balance(amount)
                    elif customer_choice == "5":
                        customer.view_order_history()
                    elif customer_choice == "6":
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Invalid login.")
        
        elif choice == "5":
            print("Thanks for comming BaperHotel. Goodbye...!")
            break
        else:
            print("Invalid choice. Try again.")


main()