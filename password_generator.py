import random
import string

charecters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

def password_generate():
    password_length = int(input('How long should the password be?:  '))

    password = []

    random.shuffle(charecters)

    for i in range(password_length):
        password.append(random.choice(charecters))

    random.shuffle(password)

    password = ''.join(password)

    print(f'Your Passoword is ready: {password}')

    save_option = input('You want save password in file?: ')
    if save_option.lower() == 'yes':
        name_of_password = input('Name of password sir: ')
        with open('passwords.txt', 'a') as f:
            f.write(f'{password} - {name_of_password}\n')
            print('Password is saved!')
    else:
        print('Okay bye')        

option = input('Would you like a generate password(Yes/No): ').lower()

if option == 'yes':
    password_generate()
elif option == 'no':
    quit('Bye')
else:
    print('YES or NO????')  
    option = input('Would you like a generate password(Yes/No): ').lower()
    if option == 'yes':
        password_generate()
    

input()