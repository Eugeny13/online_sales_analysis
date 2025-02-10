from product_manager import ProductManager
from product import Product
from cart import Cart
import random
# Define the list of products, each product is a tuple: (product name,price per unit, quantity)
products = [     
    ("Laptop", 800.00, 10),
    ("Smartphone", 500.00, 25),
    ("Headphones", 30.00, 50),
    ("Monitor", 150.00, 15),
    ("Keyboard", 20.00, 40),
    ("Mouse", 15.00, 60)
]


def main():
    manager = ProductManager()

    manager.add_product(Product("Laptop", 800.00, 5))
    manager.add_product(Product("Mouse", 15.00, 15))
    manager.add_product(Product("Keyboard", 20.00, 10))
    manager.add_product(Product("Monitor", 150.00, 7))

    manager.display_all_products()

    total_value = manager.total_inventory_value()
    print(f"\nTotal Inventory Value: ${total_value:.2f}")
    
    cart = Cart()

    products = manager.products  
    for _ in range(3):
        product = random.choice(products)  #
        max_quantity = min(product.quantity, 3)  
        if max_quantity > 0:  
            quantity = random.randint(1, max_quantity)  #
            cart.add_to_cart(product, quantity)


    print("\nCart Contents:")
    cart.display_cart()

    cart_total = cart.calculate_total()
    print(f"\nTotal Cart Value: ${cart_total:.2f}")

if __name__ == "__main__":
    main()
