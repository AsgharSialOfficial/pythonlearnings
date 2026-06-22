

def agecalculations (ageinyears):
    day_in_year = 365.2
    hours_in_day = 24.0
    minutes_in_hour = 60.0

    totalageindays = ageinyears*day_in_year
    totalageinhours = ageinyears*day_in_year*hours_in_day
    totalageinminutes = ageinyears*day_in_year*hours_in_day*minutes_in_hour
    return totalageindays, totalageinhours, totalageinminutes

while True:
    yourage = int(input('Enter your age '))
    days, hours, minutes = agecalculations(yourage)
    print(f'your age in days is {days}, in hours is {hours}, in minutes is {minutes}')

    again = input('Do you want to procede futhure y/n')
    if again !='y':
        print(f'so you want to end this program and break the loop')
    
