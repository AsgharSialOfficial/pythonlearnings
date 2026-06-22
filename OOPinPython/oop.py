
class myshoes:
    def __init__(self, color):
        self.brand = 'nike'
        self.size = 23
        self.color = color
    
    def walking(self):
        return 'I am walking with shoes'



asgharshoes = myshoes('red')

print(f'my shoes brand is',asgharshoes.brand, 'size is', asgharshoes.size, 'shoes color is', asgharshoes.color)
print(asgharshoes.walking())



class Asghar:
    pass
asghar = Asghar()

print(asghar)
asghar.name = 'asgharbhi'
print(asghar.name)
safdar = Asghar()
safdar.name = 'asghar ali'

print(safdar.name)


class asgharsaab:
    def __init__(self, name,fname):
        self.name = name
        self.fname = fname
    
bhisaab = asgharsaab('asghar','alisher')

bhisaab.name = 'asghar ali'

print(bhisaab.name)
print(bhisaab.fname)
 



class asgharinfo:
    def __init__(self):
       name = 'Asghar Ali' 
       age = 26
       Degree = 'BSIT'
       Skills = 'Programming', 'Coding'
    def intro(self):
        return (f'I am {self.name}, my age is {self.age} and i have degree in {self.Degree} with skills {self.Skills}')




asgharsaab = asgharinfo()
asgharsaab.name = 'Safdar'
del asgharsaab.name
asgharsaab.name = 'Safdar'
asgharsaab.age = 23
asgharsaab.Degree = 'BBIT',
asgharsaab.Skills = ['coding', 'programming', 'web scraping']

print(asgharsaab.intro())



print(asgharinfo.intro(asgharsaab))



class car:
    def __init__(self, name, brand, model, price, color):
        self.name = name
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
    def info(self):
        return (f'{self.name} car is {self.model} model, brand is {self.brand}, colors is {self.color} and price is {self.price}')
    


carolla = car(name='crolla Xli', brand='toyota',model='2009', price=2000000, color='black' )
print(carolla.info())




class vehical:
    def __init__(self, name):
        self.name = name



    def start(self):
        print(f'{self.name} started')
    def end(self):
        print(f'{self.name} ended')

class car(vehical):
    def __init__(self,name, model):
        super().__init__(name)
        self.model = model
    
    def start(self):
        print(f'{self.name} started')


mycar = car('crolla', 'XLI')


print(mycar.start())



class jnicar:
    def __init__(self):
        self.carbhi = car('Honda Campry', '2009')

 



asgharjnicar = jnicar()

print(asgharjnicar.carbhi.start())




class A:
    name = 'Class A'
class B(A):
    name = 'Class B'
class C(A):
    name = 'Class C'

class D(B,C):
    pass

classD = D()
print(classD.name)

# This is the stais method inside a class, we do not need self for that.
class AsgharOkara:
    

    @staticmethod
    def intro ():
        return ('I am asghar')


    
    
asgharokaraintro = AsgharOkara.intro()
print(asgharokaraintro)




class SafdarOkara:
    def __init__(self, name, age, fathername, degree):
        self.name = name
        self.age = age
        self.fathername = fathername
        self.degree = degree
    @classmethod
    def fromdic(cls, dicbhi):
        return cls(
            dicbhi['name'],
            dicbhi['age'],
            dicbhi['fathername'],
            dicbhi['degree']
        )
    @classmethod
    def fromstring(cls, mystr):
        name, age, fathername, degree = mystr.split(',')
        return cls(name, age, fathername,degree)

SAFDAR1= SafdarOkara.fromdic({"name":'Asghar', 'age':26, 'fathername':'Ali Sher', 'degree':'BSIT'})
print(SAFDAR1.name)
print(SAFDAR1.fathername)
print(SAFDAR1.degree)

SAFDAR2 = SafdarOkara.fromstring('asghar,26,Ali Sher, BSIT')

print(SAFDAR2.name)




class Alisher:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age*2
    @age.setter
    def age(self, newage):
        if newage<=100 and newage>=1:
            self._age = newage
        else:
           raise  ValueError ('Invalid value')


asgharalisher = Alisher(26)

print(asgharalisher.age)
result = asgharalisher.age = 90
print(result)
print(asgharalisher.age)


