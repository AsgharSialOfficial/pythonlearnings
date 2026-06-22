# There are many data types, like numbers, integers, float, boolean, and complex 
#numbers .

# All mathematical  operation can be done in python, like addition, subtraction, division, and multiplication.



a = 100
b = 110

addition = a+b
subtraction = a-b
multiply = a*b
divide = a/b
floordivide = a//b

modulus = a%b

print(addition)
print(subtraction)
print(multiply)
print(divide)
print(floordivide)
print(modulus)


'''   '''

amIAvailable = True
currentPoints = 5
totalPoints = amIAvailable + currentPoints
print(totalPoints)



myheight = 17.89
myweight = 56.98

bmi = int(myheight*myweight)
print(bmi)


powermath = 2**4
print(powermath)


# So that was all about string, their indexing, sclicing, and encoding.

# Tuples in python, what are they and how it works

myhobbies = ('coding', 'programming', 'web scraping', 'web development', 'AI Agents Development')
(hobby1,hobby2, hobby3, hobby4, hoppy5 ) = myhobbies

print(f'my first hobby is : {hobby1}, second hobby is : {hobby2}, third hobby is :{hobby3}, fourth hobby is :{hobby4}')

asghar, safdar = 26,23
asghar, safdar =  safdar, asghar

print(asghar)
print(safdar)


print(f'is coding in myhobbies present : {'coding' in myhobbies}')


# So yes we have tuples, their rules, assignment



myskills = ["python", "API's","JSON", "RAG" ]

myskills.append('AI Agents')


print(myskills)

myskills.extend(['coding', 'programming'])

print(myskills)

myskills.insert(0, 'web scraping')

myskills.append('pthon programming')

myskills.append('AI Agent Developer')

print(myskills)

print(myskills)


print(myskills)
i = 1

for skill in myskills:
    
    print(f'{i}:{skill}')
    i+=1





myskills.reverse()
print(myskills)
myskills.sort()
print(myskills)


#So, yes that was all about list, list indexing, list looping, different list methods, like split, sort, reverse,
#len, replcase, append, extend, insert etc.



# Hitesh Sir, taught about operator overloading anf bytearray,but things overflow my brain , i do not have deep understanding
#about them.


# Sets in python, learn how to perform crud opertions on them loop through them.

asgharskills = {'coding', 'programming', 'web scraping'}
newasgharskills = {'web development', 'app development','web scraping', 'programming'}

allskills = asgharskills | newasgharskills

print(f'allskills are here : {allskills}')


commonskills = asgharskills & newasgharskills

print(f'commonskills are here:{commonskills}')


uniqueskills = asgharskills - newasgharskills

print(f'uniqueskills are there:{uniqueskills}')

# This is how you perform actions on sets, like finding common, unique and both skills.



for skill in asgharskills:
    print(skill)



for skill in newasgharskills:
    print(skill)



# So, that was all about set, looping through them and their operations.

# Now learn Dictionaries in Python

asgharInfo = {
    'name':'Asghar',
    'rollno':26,
    'fathername':'Ali Sher',
    'Degree': 'BSIT',
    'Skill':'Python'
}

print(asgharInfo)

asgharInfo['ambition']='Python Programming'

print(asgharInfo)

asgharInfo.update({'firstname':'asghar', 'secondname':'ali'})
print(asgharInfo)

del asgharInfo['rollno']

print(asgharInfo)

for key in asgharInfo.keys():
    print(key)

for value in asgharInfo.values():
    print(value)

for key, value in asgharInfo.items():
    print(key, value)



for key in asgharInfo.keys():
    if key =='firstname':

        asgharInfo[key] = 'ALi Asghar'


print('kam ho gya bhi jn')


print(asgharInfo)