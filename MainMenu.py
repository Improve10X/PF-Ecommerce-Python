from AdminUI import AdminUI
from CustomerUI import CustomerUI
from ProductBrowser import ProductBrowser
from ShoppingCart import ShoppingCart
from Customer import Customer
from Admin import Admin

class MainMenu:
    def __init__(self, product_catalog):
        self.product_catalog = product_catalog


    def display_main_menu(self):
        print("\nMain Menu :")
        print("1. Admin")
        print("2. Customer")
        print("0. Exit")

    def handle_main_menu_input(self):
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if choice == 1:  # Admin
                admin = Admin(self.product_catalog)
                admin_ui = AdminUI(admin)
                while True:
                    admin_ui.display_menu()
                    if admin_ui.handle_user_input() is None:
                        break

            elif choice == 2:  # Customer
                shopping_cart = ShoppingCart()
                product_browser = ProductBrowser(self.product_catalog)
                customer = Customer(product_browser, shopping_cart)
                customer_ui = CustomerUI(customer)
                while True:
                    (customer_ui
                     .display_menu())
                    if customer_ui.handle_user_input() is None:
                        break

            elif choice == 0:
                print("Exiting application.")
                exit()
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
