import datetime

name = input('Enter your name')
age = input('Enter your age')
city = input('Enter your city')
profession = input('Enter your profession')
hobby = input('Enter your hobby')

selfintro = (f'I am {name} from {city} city , age {age}, working as a {profession} and in my free time I enjoy {hobby}')


currenttime = datetime.date.today().isoformat()
decoration = "*"*70

finalscript = print(f'{decoration}\n {selfintro}\n Last Login: {currenttime}\n {decoration}')

print(finalscript)

