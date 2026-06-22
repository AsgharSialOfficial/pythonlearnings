total_person = int(input('Enter total number of people '))
members = []
for i in range(total_person):
    persom_name = input('Enter Person Name')
    members.append(persom_name)

total_bill = float(input('Enter total bill amount'))
bill_per_head = round(total_bill/total_person)
print(f'{"*"*40}')
print(f'\n Total bill is {bill_per_head} PKR')
print(f'{"*"*40}')

for i in members:
    print(f'{i} have to pay {bill_per_head}')
