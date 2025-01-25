from product import Product
from product_manager import ProductManager

# Kreiramo instancu ProductManager
manager = ProductManager()

# Dodajemo proizvode
manager.add_product(Product("Desktop", 1000, 3))
manager.add_product(Product("Miš", 20, 70))
manager.add_product(Product("Tastatura", 50, 20))

