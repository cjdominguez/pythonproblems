class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return(self.balance)

    def deposit(self,amount):
        self.balance = amount+self.balance

    def withdrawl(self,amount):
        self.balance = self.balance - amount

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        self.interestRate = interestRate
        super().__init__(title,balance)

    def interestAccount(self):
        return((self.interestRate * self.balance) / 100)



customer = SavingsAccount('mark', 1000, 5)
print(customer.title)
print(customer.balance)
print(customer.interestRate)
