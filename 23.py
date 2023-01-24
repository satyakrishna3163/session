#How would you create a class in Python that represents a bank account, with methods for depositing and withdrawing money, as well as returning the account balance

class Bank_Account:
    def __init__(self):
        self.balance=0
        print("welcome atm machine")
 
    def deposit(self):
        amount=float(input("Enter amount: "))
        self.balance += amount
        print("Amount Deposit:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("You Withdrawl:", amount)
        else:
            print("Insufficient balance")
 
    def display(self):
        print("Available Balance=",self.balance)
s = Bank_Account()
s.deposit()
s.withdraw()
s.display()