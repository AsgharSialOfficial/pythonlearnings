name = input('Enter your name')
website = input('Enter your website')
city = input('Enter your city')
profession = input('Enter your profession')
hobby = input('Enter your hobby')
favoriteemoji = input('Enter your Emoji ')

print('For Vertical Style choose 1')
print('For Horizontal Style choose 2')
print('For Sandwitch Style choose 3')
style = input('Enter your option 1,2,3  ')

if style =='1':
    print (f'{favoriteemoji} {name} | {profession} \n {hobby} {favoriteemoji} \n City| {city} {favoriteemoji} \n Website|{website}')
elif style =='2':
    print (f'{favoriteemoji} {name} _ {profession} \n {hobby} {favoriteemoji} \n City_ {city} {favoriteemoji} \n Website_{website}')
elif style =='3':
    print (f'{favoriteemoji*50}\n {name} | {profession} \n {hobby} {favoriteemoji} \n City| {city} {favoriteemoji} \n Website|{website}\n {favoriteemoji*50}')
else:
    print('Invalid OutPut')


