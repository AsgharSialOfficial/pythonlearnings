# List Comprehesion
myhobbies = ['coding', 'programming', 'web scraping', 'data scince','ML']
filterhobbies = [hobby for hobby in myhobbies if hobby.endswith('ing')]

print(filterhobbies)


mysubjects = {'biology', 'chemistry', 'math','AI Development'}

newmysubjects = {subject for subject in mysubjects if subject =='math'}
print(newmysubjects)

# Set comprehensions

mydetails = {
    'hobiies':['web scraping', 'coding', 'web development', 'python'],
    'subjects':['python','AI Agents', 'LLMs']
}

mynewdetails = {subject for subjects in mydetails.values() for subject in subjects}

print(mynewdetails)



# Dictionaries Comprehension in Python

asghardetails ={
    'name':'asghar',
    'age':26,
    'degree':'BSIT',
    'address':{
        'street':'fareed town, okara',
    },
}

asgharnewdetails = {key: value for key,value in asghardetails.items()}
print(asgharnewdetails)



numberlist = [1,2,3,4,5]
sqrtnumber = [x**x for x in numberlist]
print(sqrtnumber)


mixednumber = [1,1,2,3,2,4,5,4,6,7,7,8,9]
uniqueset = {number for number in mixednumber}

print(uniqueset)


generators = sum((x for x in mixednumber))

print(generators)