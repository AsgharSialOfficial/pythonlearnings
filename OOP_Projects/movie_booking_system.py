class Movie:
    def __init__(self, name:str, price:float,totalseats:int,bookedseats:int):
        self.name = name
        self.price = price
        self.totalseats = totalseats
        self.bookedseats = bookedseats
    
    def book_ticket(self, no_of_tickets):
        if self.bookedseats ==self.totalseats:
            return 'No Seats!.All Seats Booked'
        else:
            totalprice = self.price * no_of_tickets
            self.bookedseats+=no_of_tickets
            return (f'you have to pay {totalprice}, your seats bas been booked')
    def show_status(self):
        return (f'Movie Name:{self.name}\n Movie Price: {self.price}PKR\n Total Seats:{self.totalseats}\n Booked Seats:{self.bookedseats}')
    

    
m1 = Movie('Diljalee',250.0,100,0)
print(m1.show_status())
print(m1.book_ticket(85))
print(m1.show_status())
print(m1.book_ticket(15))
print(m1.show_status())
print(m1.book_ticket(1))