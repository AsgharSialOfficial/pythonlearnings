class BankAccount:
    def __init__(self, account_number:str, pin:int, balance:float):
        ''' There are some limitations in this program, I am using encapsulation and balance protection. Which you can do by _balance'''
        self.account_number = account_number
        self.pin = pin
        self.balance = balance 
    def checkbalance(self):
        return self.balance
    def deposit(self, amount:float):
        if amount>0:
            self.balance = self.balance + amount
            return (f'{amount}PKR has been deposited in your bank account\n New Balance is {self.balance}')
        else:
            raise Exception('Invalid Amount')
    def withdraw(self, amount:float):
        if amount<=self.balance and amount>0:
            self.balance=self.balance - amount
            return (f'{amount} has been deducted with from you account. Current balance is {self.balance}')
        else:
            raise Exception('Insufficent Account Balance')
class ATM:
    def __init__(self):
        self.registered_accounts = {}
    def register_account(self, account:BankAccount):
        self.registered_accounts[account.account_number] = account
    def authenticate(self,account_number, pin):
         account = self.registered_accounts.get(account_number)
         if pin == account.pin:
             print('Login Successful!.')
             return account
         else:
             raise Exception('Invalid PIN')
    @staticmethod
    def display_option():
        
        print('1.Check Balance')
        print('2.Withdraw Balance')
        print('3.Deposit Balance')
        print('Exit')
    
asgharaccount = BankAccount('1',1221,60000)
asgharaccountatm = ATM()
asgharaccountatm.register_account(asgharaccount)



accountnumber = input('Enter your account number')
accountpin = int(input('Enter your account pin'))
asgharbankaccount:BankAccount = asgharaccountatm.authenticate(accountnumber,accountpin)
while asgharbankaccount:
    asgharaccountatm.display_option()
    choice= input('Enter your choice')
    match choice:
         case "1":
            useraccountbalance = asgharbankaccount.checkbalance()
            print(f'your account balance is {useraccountbalance}')
         case '2':
            amount = float(input('Enter amount you want to withdraw'))
            finalmessage = asgharbankaccount.withdraw(amount)
            print(finalmessage)
         case '3':
            amount = float(input('Enter amount you want to deposit '))
            finalmessage =asgharbankaccount.deposit(amount)
            print(finalmessage)
         case '4':
            break
         case __:
            print('Invalid Input Choice')





