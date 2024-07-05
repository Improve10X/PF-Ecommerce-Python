class Customer:
    def __init__(self, product_browser, shopping_cart):
        self.product_browser = product_browser
        self.shopping_cart = shopping_cart

    def view_product_listing(self):
        self.product_browser.display_products()

    def view_product_details(self, product_id):
        self.product_browser.display_product_details(product_id)

    def add_to_cart(self, product_id, quantity):
        product = self.product_browser.product_catalog.get_product_by_id(product_id)
        if product:
            self.shopping_cart.add_item(product, quantity)
            print(f"{quantity} {product.name}(s) added to cart.")
        else:
            print("Product not found.")

    def remove_from_cart(self, product_id):
        product = self.product_browser.product_catalog.get_product_by_id(product_id)
        if product:
            self.shopping_cart.remove_item(product)
            print(f"{product.name} removed from cart.")
        else:
            print("Product not found.")

    def clear_cart(self):
        self.shopping_cart.clear_cart()
        print("Cart cleared.")

    def checkout(self):
        self.shopping_cart.display_cart()
        # In a real implementation, we would handle the payment process here
        print("Checkout functionality not implemented yet.")
