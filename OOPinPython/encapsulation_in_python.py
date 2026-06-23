class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    
    def checkbalance(self):
        return self.__balance
    def withdraw(self, amount):
        if self.__balance>=amount:
            self.__balance = self.__balance-amount
            return(f'you withdrawed {amount}PKR. Remaining Balance {self.__balance}')
        else:
            return (f'you have insufficient balance. your current balance is {self.__balance}')
    def deposit(self,amount):
        self.__balance+amount
        return (f'you sucesfuly deposited amount into your bank account. Current Balance is {self.__balance}')


asgharBankAccount = Bank('Asghar', 2000)

print(asgharBankAccount.checkbalance())
print(asgharBankAccount.withdraw(1800))
print(asgharBankAccount.withdraw(1000))