class Product:
    def __init__(self, name, price, discount_percentage=0):
        self.name = name
        self.price = price
        self.discount_percentage = discount_percentage

    def calculate_discount(self):
        return self.price * (self.discount_percentage / 100)

    def final_price(self):
        return self.price - self.calculate_discount()
