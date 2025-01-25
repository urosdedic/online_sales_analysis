from product import Product
from product_manager import ProductManager
from cart import Cart
import random

# Kreiramo instancu ProductManager
manager = ProductManager()

# Dodajemo proizvode
manager.add_product(Product("Desktop", 1000, 3))
manager.add_product(Product("Miš", 20, 70))
manager.add_product(Product("Tastatura", 50, 20))
manager.add_product(Product("Monitor", 150, 10))
manager.add_product(Product("USB Drive", 15, 100))


# Kreiramo instancu klase Cart
cart = Cart()

# Dodajemo tri slučajna proizvoda u korpu
random_products = random.sample(manager.products, 3)
for product in random_products:
    cart.add_to_cart(product)

# Prikazujemo sadržaj korpe
print("\nCart Contents:")
print(cart.display_cart())

# Prikazujemo ukupnu vrednost korpe
print("\nTotal Cart Value:")
print(cart.calculate_total())

