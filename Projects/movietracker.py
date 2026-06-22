import os
import json
filename = "movietrackerfile.json"

def initializafile():
    if not os.path.exists(filename):
        with open (filename, 'w') as file:
            json.dump([],file)

def viewallmovies():
    with open (filename, 'r') as file:
        allmovies = json.load(file)
        return allmovies
def savemovies(movies):
    with open(filename, 'w') as file:
        json.dump(movies,file, indent=2)

def addmovie():
    moviename = input('Enter movie name')
    moviecategory = input('Enter movie category')
    movierating = float(input('Enter movie rating'))
    allmovies = viewallmovies()
    for movie in allmovies:
        if movie['name'].lower()==moviename.lower():
            print('This moview Already exists')
            return
    allmovies.append({'name':moviename, 'category':moviecategory, 'rating':movierating})
    savemovies(allmovies)

def searchmovie():
    moviename = input('Enter movie name you want to search')
    moviecategory = input('Enter your movie category')
    movierating = float(input('Enter movie rating'))

    allmovies = viewallmovies()
    found = False
    for movie in allmovies:
        if (movie['name']==moviename or movie['category']==moviecategory or movie['rating']==movierating):
            print('Movie Found')
            print(f"Movie Name: {movie['name']}\n Movie Category:{movie['category']} \n Movie Rating:{movie['rating']}")
            found = True
            break

    if not found:
        print('Movie do not exist')
def deletemovie():
    number = int(input('Enter movie number you want to delete'))
    allmovies = viewallmovies()
    allmovies.pop(number-1)
    savemovies(allmovies)
    print('Movie has been deleted')

while True:
    print('1.View Movies')
    print('2.Add Movies')
    print('3.Search Movies')
    print('4.Delete Movies')
    print('5.Exit')
    choice = input('Enter your Choice')

    match choice:
        case '1':
            allmovies = viewallmovies()
            for movies in allmovies:
                print(f'1.{'*'*10}')
                for key,value in movies.items():
                    print(f'{key}:{value}')
        case '2':
            addmovie()
        case '3':
            searchmovie()
        case '4':
            deletemovie()
        case '5':
            break
        case _:
            print('Invalid Choise')

