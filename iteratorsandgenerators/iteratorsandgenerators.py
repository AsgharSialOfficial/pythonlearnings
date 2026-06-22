

def asgharcase():
    yield 'Case 1: This is case 1'
    yield 'Case 2: This is case 2'
    yield 'Case 3: This is case 3'



cases = asgharcase()
print(cases)
print(cases)
print(cases)
for case in cases:
    print(case)





def infinteukvisa():
    ukvisa = 1
    while True:
        yield f'uk visa {ukvisa}'
        ukvisa +=1

ukvisa = infinteukvisa()

for _ in range(5):
    print(next(ukvisa))


# Send Value to Generators

def asgharbhi():
    print('who are you brother? Do you have any good name')
    name = yield
    while True:
        print(f'Your name is {name}')
        name= yield

yourname = asgharbhi()



print(next(yourname))

yourname.send('Asghar')



def programmingskills():
    yield 'Coding'
    yield 'Programming'

def personalskills():
    yield 'Communications'
    yield 'Investor'

def fullskills():
    yield from programmingskills()
    yield from personalskills()



allskills = fullskills()

for skill in allskills:
    print(skill)

allskills.close()


def asgharchai():
    try:
        yield 'hello g'
        raise ValueError('Something went wrong')
    except:
        yield 'error bro'


asgharchairesult = asgharchai()

print(next(asgharchairesult))



def myfunc(func):
    def mywrapper():
        print('Before the print statement')
        func()
        print('After the print statement')
    return mywrapper

@myfunc
def mygreet():
    print('how are you bro')




mygreet()




def chaiwrapper(func):
    print('I am chai wrapper')
    def chaiwrapperarguments(*arg,  **kargs):
        result = func(*arg, **kargs)
        print(f'function calling start: {result}')
        print(result)
        print(f'Function calling end: {result}')
        return result
    return chaiwrapperarguments
@chaiwrapper
def mychai(chai_type):
    print(f'you chai is ready : {mychai.__name__}')


mychai('lachi chai')




def shouldlogin(function):
    print('this is shouldlogin function')
    def loginwrapper(role):
        if role !='admin':
            return ('Acess Denied, you are not admin')
        else:
            return function(role)
    return loginwrapper


@shouldlogin
def canilogin(role):
    return 'Yes, you have, logged in sucessfully'


finalresult =canilogin('admin')
print(finalresult)

print(finalresult)
    