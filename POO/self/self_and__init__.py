# Atributos
# Objetivos
# Aprender sobre los atributos de instancia vs. atributos de clase
# Familiarizarse con el método __init __()


# Atributos de instancia
# Construyamos una aplicación bancaria con Usuarios. Queremos que un Usuario tenga nombre, email y saldo de cuenta.

# Los atributos de instancia se definen en un "método mágico" llamado __init__, que se llama cuando se crea una instancia de un nuevo objeto

# declarar una clase y darle el nombre Usuario
class Usuario:
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0

# El primer parámetro de un método de instancia dentro de una clase será self, y los atributos de instancia también se indican por
# self.

# self es una referencia a la instancia, no a la clase.

# Ahora podemos crear instancias de Usuario

Usuario()
guido = Usuario()
monty = Usuario()
# Accediendo a los atributos de la instancia
print(guido.name)	# salida: Michael
print(monty.name)	# salida: Michael
# copy
# También podemos establecer los valores para los atributos de nuestra instancia:

guido.name = "Guido"
print(guido.name) # salida: Guido
monty.name = "Monty"
print(monty.name) # salida: Monty

# Atributos de clase
# Los atributos de clase se definen fuera de cualquier método de instancia y se comparten entre todas las instancias de la clase. 

class User:
    # declarando un atributo de clase
    nombre_banco = "Primer Dojo Nacional"
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0
# copy
# Los atributos de clase son más flexibles porque podemos cambiarlos en una instancia o en toda la clase. 

# Cambiarlos en una instancia:

guido = Usuario()
monty = Usuario()
guido.nombre_banco = "Dojo Credit Union"
print(guido.bank_name) # salida: Dojo Credit Union
print(monty.bank_name) # salida: Primer Dojo Nacionalcopy
# Cambiarlos en toda la clase:

User.bank_name = "Banco del Dojo"
print(guido.nombre_banco) # salida: Banco del Dojo
print(monty.nombre_banco) # salida: Banco del Dojo

# Pasar argumentos
# Si bien definitivamente queremos que cada usuario tenga un nombre, correo electrónico y balance de cuenta, no queremos que todos nuestros usuarios tengan el mismo nombre y dirección de correo electrónico al momento de la creación. ¿Cómo sabremos cuál debería ser el nombre? Ahora vamos a pasar argumentos al método__init__ para especificar los atributos de instancia de un usuario.

# En nuestro ejemplo, aunque tenemos 3 atributos de instancia, solo requerimos entrada para 2 de ellos. Cuando se crea la instancia Usuario, deberíamos esperar recibir valores específicos para el nombre y la dirección de correo electrónico. Sin embargo, asumiremos que todos comienzan con $0 en su cuenta. Ajustemos nuestro código para permitir que los argumentos se pasen al crear una instancia:

class Usuario:
# los atributos de clase se definen en la clase
    nombre_banco = "Primer Dojo Nacional"
# ¡ahora nuestro método tiene 2 parámetros!
    def __init__(self , name, email_address):
        # los asignamos en consecuencia
        self.name = name
        self.email = email_address
        # el balance de la cuenta se establece en $0
        self.balance_cuenta = 0
guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
print(guido.name)	# salida: Guido van Rossum
print(monty.name)	# salida: Monty Python

# Self

# Probablemente sea hora de hablar sobre self. El parámetro self incluye toda la información sobre el objeto individual que ha llamado al método. Pero, ¿cómo se transmite? Según la firma del método de depósito o el método __init__, requieren 2 y 3 argumentos, respectivamente. Sin embargo, cuando los llamamos, pasamos solo 1 y 2. ¿Qué está pasando aquí? Debido a que estamos invocando el método desde la instancia, esto se conoce como paso implícito de self. Cuando invocamos un método desde una instancia, esa instancia, junto con toda su información (nombre, email, balance), se pasa como self.