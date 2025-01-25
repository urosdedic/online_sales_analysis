from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        if not self.products:
            return "No products available."
        return "\n".join([product.display_info() for product in self.products])

    def total_inventory_value(self):
        return sum(product.price * product.quantity for product in self.products)
    
    def remove_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return f"Product '{name}' has been removed."
        return f"Product '{name}' not found."