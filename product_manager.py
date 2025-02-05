class ProductManager:
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
         # Instance fields (specific to each instance)
        self.name = name
        self.price = price
        self.quantity = quantity

# Define the list of products, each product is a tuple: (product name,price per unit, quantity)
products = [     ("Laptop", 800.00, 10),
    ("Smartphone", 500.00, 25),
    ("Headphones", 30.00, 50),
    ("Monitor", 150.00, 15),
    ("Keyboard", 20.00, 40),
    ("Mouse", 15.00, 60)
]






 