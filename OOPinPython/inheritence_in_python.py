class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f'{self.name} is eating')
    def slepp(self):
        print(f'{self.name} is sleeping')
    def move(self):
        return(f'{self.name} is moving with 2 legs but slowly')
    
class Dog(Animal):
    def __init__(self,name,age,color):
        super().__init__(name, age)
        self.color = color
    def barking(self):
        print(f'Barking')
    '''This is classical example of polymophism, same function, behaving differently. This is achieved using Polymorphism'''
    def move(self):
        return (f'{self.name} is moving with four legs with high speed')

    

germanshephart = Dog('GermanSherpart', 20, 'BlackBrown')
print(f'{germanshephart.name} is eating. Color is {germanshephart.color} and {germanshephart.move()}')