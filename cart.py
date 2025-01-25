class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def calculate_total(self):
        return sum(item.price * item.quantity for item in self.cart_items)

    def display_cart(self):
        if not self.cart_items:
            return "The cart is empty."
        return "\n".join([item.display_info() for item in self.cart_items])