from UserInterface import UserInterface


class CustomerUI(UserInterface):
    def __init__(self, customer):
        self.customer = customer

    def display_menu(self):
        print("\nCustomer Menu:")
        print("1. View Product Listing")
        print("2. View Product Details")
        print("3. Add to Cart")
        print("4. Remove from Cart")
        print("5. Clear Cart")
        print("6. Checkout")
        print("0. Back to Main Menu")

    def handle_user_input(self):
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if choice == 1:
                self.customer.view_product_listing()
            elif choice == 2:
                product_id = input("Enter product name: ")
                self.customer.view_product_details(product_id)
            elif choice == 3:
                product_id = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))
                self.customer.add_to_cart(product_id, quantity)
            elif choice == 4:
                product_id = input("Enter product name: ")
                self.customer.remove_from_cart(product_id)
            elif choice == 5:
                self.customer.clear_cart()
            elif choice == 6:
                self.customer.checkout()
            elif choice == 0:
                return  # Go back to the main menu
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
