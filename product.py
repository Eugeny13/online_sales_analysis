class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product_info(self):
        print(f"Product: {self.name}")
        print(f"Price per unit (with tax): {self.price * (1 + Product.tax)}")
        print(f"Quantity: {self.quantity}")
        print(f"Total price: {self.calculate_total_price()}")

    def show_total_quantity(self):
        return self.quantity * self.name
    
    