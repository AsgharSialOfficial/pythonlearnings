import os
import csv 

filename = 'contacts.csv'

def intializecsv():
    if not (os.path.exists(filename)):
        with open(filename,'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name','phone', 'adress'])

def loadcontacts():
    contacts = []
    with open (filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def addcontact():
    name= input('Enter contatc name')
    phone = input('Enter contact phone number')
    address = input('Enter contact address')
    allcontacts = loadcontacts()
    for contact in allcontacts:
        if contact['name'].lower()==name.lower():
            print('This contact already exist')
            return
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name,phone,address])
    print('Contact is added')

def searchcontact():
    name = input('Enter contact name you want to search').strip()
    allcontacts = loadcontacts()
    found = False
    for contact in allcontacts:
        if contact['name'].lower()==name.lower():
            print('This name exist')
            print(f'name:{contact['name']}\n phone:{contact['phone']}\n address:{contact['adress']}')
            found =True
            break
    if not found:
        print(f'Contact with {name} not found')
def viewcontacts():
    allcontacts = loadcontacts()
    for i,contact in enumerate(allcontacts,1):
        print(f'{'*'*5}{i}{'*'*5}')
        for key, value in contact.items():
            print(f'{key}:{value}')

def saveallcontatcs(contactlist):
    with open(filename,'w',newline='') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(['name','phone','adress'])
        for contact in contactlist:
            filewriter.writerow([contact['name'],contact['phone'],contact['adress']])
        print('All Contact have been saved!')
def updatecontact():
    number = int(input('Which contact you want to update'))
    name = input('Enter Updated name')
    phone = input('Enter Updated Phone')
    address = input('Enter Updated Address')
    allcontacts = loadcontacts
    allcontacts[number-1]['name']= name
    allcontacts[number-1]['phone']= phone
    allcontacts[number-1]['adress']= address

    saveallcontatcs(allcontacts)
    print('Contact list has been updated!')

def deletecontact():
    number = int(input('Enter number you want to delete'))
    allcontacts = loadcontacts()
    allcontacts.pop(number-1)
    saveallcontatcs(allcontacts)
    print('Contact list has been updated!.')

viewcontacts()

while True:
    print('1.View all Contacts')
    print('2.Search Contact')
    print('3.Add Contact')
    print('4.Update Contact')
    print('5.Delete Contact')
    print('6.Exit')

    option = input('Choose Option').strip()
    match option:
        case '1':
            viewcontacts()
        case '2':
            searchcontact()
        case '3':
            addcontact()
        case '4':
            updatecontact()
        case '5':
            deletecontact()
        case '6':
            print('Exit')
            break
        case _:
            print('Invalid OutPut')



