from store import Store
from product import Product

market = Store("Market Yojan´s")

meat = Product("Meat", 10, "Food")
chicken = Product("Chicken", 5, "Food")
sugar = Product("Sugar", 2, "Food")
tuna = Product("Tuna", 3, "Food")
milk = Product("Milk", 1, "Dairy")
eggs = Product("Eggs", 1, "Dairy")
broccoli = Product("Broccoli", 2, "Vegetables")
apples = Product("Apples", 2, "Fruits")

market.add_product(meat).add_product(chicken).add_product(sugar).add_product(tuna).add_product(milk).add_product(eggs).add_product(broccoli).add_product(apples)

for product in market.list_products:
    product.print_info()

print("*" * 80)

market.sell_product(2).sell_product(3).set_clearance("Food", 50).inflation(10)

print("*" * 80)
for product in market.list_products:
    product.print_info()