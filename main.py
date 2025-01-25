from product import Product
from product_manager import ProductManager

# Kreiramo instancu ProductManager
manager = ProductManager()

# Dodajemo proizvode
manager.add_product(Product("Laptop", 1000, 5))
manager.add_product(Product("Mouse", 20, 50))
manager.add_product(Product("Keyboard", 50, 30))

# Prikazujemo sve proizvode
print("All Products:")
print(manager.display_all_products())

# Prikazujemo ukupnu vrednost inventara
print("\nTotal Inventory Value:")
print(manager.total_inventory_value())