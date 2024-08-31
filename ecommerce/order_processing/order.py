
class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products  # A list of (product, quantity) tuples

    def calculate_total(self):
        total = 0
        for product, quantity in self.products:
            total += product.price * quantity
        return total

    def __str__(self):
        products_str = ', '.join([f"{product.name} (x{quantity})" for product, quantity in self.products])
        return f"Order(id={self.order_id}, products=[{products_str}], total={self.calculate_total()})"
    