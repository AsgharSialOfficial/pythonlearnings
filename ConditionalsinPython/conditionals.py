tea_leaves = True
if(tea_leaves):
    print('you have tea leaves')
else:
    print('you do not have tea')



customer_name = 'Asghar'
customer_age = 60
total_purchases = 1000

if customer_age>=60:
    print('Customer is senior citizen')
    if total_purchases >=1000:
        print('Customer is eligible for discount')




print('All Done')


user_choice = input('Enter your Input').lower()
if user_choice == 'samosa' or user_choice =='cookies':
    print('Order Confirmed')
else:
    print('Item unavailable')




juice_cup = input('Enter your Juice Cup')

if juice_cup == 'small':
    print('Price is 50 pkr')
elif juice_cup =='medium':
    print('Price is 100 pkr')
elif juice_cup =='large':
    print('Price is 150 pkr')
else:
    print('Unknown Size of Cup')


device_status = False
temperature = int(input('enter your temperature'))
if device_status:
    print('device is active')
    if temperature >=35:
        print('temperature is high')
    else:
        print('temperature is normal')
else:
    print('device is inactive')


# Solved problem through ternary operator.

enter_orderamount = int(input('Enter your Amount'))

delivryfee = 0 if enter_orderamount>300 else 50

print(f'your delivery fee is : {delivryfee}')


job_type = input('Enter your job type')

match job_type:
    case 'web scraper':
        print('So, you want to become web scraper')
    case 'AI Agents Developer':
        print('So, you want to become AI Agents Developer')
    case 'Python Automation':
        print('So, you want to become Python Automation Expert')
    case _:
        print('You did not choose anything')




