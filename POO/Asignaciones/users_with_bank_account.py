"""
How to call another classes from another files:

from user import User
from bank_account import Bankaccount

"""


class Bank_account:
    all_accounts = []
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        Bank_account.all_accounts.append(self)

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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Bank_account(int_rate=0.02, balance=0)

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount)	# the specific user's account increases by the amount of the value received
        return self

    def make_withdrawal(self, amount):	# takes an argument that is the amount of the withdrawal
        self.account.withdraw(amount)	# the specific user's account decreases by the amount of the value received
        return self

    def display_user_balance(self):	# print the user's name and account balance to the terminal
        print(f"{self.name}, tiene balance de ${self.account.balance} en su cuenta")
        return self

    def transfer_money(self, other_user, amount):	# takes two arguments: the other user's object and the amount
        self.account.balance -= amount
        other_user.account.balance += amount
        print(f"{self.name}, tiene balance de ${self.account.balance} en su cuenta")
        print(f"{other_user.name}, tiene balance de ${other_user.account.balance} en su cuenta")
        return self


Elon = User("Elon Musk", "elonmusk234@python.com")
Bezos = User("Jeff Bezos", "jeffbezos234@python.com")

Elon.display_user_balance()
Elon.make_deposit(1000).make_deposit(2000).make_deposit(3000).make_withdrawal(5000).display_user_balance()

Bezos.display_user_balance()
Bezos.make_deposit(1000).make_deposit(2000).make_withdrawal(500).make_withdrawal(500).display_user_balance()

Bezos.transfer_money(Elon, 500)

# permite que un usuario tenga varias cuentas; actualiza métodos para que el usuario tenga que especificar en qué cuenta está retirando o hacia cuál están depositando

