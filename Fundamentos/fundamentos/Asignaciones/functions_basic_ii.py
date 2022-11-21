#  1. Cuenta regresiva: crea una función que acepte un número como entrada.
# Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento).
# Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0].

def countdown(num):
    lista = []
    for i in range(num, -1, -1):
        lista.append(i)
    return lista

print(countdown(5))

# 2. Imprimir y devolver: crea una función que recibirá una lista con dos números.

def count(lista):
    print(lista[0])
    return lista[1]

count([1,2])
print(count([1,2]))

# # 3.Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
# # Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)

first_plus_length = lambda lista: lista[0] + len(lista)
print(first_plus_length([1,2,3,4,5]))

# 4. Valores mayores que el segundo: escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False.
# Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4].
# Ejemplo: valores_mayores_que_el_segundo([3]) debería devolver False.

def values_greater_than_second(lista):
    if len(lista) < 2:
        return False
    else:
        new_list = []
        for i in lista:
            if i > lista[1]:
                new_list.append(i)
        print(len(new_list))
        return new_list
print(values_greater_than_second([5,2,3,2,1,4]))

# 5. Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
# Ejemplo: longitud_valor(4,7) debería devolver [7,7,7,7]
# Ejemplo: longitud_valor(6,2) debería devolver [2,2,2,2,2,2]

def length_and_value(size, value):
    lista = []
    for i in range(size):
        lista.append(value)
    return lista

print(length_and_value(4,7))
print(length_and_value(6,2))