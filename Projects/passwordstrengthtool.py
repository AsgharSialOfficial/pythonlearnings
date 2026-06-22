import random
import string
import getpass

def password_strength_checker(password):

    errors = []
    if len(password)<8:
        errors.append('Password should be equal 8 characters')
    if not any(c.islower()for  c in password):
        errors.append('There is no any lower case practice')
    if not any(c.isupper() for c in password):
        errors.append('There is not any uppercase letter in the password')
    if not any(c.isdigit() for c in password):
        errors.append('There is not any digit in your password')
    if not any(c in string.punctuation for c in password):
        errors.append('There is not an special character')
    return errors, password
def generate_strong_password(length=12):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for _ in range(length))
    return password



while True:
    suggestion = generate_strong_password()
    password = getpass.getpass('Enter your password')
    errors, userpassword = password_strength_checker(password)
    if not errors:
        print('Password is strong')
        print(f'This is your password: {userpassword}')
    else:
        if errors:
            for i in errors:
                print(f'{i}')
        print(f'you can use this password , this is strong:{suggestion}')