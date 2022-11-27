# # Módulos y paquetes
# # Objetivos
# # Aprender qué es un módulo de Python
# # Aprender cómo construir y usar un módulo en nuestro código
# # Aprender qué es un paquete de Python

# Módulos
# Los módulos son simplemente archivos de Python con la extensión .py que implementan un conjunto de funciones. Los módulos se importan mediante el comando import.

# La primera vez que se carga un módulo en un script de Python en ejecución, se inicializa ejecutando el código en el módulo una vez. Si otro módulo en tu código importa el mismo módulo nuevamente, no se cargará dos veces, sino solo una vez, por lo que las variables locales dentro del módulo actúan como un "singleton", se inicializan solo una vez.

# Ahora, si queremos importar el módulo urllib.request, que nos permite solicitar datos de las URL, podemos importar el módulo de manera simple:

# importar la biblioteca
import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)

# copy
# Observa cómo usamos urllib.request como una variable para referirnos a nuestro módulo y luego llamamos a los métodos usando notación de puntos.

# Crear tus propios módulos
# Escribir tus propios módulos de Python es muy simple. Para crear un módulo, primero creamos un nuevo archivo .py con el nombre del módulo en el mismo directorio que el archivo que importará el módulo. Luego lo importamos usando el comando import y el nombre del archivo Python (sin la extensión .py)

# Por ejemplo, creemos un módulo de operaciones aritméticas:

# ejemplo_modular/aritmética.py

def sumar(x, y):
    return x + y
def multiplicar(x, y):
    return x * y
def restar(x, y):
    return x - y
# copy
# Ahora, crea otro archivo en el mismo directorio que aritmética.py llamado cálculos.py. Podemos importar el módulo aritmético a cálculos.py y ejecutar las funciones haciendo esto...

# ejemplo_modular/cálculos.py


import aritmética

print(aritmética.sumar(5, 8))
print(aritmética.restar(10, 5))
print(aritmética.multiplicar(12, 6))

# Nota: asegúrate de que el módulo y el archivo que importa el módulo estén en la misma carpeta/directorio.

# Módulos estándar (integrados)
# Python viene con una biblioteca de módulos estándar. Algunos módulos están integrados en el intérprete; estos proporcionan acceso a operaciones que no forman parte del núcleo del lenguaje pero que, sin embargo, están integradas, ya sea para eficiencia o para proporcionar acceso a las primitivas del sistema operativo, como las llamadas al sistema. El conjunto de dichos módulos es una opción de configuración que también depende de la plataforma subyacente. Por ejemplo, el módulo winreg solo se proporciona en sistemas Windows. Un módulo en particular merece una mención especial: sys, que está integrado en todos los intérpretes de Python.

# En este enlace se puede encontrar una lista de módulos integrados.

# Explorar módulos integrados
# Dos funciones muy importantes son útiles cuando se exploran módulos en Python: las funciones dir y help. Podemos buscar qué funciones se implementan en cada módulo usando la función dir:

# image.png

# Paquetes
# Un módulo es un solo archivo (o archivos) que se importa bajo una sola importación. Un paquete es una colección de módulos en directorios que dan una jerarquía de paquetes.

from mi_paquete.subdirectorio import mis_funciones

# Los paquetes son namespaces que contienen múltiples paquetes y módulos. Son simplemente directorios, pero con una pequeña diferencia.

# proyecto_ejemplo
#      |_____ archivo_python.py
#      |_____ mis_módulos
#                |_____ __init__.py
#                |_____ módulo_prueba.py
#                |_____ otro_módulo.py
#                |_____ tercer_módulo.py

# En el diagrama anterior, el nombre del paquete es mis_módulos.

# Escribir paquetes
# Si creamos un directorio llamado mis_módulos, que marca el nombre del paquete, podemos crear un módulo dentro de ese paquete llamado módulo_prueba.

# Para usar el módulo módulo_prueba, podemos importarlo de dos maneras:

import mis_módulos.módulo_prueba


from mis_módulos import módulo_pruebacopy
Archivo __init__.py


# Es posible que hayas notado el archivo __init__.py descrito en la estructura anterior y te hayas preguntado qué es. Este archivo era necesario para todos los paquetes en Python 2.7; a menudo estaría vacío, pero era necesario para indicar que los archivos en la carpeta eran parte del paquete.

# En Python 3.3+, solo necesitamos este archivo si necesitamos personalizar qué módulos están disponibles para cualquiera que intente importar el paquete. Por ejemplo, si no queremos que otro_módulo o tercer_módulo sean accesibles para importar, podríamos anular la variable __all__ , así:

proyecto_ejemplo/mis_módulos/__init__.py
__all__ = ["módulo_prueba"]

