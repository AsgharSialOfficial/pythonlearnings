class User:
    def __init__(self,name, age,location):
        self.name = name
        self.age = age
        self.location = location
        self.__salary = 0
    @property
    def salary(self):
        return self.__salary
         
    @salary.setter
    def salary(self, newsalary:float):
        self.__salary = newsalary
    


Asghar = User('Asghar',26,'Okara')
print(Asghar.salary)
Asghar.salary=150000
print(Asghar.salary)
