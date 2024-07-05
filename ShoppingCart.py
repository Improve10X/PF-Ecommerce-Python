class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]

    def clear_cart(self):
        self.items.clear()

    def get_total_price(self):
        return sum(product.final_price() * quantity for product, quantity in self.items.items())

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            for product, quantity in self.items.items():
                print(f"{product.name} x {quantity} = ${product.final_price() * quantity:.2f}")
            print(f"Total: ${self.get_total_price():.2f}")
