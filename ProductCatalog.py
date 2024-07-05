class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.name == product_id:  # Assuming product name as ID for now
                return product
        return None

    def get_all_products(self):
        return self.products

    def remove_product(self, product):
        self.products.remove(product)
