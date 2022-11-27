#  Anulación y polimorfismo

# Anulación y polimorfismo
# Objetivos
# ¿Cómo pueden las clases hijas (o secundarias) anular los métodos de la clase principal (padre)?
# ¿Qué es el polimorfismo en el contexto de la programación orientada a objetos y cuándo sería útil?

# Anulación
# Hablemos de otras características interesantes de la programación orientada a objetos. A veces, el problema con la herencia implícita es que quieres que el hijo se comporte de manera completamente diferente al padre. En estos casos, quieres anular la función, reemplazando efectivamente la funcionalidad. Para hacer esto, simplemente define una función con el mismo nombre en la clase secundaria. Un ejemplo:

class Padre:
    def method_a(self):
        print("invocando método_a PADRE")


class Hijo(Padre):
    def method_a(self):
        print("invocando método_a HIJO")


papá = Padre()
hijo = Hijo()
papá.method_a()
hijo.method_a()  # Nota que esto anula el método Padre

# En este ejemplo, tenemos una función llamada método_a() en ambas clases, así que veamos qué sucede cuando la ejecutas.

# invocando método_a PADRE
# invocando método_a HIJO

# Como puedes ver, cuando invocamos papá.método_a(), ejecuta la clase Padre método_a() porque esa variable (papá) es una instancia de la clase Padre. Sin embargo, cuando invocamos hijo.método_a(), ejecuta la clase Hijo método_a() porque esa variable hijo es una instancia de la clase Hijo. Hijo anula este método del padre definiendo su propia versión.

# Polimorfismo

# El comportamiento polimórfico nos permite especificar métodos comunes en un nivel "abstracto" e implementarlos en instancias particulares. Es el proceso de utilizar un operador o función de diferentes formas para diferentes entradas de datos.


# utilizaremos la clase Persona para demostrar polimorfismo
# en el que varias clases heredan de la misma clase pero se comportan de diferentes maneras
class Persona:
  def pagar_cuenta(self):
      raise NotImplementedError
# Millonario hereda de Persona
class Millonario(Persona):
  def pagar_cuenta(self):
      print("Aquí tienes. Quédate con el cambio.")
# Estudiante de posgrado también hereda de la clase Persona
class EstudiantePosgrado(Persona):
  def pagar_cuenta(self):
      print("¿Puedo deberle diez dólares o lavar los platos?")

# Según este ejemplo, un millonario y un estudiante de posgrado son Personas. Sin embargo, cuando se trata de pagar una cuenta, la forma en que actúan es bastante diferente. Este patrón es útil cuando sabes que cada subclase de una clase principal debe definir un comportamiento específico en un método y no quieres definir un comportamiento predeterminado en la clase principal (de ahí la implementación virtual pura en la principal).