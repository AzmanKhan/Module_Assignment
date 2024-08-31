
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if quantity < 0 and abs(quantity) > self.stock:
            raise ValueError("Cannot reduce stock below zero.")
        self.stock += quantity

    def __str__(self):
        return f"Product(id={self.product_id}, name={self.name}, price={self.price}, stock={self.stock})"
    