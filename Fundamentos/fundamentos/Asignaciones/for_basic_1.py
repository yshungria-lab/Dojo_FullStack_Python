# 1. Básico: imprime todos los números enteros del 0 al 150.

for x in range(151):
    print(x)


# 2. Múltiplos de cinco: imprime todos los múltiplos de 5 de 5 a 1,000
for x in range(5, 1001, 5):
    print(x)

# 3. Contar, no imprimir: imprime los enteros del 1 al 100. Si es divisible por 5, imprime "Coding" en su lugar.
# Si es divisible por 10, imprime "Coding Dojo".

for x in range(1, 101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)


# 4. Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.

suma_imp = 0
for x in range(0, 500001, 1):
    if(x % 2 != 0):
        ## IMPAR ##
        # print("Numero impar: ", x)
        suma_imp += x
print("Suma total enteros impares: ", suma_imp)

# 5.Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.

"""
for x in range(2018, 0, -4):
    print(x)
"""
for x in range(2018, 0, -4):
    print("Cuenta regresiva: {}".format(x))

# 6.Contador flexible: establece tres variables: lowNum, highNum, mult.
# Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult.
# Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas).

input_lowNum = int(input("Ingresa el numero menor: "))
input_highNum = int(input("Ingresa el numero mayor: "))
input_mult = int(input("Ingresa el numero multiplo: "))
for x in range(input_lowNum, input_highNum+1, 1):
    if x % input_mult == 0:
        print(x)

if not x:
    print("No hay numeros multiplos")