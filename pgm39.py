#Create a Bank account with members — account number, name, type of account, and balance. Write constructor and methods to deposit at the bank and withdraw an amount from the bank.
class BankAccount:
    def __init__(self,acc_no="",name="",acc_type="",balance=0):
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance
        self.name = name

    def deposit(self,amount):
        self.balance += amount
        print(f"${amount} deposited\n................")

    def withdraw(self,amount):
        self.balance -= amount
        print(f"${amount} withdrawn\n................")

    def __str__(self):
        return f"Account Number : {self.acc_no} \nAccount Holder Name : {self.name} \nAccount Type : {self.acc_type} \nCurrent Balance : {self.balance}\n................"

user1 = BankAccount(acc_no="123",name="Alona",acc_type="savings",balance=100)
print(user1)
user1.deposit(50)
user1.withdraw(20)
print(user1)

