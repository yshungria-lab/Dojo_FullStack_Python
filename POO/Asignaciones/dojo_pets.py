# class Ninja:
#     # implementar __init__( nombre, apellido, premios, comida_mascota, mascota )
# # implementa los siguientes métodos:
# # caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
# # alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
# # bañar(): limpia la mascota del ninja invocando el método de mascota sonido()copy


class Ninja:
    def __init__(self, first_name, last_name, pet, reward, prefer_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.reward = reward
        self.prefer_food = prefer_food

    def walk(self):
       self.pet.play()
       return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self


# class Mascota:
#     # implementa __init__( name , tipo , golosinas ):
#     # implementa los siguientes métodos:
#     # dormir() - incrementa la energía de la mascota en 25
#     # comer() - incrementa la energía de la mascota en 5 y la salud en 10
#     # jugar() - incrementa la salud de la mascota en 5
#     # ruido() - imprime el sonido que produce la mascota

class Pet:
    def __init__(self, name, type, treats):
        self.name = name
        self.type = type
        self.tricks = treats
        self.health = 100
        self.energy = 100

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy += 25
        return self

    def eat(self):
        print(f"{self.name} is being fed...")
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        print(f"{self.name} is being walked...")
        self.health += 5
        return self

    def noise(self):
        print("juummmm!!!")
        return self

# Crea una instancia de un Ninja y asígnale una instancia de mascota al atributo de mascota.

ninja1 = Ninja("Guido", "van Rossum", Pet("Miau", "cat", "gummies"), "1000", "Fish")

ninja1.walk()
ninja1.feed()
ninja1.bathe()

