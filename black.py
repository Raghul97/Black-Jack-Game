class Account:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(' Amount successfully deposited')
        return self.balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance - amount
            print(' Amount successfully withdrawn')
        else:
            print(' Insufficient Balance ')
        return self.balance
