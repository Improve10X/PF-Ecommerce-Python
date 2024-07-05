from tabulate import tabulate

class ProductBrowser:
    def __init__(self, product_catalog):
        self.product_catalog = product_catalog

    def display_products(self):
        headers = ["Product Name", "Price ($)", "Discount (%)", "Price After Discount ($)"]
        table_data = []
        print("Available Products:")
        for product in self.product_catalog.get_all_products():
            discounted_price = product.price * (1 - product.discount_percentage / 100)
            table_data.append([product.name, f"{product.price:.2f}", f"{product.discount_percentage}", f"{discounted_price:.2f}"])
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def display_product_details(self, product_id):
        product = self.product_catalog.get_product_by_id(product_id)
        if product:
            print("Product Details:")
            headers = ["Label", "Value"]
            table_data = []
            table_data.append(["Name", product.name])
            table_data.append(["Price", f"${product.price:.2f}"])
            table_data.append(["Discount", f"${product.discount_percentage}%"])
            table_data.append(["Final Price", f"${product.final_price():.2f}"])
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        else:
            print("Product not found.")
