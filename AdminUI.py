from UserInterface import UserInterface


class AdminUI(UserInterface):
    def __init__(self, admin):
        self.admin = admin

    def display_menu(self):
        print("\nAdmin Menu:")
        print("1. Add New Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. View All Products")
        print("0. Back to Main Menu")

    def handle_user_input(self):
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if choice == 1:
                self.admin.add_new_product()
            elif choice == 2:
                self.admin.update_product()
            elif choice == 3:
                self.admin.remove_product()
            elif choice == 4:
                self.admin.view_all_products()
            elif choice == 0:
                return  # Go back to the main menu
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
