# 1. Actualizar valores en diccionarios y listas.

x = [ [5,2,3], [10,8,9] ]


# 1. Cambiar el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x[1][0] = 15
print (x)

# 2. Cambiar el apellido del primer alumno de 'Jordan' a 'Bryant'.
students = [{'first_name':  'Michael', 'last_name' : 'Jordan'},{ 'first_name' : 'John', 'last_name' : 'Rosales'}]
sport_directory = {'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'], 'soccer' : ['Messi', 'Ronaldo', 'Rooney']}
z = [ {'x': 10, 'y': 20} ]
students[0]['last_name'] = 'Bryant'
print(students)

# 3. En el directorio sports_directory, cambie 'Messi' a 'Andres'.
sport_directory['soccer'][0] = 'Andres'
print(sport_directory)

# 4. Cambiar el valor 20 en z a 30.
z[0]['y'] = 30
print(z)

print("=============================================")

#2. Iterar a través de una lista de diccionarios.
students = [{'first_name':  'Michael', 'last_name' : 'Jordan'},{ 'first_name' : 'John', 'last_name' : 'Rosales'},{ 'first_name' : 'Mark', 'last_name' : 'Guillen'},{ 'first_name' : 'KB', 'last_name' : 'Tonel'}]

def iterateDictionary(students):
    for i in range(len(students)):
        print(f"first_name - {students[i]['first_name']}, last_name - {students[i]['last_name']}")
iterateDictionary(students)

#3. Obtener valores de una lista de diccionarios. Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:

# Michael
# John
# Mark
# KB

# Y iterateDictionary2('last_name', estudiantes) debería generar:

# Jordan
# Rosales
# Guillen
# Tonel

students = [{'first_name':  'Michael', 'last_name' : 'Jordan'},{ 'first_name' : 'John', 'last_name' : 'Rosales'},{ 'first_name' : 'Mark', 'last_name' : 'Guillen'},{ 'first_name' : 'KB', 'last_name' : 'Tonel'}]

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2('first_name', students)
print("=============================================")
iterateDictionary2('last_name', students)


#4.Iterar a través de un diccionarios con valores de lista. Crea una función printInfo(some_dict) que, dado un diccionario cuyos valores son todas listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

dojo = { 'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'], 'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for i in range(len(value)):
            print(value[i])
printInfo(dojo)



