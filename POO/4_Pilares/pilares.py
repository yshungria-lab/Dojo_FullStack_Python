# 1. Encapsulamiento
# La encapsulación es la idea de que podemos agrupar el código en objetos; de ahí la Programación Orientada a Objetos. Usamos clases o "blueprints” para definir qué son nuestros objetos y cómo se comportan. Encapsulamos atributos y métodos en nuestra clase.

class CaféM:
    def __init__(self,name):
        self.name = name
        self.temp_agua = 200
    def preparar_ahora(self,granos):
        print(f"Utilizando {granos}!")
        print("¡Preparar ahora, vaca café!")
    def limpiar(self):
        print("¡Limpiando!")



# 2. Herencia
# La herencia es la idea de que pasamos atributos y métodos de una clase a una "subclase" o clase hija, y no tenemos que volver a escribir el código para que funcione. Las clases hijas pueden ser versiones más específicas de la clase padre. El uso de la palabra clave “super” llamará los métodos

class CappuccinoM( CaféM ):
    def __init__(self,name):
        super().__init__(name)
        self.leche = "entera"
    def hacer_cappuccino(self,granos):
        super().preparar_ahora(granos)
        print("¡Espumoso!")

# 3. Polimorfismo
# Polimorfismo significa “muchas formas”, y la idea en POO es que una clase hija pueda tener una versión diferente de un método que la clase padre. En este ejemplo, la clase hija CappuccinoM tiene un método limpiar al igual que CaféM. Dependiendo de la clase, el método limpiar hará diferentes cosas.

# EJEMPLO:

class CappuccinoM( CaféM ):
    def __init__(self,name):
        super().__init__(name)
        self.leche = "entera"
    def hacer_cappuccino(self,granos):
        super().preparar_ahora(granos)
        print("¡Espumoso!")
    def limpiar(self):
        print("¡Limpiando la espuma")
# copy
# 4. Abstracción
# La abstracción es una extensión de la encapsulación y podemos ocultar atributos o métodos que un barista no necesita conocer, como un CaféM. De esa manera, el barista puede preparar una taza de café de una manera más sencilla.


class Barista:
    def __init__(self,name):
        self.name = name
        self.café = CaféM("Café")
    def hacer_café(self, granos):
        self.café.preparar_ahora(granos)

