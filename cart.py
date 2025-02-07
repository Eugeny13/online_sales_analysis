class Cart:
    def __init__(self, cart_items=list):
        self.cart_items = cart_items

    def add_product(self,product,quantity):
        if product in self.cart_items:
            self.cart_items[product] += quantity
        else:
            self.cart_items[product] = quantity
    def total_spent(self):
        price = 0.0
        quantity = 0
        return sum (price() * quantity for product, quantity in self.cart_items())
    def display_info(cart_items):
        return("Cart: {self.cart_items}, total spent: {total_spent}")