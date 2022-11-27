# 1. Mientras seguimos pensando en nuestra aplicación bancaria, nos damos cuenta de que sería más preciso asignar un balance no al usuario directamente, sino que en el mundo real. Los usuarios tienen cuentas y las cuentas tienen balances. ¡Esto nos da la idea de que quizás una cuenta sea su propia clase! Pero como dijimos, no es completamente independiente de una clase; las cuentas solo existen porque los usuarios las abren.

# Para esta tarea, no te preocupes por poner información de usuario en la clase CuentaBancaria. ¡Nos ocuparemos de eso en la próxima lección!

# Primero, practiquemos un poco más la escritura de clases escribiendo una clase nueva CuentaBancaria.

# La clase CuentaBancaria debe tener un balance. Cuando se crea una nueva instancia de CuentaBancaria, si se da un monto, el balance de la cuenta debe establecerse inicialmente en ese monto; de lo contrario, el balance debe comenzar en $0. La cuenta también debe tener una tasa de interés, guardada como decimal (es decir, 1% se guardaría como 0,01), que debe proporcionarse al crear la instancia. (Sugerencia: cuando se utilizan valores predeterminados en los parámetros, ¡el orden de los parámetros es importante!).

# Utiliza un método de clase para imprimir todas las instancias de la información de una cuenta bancaria

class bank_account:
    all_accounts = []
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        bank_account.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def print_all_accounts(cls):
        sum = 0
        for account in cls.all_accounts:
            print(f"Balance de cuenta Numero {cls.all_accounts.index(account)+1}: ${account.balance}")
        sum += account.balance
        print(f"La suma total de los balances de las cuentas es: ${sum}")


# Crea 2 instancias de la clase CuentaBancaria

cuenta1 = bank_account(0.01)
cuenta2 = bank_account(0.01)

cuenta1.deposit(100).deposit(200).deposit(300).withdraw(50).yield_interest().display_account_info()

cuenta2.deposit(200).deposit(300).withdraw(50).withdraw(20).withdraw(30).withdraw(20).yield_interest().display_account_info()

bank_account.print_all_accounts()


