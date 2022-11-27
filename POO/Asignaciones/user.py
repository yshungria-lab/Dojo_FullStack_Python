class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self

    def make_withdrawal(self, amount):	# takes an argument that is the amount of the withdrawal
        self.account_balance -= amount	# the specific user's account decreases by the amount of the value received
        return self

    def display_user_balance(self):	# print the user's name and account balance to the terminal
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):	# takes two arguments: the other user's object and the amount
        self.account_balance -= amount	# the specific user's account decreases by the amount of the value received
        other_user.account_balance += amount # the other user's account increases by the amount of the value received
        return self
Guido = User("Guido van Rossum", "guido@gmail.com")
# Guido.make_deposit(1000)
# Guido.make_deposit(2000)
# Guido.make_deposit(3000)
# Guido.make_withdrawal(5000)
# Guido.display_user_balance()
Guido.make_deposit(1000).make_deposit(2000).make_deposit(3000).make_withdrawal(5000).display_user_balance()

Yojan = User("Yojan", "yshungria@hotmail.com")
# Yojan.make_deposit(1000)
# Yojan.make_deposit(2000)
# Yojan.make_withdrawal(500)
# Yojan.make_withdrawal(500)
# Yojan.display_user_balance()
Yojan.make_deposit(1000).make_deposit(2000).make_withdrawal(500).make_withdrawal(500).display_user_balance()

Ingrith = User("Ingrith", "ingrith@gmail.com")
# Ingrith.make_deposit(5000)
# Ingrith.make_withdrawal(1000)
# Ingrith.make_withdrawal(500)
# Ingrith.make_withdrawal(500)
# Ingrith.display_user_balance()
Ingrith.make_deposit(5000).make_withdrawal(1000).make_withdrawal(500).make_withdrawal(500).display_user_balance()
Guido.transfer_money(Ingrith, 1000)
Ingrith.display_user_balance()




