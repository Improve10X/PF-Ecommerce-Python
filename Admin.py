import random

from Product import Product


class Admin:
    def __init__(self, product_catalog):
        self.product_catalog = product_catalog

    def add_new_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        discount_percentage = int(input("Enter discount percentage (0 for no discount): "))
        product = Product(name, price, discount_percentage)
        self.product_catalog.add_product(product)
        print("Product added successfully!")

    def update_product(self):
        product_id = input("Enter product name to update: ")
        product = self.product_catalog.get_product_by_id(product_id)
        if product:
            new_price = float(input("Enter new price: "))
            new_discount_percentage = int(input("Enter new discount percentage (0 for no discount): "))
            product.price = new_price
            product.discount_percentage = new_discount_percentage
            print("Product updated successfully!")
        else:
            print("Product not found.")

    def remove_product(self):
        product_id = input("Enter product name to remove: ")
        product = self.product_catalog.get_product_by_id(product_id)
        if product:
            self.product_catalog.remove_product(product)
            print("Product removed successfully!")
        else:
            print("Product not found.")

    def view_all_products(self):
        for product in self.product_catalog.get_all_products():
            print(product.name, product.price, product.discount_percentage)

    def generate_sales_report(self):
        print("Sales Report:")
        # In a real implementation, we would fetch sales data from a database
        for product in self.product_catalog.get_all_products():
            # Simulating sales data
            quantity_sold = random.randint(0, 100)
            total_revenue = quantity_sold * product.final_price()
            print(f"{product.name}: Sold {quantity_sold}, Total Revenue: ${total_revenue:.2f}")
