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




# Asignación: Tienda y productos
# Objetivos
# Practicar el crear clases
# Practicar la asociación entre clases
# Practicar modularizar código
# Empieza por crear una clase de tienda que tenga 2 atributos: un nombre y una lista de productos. El nombre debe proporcionarse en el momento de la creación, pero la lista de productos debe estar vacía.

# A continuación, crea una clase de producto que tenga 3 atributos: un nombre, un precio y una categoría. Todos estos deben proporcionarse al momento de la creación.

# Demos algunos métodos a nuestra clase Producto:

# actualizar_precio(self, cambio_porcentaje, está_elevado): actualiza el precio del producto. Si está_elevado es True, el precio debería aumentar en el cambio_porcentaje proporcionado. Si es False, el precio debería disminuir en el cambio_porcentaje proporcionado.
# Print_info(self): imprime el nombre del producto, categoría y precio.
# Demos algunos métodos a nuestra clase de producto:

# agregar_producto(self, nuevo_producto): toma un producto y lo agrega a la tienda
# vender_producto(self, id): elimina el producto de la lista de productos de la tienda mediante el id (supón que el id es el índice del producto en la lista) e imprime su información.
# inflación(self, porcentaje_aumento): aumenta el precio de cada producto por el porcentaje_aumento dado (¡usa el método que escribiste en la clase Producto!)
# hacer_liquidación(self, category, porcentaje_descuento): actualiza todos los productos que coinciden con la categoría dada al reducir el precio por el porcentaje_descuento dado (¡usa el método que escribiste en la clase Producto!) 
# Crea una clase de tienda con 2 atributos

# Crea una clase de producto con 3 atributos

# Agrega el método print_info a la clase Producto

# Agrega el método actualizar_precio a la clase Producto

# Agrega un método agregar_producto a la clase Tienda

# Agrega un método vender_producto a la clase Tienda

# Prueba tus clases creando una instancia de Tienda y algunas instancias de la clase Producto. Agrega esas instancias a la instancia de tienda y luego prueba los métodos.

# BONUS NINJA: Agrega el método inflación a la clase Tienda

# BONUS NINJA: Agrega el método hacer_liquidación a la clase Tienda

# BONUS NINJA: Modulariza tu código en 3 archivos separados

# BONUS SENSEI: Actualiza la clase de producto para dar a cada producto un id único. Actualiza el método vender_producto para aceptar el id único.