class UserInterface:
    def display_menu(self):
        raise NotImplementedError("Subclasses must implement display_menu")

    def handle_user_input(self):
        raise NotImplementedError("Subclasses must implement handle_user_input")
