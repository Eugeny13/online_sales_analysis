from product_manager import ProductManager
from cart import Cart
# Define the list of products, each product is a tuple: (product name,price per unit, quantity)
products = [     
    ("Laptop", 800.00, 10),
    ("Smartphone", 500.00, 25),
    ("Headphones", 30.00, 50),
    ("Monitor", 150.00, 15),
    ("Keyboard", 20.00, 40),
    ("Mouse", 15.00, 60)
]

# Adding a new product to the end of the list
products.append("Tablet")
print(products)

products_on_sale = ("Laptop", "Monitor", "Mouse")
new_category = ("Headphones", "Camera")

# Merging two tuples
all_products = products_on_sale + new_category
print(all_products) 

# Initialize total inventory value
total_inventory_value = 0.0

# Iterate over the list of products
for product in products:
    name = product[0]
    quantity = product[1]
    price = product[2]
    # Calculate the inventory value for the product
    inventory_value = quantity * price     # Add to the total inventory value
    total_inventory_value += inventory_value
    # Optional: Print the inventory value for each product
    # print(f"{name}: Quantity = {quantity}, Price = ${price:.2f}, Inventory Value = ${inventory_value:.2f}")

# Print the total inventory value
print(f"The total value of all inventory is: ${total_inventory_value:.2f}")

cart_items = [
    ("Smartphone", 500.00, 1),
    ("Headphones", 30.00, 2),
    ("Monitor", 150.00, 1)
]
for product in products:
    cart_items.append {product[0]}
    cart_items.append {product[1]}
    cart_items.append {product[2]}
    total_cart_items = sum (price() * quantity, quantity in cart_items())
print(total_cart_items)