# Métodos de clase y estáticos

# Objetivos:

# Comprender la diferencia entre métodos de clase y estáticos
# Saber cuándo usar métodos de clase y estáticos

# Normalmente, cuando creamos un método en una clase, pasamos self para referirnos a la instancia del objeto. Estos métodos normales se denominan métodos de instancia. Pero hay otros tipos de métodos que podemos implementar en la clase. Métodos que pertenecen a la clase y no a la instancia.

# @classmethod
# Los métodos de clase se definen con un decorador @classmethod. Pertenecen a la propia clase en lugar de a la instancia. En lugar de pasar implícitamente self al método, pasamos cls. Esta es una referencia a la clase.

# Así es como escribimos @classmethods:

class CuentaBancaria:
    # atributo de clase
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []
    def __init__(self, int_rate, balance):
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

# método de clase para cambiar el nombre del banco
    @classmethod
    def cambiar_nombre_banco(cls, name):
    cls.nombre_banco = name
# método de clase para obtener balance de todas las cuentas
    @classmethod
    def todos_los_balances(cls):
        sum = 0
        # utilizamos cls para referirnos a la clase
        for account in cls.todas_las_cuentas:
            sum += balance.cuenta
        return sum

# Es importante saber que los métodos de clase no tienen acceso al atributo de instancia ni a ningún atributo que comience con self.

# @staticmethod
# Los métodos estáticos son funciones definidas dentro de la clase con un decorador @staticmethod. No tienen acceso a atributos de instancia o clase, por lo que sí necesitamos pasarles argumentos.

# Si quisiéramos que nuestra clase CuentaBancaria tuviera una función de utilidad para sumar o restar, podríamos implementar @staticmethod en la clase.

class CuentaBancaria:
# ... __init__ va aquí
    def re_tiro(self,amount):
# podemos usar el método estático aquí para evaluar
# si podemos retirar los fondos sin quedar con balance negativo
        if CuentaBancaria.puede_retirar(self.balance,amount):
            self.balance -= amount
        else:
            print("Fondos insuficientes")
        return self
# los métodos estáticos no tienen acceso a ningún atributo
# solo a lo que se le pasa
    @staticmethod
    def puede_retirar(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

# No hay un propósito real para los métodos estáticos en Python, pero nos ofrecen una forma de organizar nuestro código de una mejor manera. Podríamos verificar de manera simple si se puede retirar dinero de la cuenta, pero ¿qué pasa si queremos ampliar nuestra aplicación con más lógica en torno a esta idea? Tendríamos que actualizar todos los lugares donde estamos haciendo esa evaluación, pero si lo ponemos en un @staticmethod, podemos actualizar todas las comprobaciones desde un solo lugar. Y nuestro código se vuelve un poco más D.R.Y.