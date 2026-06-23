from abc import ABC, abstractmethod
class PaymentManager(ABC):
    @abstractmethod
    def sendpayment(self):
        pass
    @abstractmethod
    def recievepayment(self):
        pass

class JazzCash(PaymentManager):
    def __init__(self):
        self.name = 'JazzCash'
    def sendpayment(self, person, amount):
        return (f'you sent {person}- {amount}PKR')
    def recievepayment(self,person,amount):
        return (f'you revieved {amount} from {person}')
        
        

jazzpayment= JazzCash()
print(jazzpayment.sendpayment('Safdar', 100000))