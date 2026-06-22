
def chaitype(typeofchai):
    print(f'i am prerating {typeofchai} chai')
    try:
        if typeofchai=='unknown':
            raise ValueError ('This is not a valid value')
    except Exception as e:
        print('Error',e)
    else:
        print(f'Chai {typeofchai} is served')
    finally:
        print(f'Next Customer please')


chaitype(
    'unknown'
)



def servechai(item, quantity):
    try:
        price = {'masala':40, 'lachi':20}[item]
        quantity = quantity
        total = price*int(quantity)
        print(f'total price is {total}')
    except KeyError:
        print(f'There is no key with {item} in our menu')
    except TypeError:
        print(f'Quantity should be in numbers')

servechai('masala', '12')



def menuselector(youritem):
    if youritem not in ['masala chai', 'lachi chai','ginger chai','podina chai']:
        raise ValueError('This item is not in out menu')
    else:
        print(f'Your chai is ready. Please take your {youritem} chai')


menuselector('ginger chai')


class MyExceptions(Exception):
    pass
    



def makechai(milk, sugar):
    try:
        if milk ==0 or sugar ==0:
            raise MyExceptions('We cannot make chai without sugar and milk')
    except Exception as e:
        print('this is error', e)
    else:
        print(f'Chai is ready with {milk} milk and {sugar} sugar')

makechai(1,2)


class chaiErrors(Exception):pass

def makechai(chaitype, cup):
    menu = {'masala':20,'lachi':40, 'ginger':50}
    try:
        if chaitype not in menu:
            raise chaiErrors('This flavor is not available')
        if not isinstance(cup,int):
            raise TypeError('Cup should be integer')
        price = menu[chaitype]
        cup = cup
        total = price*cup
        print(f'Total bill for your {chaitype} chai and {cup} cup is {total}')
    except Exception as e:
        print('Error Occured', e)
        

makechai('ginger', 2)




file = open('asghar.txt','w')
try:
    file.write('I am asghar, from okara, learning cloud, help me to master that')
except Exception as e:
    print('Error', e)
finally:
    print('Hi, Asghar how are you!.')
    print('I have done the work, file is being written')
    file.close

with open('asghar.txt', 'w') as file:
    file.write('Hello, Asghar how are you!')

    