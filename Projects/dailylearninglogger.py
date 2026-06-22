import datetime

enter_your_learning = input('Enter your learning- what you learned today!')
rate_productivity = input('How was your productivity_ rate 1-5')

timeentry = datetime.date.today().isoformat()
print(timeentry)





final_entry_string = f'\n{timeentry}  \n {enter_your_learning} \n Productivity: {rate_productivity}\n{"*"*70}'


with open('mydailyjournal.txt', 'a', encoding='utf-8') as file:
    file.write(final_entry_string)
print(f'your entry has been recorded')