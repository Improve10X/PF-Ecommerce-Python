from Product import Product


class DummyDataFactory:
    @staticmethod
    def create_dummy_products():
        return [
            Product("Laptop", 700, 10),
            Product("Phone", 500, 5),
            Product("Headphones", 100, 0),
            Product("Mouse", 30, 20),
            Product("Keyboard", 50, 15),
        ]

    @staticmethod
    def preloadData(product_catalog):
        for product in DummyDataFactory.create_dummy_products():
            product_catalog.add_product(product)
