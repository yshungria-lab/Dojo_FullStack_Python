import itertools

class Product:

    newid= itertools.count()

    def __init__(self, name, price, category):
        self.id = next(Product.newid)
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if (is_increased):
            self.price += self.price * percent_change/100
        elif not is_increased:
            self.price -= self.price * percent_change/100
        return

    def print_info(self):
        print(f"Product id: {self.id}  Product Name: {self.name}, Price: {self.price}, Category: {self.category}")