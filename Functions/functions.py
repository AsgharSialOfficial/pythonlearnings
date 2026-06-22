def chai_order(name, chaitype):
    print(f'{name} ordered {chaitype} chai')


chai_order('asghar', 'lachi')



# pure and impure, recursive function


def asgharbhi(*hobbies, **personalData):

    print(f'my hobbies are :{hobbies}')
    print(f'my personal info is :{personalData}')



asgharbhi('coding', 'programming', 'web scraping', name='asghar', age=23, degree='BSIT')


# This was about how to get multiple positional arguments and key value pairs.


def make_chai(chai, sugar, price):

    print(f'This chai is {chai} chai, with {sugar} sugar and price {price}')


make_chai('lachi', '2g', 150)
make_chai(chai='podina', price=200, sugar='5g')


def asgharage (n):
    print(f'asghar age is :{n}')

    if n==0:
        return
    return asgharage(n-1)


asgharage(26)


# This was resusive function and we use it. 


def math_operations(numbr1, number2, operation):
    if operation=='add':
        return numbr1+number2
    elif operation=='multiply':
        return numbr1 *number2
    elif operation == 'subtract':
        return numbr1-number2
    elif operation == 'divide':
        return numbr1/number2
    else:
        print('Invalid Math Operations')
finalvalue = math_operations(23,56,'multiply')
print(finalvalue)



myname = 'asghar'
def yourname():
    myname = 'safdar'
    print(myname)
    def iwillchange():
        nonlocal myname
        myname = 'safdar ali'
        print(myname)
    print(myname)
    print(f'Before',myname)
    iwillchange()
    print(f'After',myname)
yourname()


print(myname)