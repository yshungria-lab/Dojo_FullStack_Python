import padre

# # Antes de escribir cualquier otra cosa, ejecuta hijo.py. Comprueba lo que hay en tu directorio. ¿Qué cambió? Deberías ver un directorio llamado __pychache__ que contiene un archivo .pyc. Este archivo contiene el bytecode de Python; el idioma que habla el intérprete de Python. Dado que estos archivos están en un lenguaje que Python conoce, podemos ejecutarlos como cualquier otro archivo de Python: (por ejemplo, __pycache __ /padre.cpython-36.pyc).

# Una forma en que se crearán estos archivos .pyc es cuando se importa un módulo. Es por eso que es posible que no hayas visto archivos .pyc antes. Una vez que se genera un archivo .pyc, siempre y cuando no cambiemos ese archivo, Python no tendrá que volver a compilar tu código en bytecode, lo que puede ahorrar tiempo de procesamiento cuando se trabaja con bases de código grandes.

# Probablemente también hayas notado que todo tu código de padre.py se ejecutó en la sentencia import. Esto significa que cada sentencia print e instanciación de variable todavía está sucediendo. Eso está bien, pero usemos un concepto llamado namespace y una variable integrada llamada __name__ para limpiar nuestro código.

# Namespace:

# El espacio de nombres se refiere a las variables, funciones y clases a las que podemos acceder en cualquier momento durante la ejecución de un programa. Namespace es importante porque tenemos que saber a qué variables tenemos acceso. Para ver qué variables están disponibles en un lugar determinado, agrega la línea print(locals()) y ve qué variables están en tu espacio de nombres actual. El objeto que se imprime será un diccionario donde los nombres de las variables son claves y los objetos a los que hacen referencia son los valores. Comprender namespace te ayudará a comprender la siguiente parte, donde usaremos el espacio de nombres para controlar la funcionalidad que se importa con nuestro documento.

# print(locals())
print(__name__)