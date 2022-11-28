# Empieza por crear una clase de tienda que tenga 2 atributos: un nombre y una lista de productos. El nombre debe proporcionarse en el momento de la creación, pero la lista de productos debe estar vacía.

class Store:

    def __init__(self, name, list_products=[]):
        self.name = name
        self.list_products = list_products

    def add_product(self, new_product):
        self.list_products.append(new_product)
        return self

    def sell_product(self, id):
        found = False
        for product in self.list_products:
            if product.id == id :
                print("Sold:")
                self.list_products[id].print_info()
                del self.list_products[id]
                found = True
        if not found :
            print("Product id not found")
        return self

    def inflation(self, percent_increase):
        for product in self.list_products:
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.list_products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self