
class Library:
    def __init__(self):
        self.book = []
        self.member = []
    def listbooks(self):
        books = []
        for book in self.book:
            books.append({"id":book.id ,"name":book.name ,"author":book.author})
        return books
    def isbookavailable(self, Book):
        if Book.isAvailable:
            return 'Yes , It is available'
        else:
            'No, Book is not available'
    def addbook(self,book):
        if book not in self.book:
            self.book.append(book)
            return 'Book has been added to the library'
        else:
            return 'This Books already Exist'
    def searchbook(self, name):
        found = False
        for eachook in self.book:
            if eachook.name == name:
                print(f'Name: {eachook.name} \n Author:{eachook.author} \n ID: {eachook.id}')
                found = True
        if not found:
            print('Book is not available')
    def deletebook(self, bookid):
        for book in self.book:
            if book.id ==bookid:
                self.book.remove(book)
                print('Books has been removed')
                break
        
    def register(self, Member):
        if Member not in self.member:
            self.member.append(Member)
            print(f'You have been registered with libbrary. \n Now you are borrow books.')
        else:
            print('You are already regisrered with Library')

        
    def borrowbook(self, bookid, member):
        if not member in self.member:
            print(f'you are not registered with library so thats why you cannot borrow books \n First register yourself with library✔')
        
        else:
            for eachbook in self.book:
                if eachbook.id == bookid and eachbook.isAvailable ==True:
                    member.borrowedbooks.append(eachbook)
                    eachbook.isAvailable = False
                    print(f'You have borroed {eachbook.name}')
                    break
    def returnbook(self, bookid, member):
        if member not in self.member:
            print(f'you are not registered with library. Get you self registered first')
        else:
            for eachbook in self.book:
                if eachbook.id == bookid:
                    eachbook.isAvailable ==True
                    member.borrowedbooks.remove(eachbook)
                    print('Ok, your book return is sucessfully ssubmitted!')
                    break

    

class Book:
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.isAvailable = True

class Member:
    def __init__(self, name, age, address, phone, city):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.city = city
        self.borrowedbooks = []  



asgharlibrary = Library()
listofbooks = asgharlibrary.listbooks()
print(listofbooks)





addmessage = asgharlibrary.addbook(Book(1,'OOP by Asghar', 'Muhammad Asghar'))
print(addmessage)

print(asgharlibrary.listbooks())

addmessage = asgharlibrary.addbook(Book(1,'OOP by Asghar', 'Muhammad Asghar'))
print(addmessage)