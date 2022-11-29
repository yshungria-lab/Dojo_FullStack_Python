# Crea una clase de Python llamada MathDojo que tenga un atributo, resultado y 2 métodos: sumar y restar. Cada uno de los 2 métodos debe tomar al menos 1 parámetro, pero pueden tomar muchos más.

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)

#------------------------------------#
### ADDING NUMBERS ###
suma1 = md.add(2, 4, 6).result  # should give 12
print(suma1)
suma2 = md.add(2, 5, 6).result  # should give 13
print(suma2)
suma3 = md.add(2, 6, 6).result  # should give 14
print(suma3)
print("-----------------------------------------")
### SUBSTRACTING NUMBERS ###
resta1 = md.subtract(2, 4, 6).result       # should give -12
print(resta1)
resta2 = md.subtract(2, 5, 6).result       # should give -13
print(resta2)
resta3 = md.subtract(2, 6, 6).result       # should give -14
print(resta3)
print("-----------------------------------------")
### ENCHAINMENT NUMBERS ###
encadenamiento1 = md.add(2, 4, 6).subtract(2, 5, 6).result
print(encadenamiento1)
print("-----------------------------------------")