class Account:
    def __init__(self,title=None, balance=0):
        self.title=title
        self.balance=balance

    def getBalance(self):
        return self.balance
    

    def deposit(self, amount):
        self.balance=amount+self.balance

    def withdrawal(self, amount):
        self.balance=self.balance-amount


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate= interestRate
    
    def interestAmount(self):
        return ((self.interestRate*self.balance)/100) 


obj = Account('a',2000)
print(obj.getBalance())
obj.deposit(500)
print(obj.getBalance())
obj.withdrawal(500)
print(obj.getBalance())
obj2 = SavingsAccount('b',2000,5)
print (obj2.interestAmount())
