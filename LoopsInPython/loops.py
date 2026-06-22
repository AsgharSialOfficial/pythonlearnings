for token in range(1,11):
    print(f'Serving Chai to Token#{token}')



for batch in range(1,5):
    print(f'Making Chai for Batch #{batch}')


chai_Orderlist =['asghar', 'safdar', 'ali', 'saqlain']

for personorder in chai_Orderlist:
    print(f'Chai for {personorder} is ready.Please Take it.')

for index,keys in enumerate(chai_Orderlist, start=1):
    print(f'{index}:{keys}') 


customer_list = ['asghar', 'safdar', 'awais', 'ali']
customer_bills = [100,150,200,130]

for customer, bill in zip(customer_list, customer_bills):
    print(f"{customer.capitalize()} needs to pay {bill} PKR")



temperature = 40

while(temperature<=100):
    print(f'current temperature is {temperature}')
    temperature+=15

chai_flavors=['lachi', 'podina', 'green']
for flavor in chai_flavors:
    if flavor == 'lachi':
        continue

    if flavor =='green':
        print('this flavor is discontinued')
        break
    else:
        print(f'{flavor} is available')
print('Now we are outside of loop')


candidates = [('asghar', 10), ('safdar', 15), ('ali', 23)]

for name, age in candidates:
    if age >=18:
        print(f'{name} is eligible for vote ')
        
    else:
        print(f'{name} is not eligible for vote')



available_sizes = ['small', 'medium', 'large']

if (requested_size:=input('Enter your size')) in available_sizes:
        print(f'{requested_size} is avialable in availabe sizes')
else:
        print(f'{requested_size} is available in available sizes')


