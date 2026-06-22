
# There are mutable and unmutable. You can change the referecen not the numbers.


#There are values, id and types of Objects, We can check mutibilty and non-mutibilty of an obect using Id.




asgharage = 23
print(f' asghar age is : {asgharage}')
asgharage = 26
print(f" asghar age is : {asgharage}")
print(f'23 id is:{id(23)}')
print(f'26 id is :{id(26)}')



asgharhobbies = set()
print(f'asgharhobbies id before adding :{id(asgharhobbies)}')

asgharhobbies.add('football')
asgharhobbies.add('cricket')
asgharhobbies.add('hockey')
print(f'asgharhobbies id after changes: {id(asgharhobbies)}')

print(f'my hobbies are : {asgharhobbies}')

asgharhobbies = {'coding', 'hockey', 'programming'}
print(f'asghar is my friend: {asgharhobbies}')
print(f'asgharhobbies after second assignment :{id(asgharhobbies)}')

#so what we learned that number are unmutabe, we only change referecne to that memory 
#location, whilesome data types are mutable means we can perform crud operation
# in them, ike lists, set, dictionaries.




asghar_age = 34


print(asghar_age)

print(id(asghar_age))

asghar_age = 56

print(asghar_age)
print(id(asghar_age))


asghar_hobbies = {'coding','programming', 'web scraping'}
print(asghar_hobbies)
print(id(asghar_hobbies))


asghar_hobbies.add('web developer')

print(asghar_hobbies)
print(id(asghar_hobbies))



asghar_hobbies.add('AI Agents Developer')

print(asghar_hobbies)
print(id(asghar_hobbies))



# Numbers, integers, boolean, and real are different types of number data types in python.

month_days = 30
daily_expense = 100

monthly_expense = month_days*daily_expense

print(f'your monthly expense is : {monthly_expense}')

daily_expense = monthly_expense/month_days

print(f'your daily expense is:{daily_expense}')

month_days = monthly_expense/daily_expense

print(f'month days are : {month_days}')

mymodulus = daily_expense%month_days

print(f'my daily modulus is: {mymodulus}')

# Can I concatenate a string and integar



number1 = 12
myname = 'asghar'

print(str(number1)+myname)




number1 = 12
mynameletter = 5

print(number1+mynameletter)



# String in Python, we will learn about indexes, slicing, encoding.


myname = 'asghar'
print(myname)

fullname = myname[:-1]
print(fullname)

first3letter = myname[0:3]
print(first3letter)

last3digit = myname[3:-1]

print(last3digit)

reverseString = myname[::-1]

print(reverseString)
encodedstring = myname.encode("utf-8")

print(encodedstring)


asgharwith1inter  = myname[:2]
print(asgharwith1inter)
