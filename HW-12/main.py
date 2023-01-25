# 1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.
#
# Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
# При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
# Підказка: Ви можете використати бібліотеку json, яка допоможе із перетворенням dict в JSON string (при записі в файл) і JSON string в dict (при читанні із файлу). Файл слід оновлювати після кожної успішної операції add або delete.

import json
import time


def number_validation(number):
    split_plus = number.split("+")
    if not number.startswith("+"):
        print("Number must starts with '+'")
        return False
    elif not split_plus[1].isdigit():
        print("Must be integer")
        return False
    elif len(split_plus[1]) != 12:
        print('Length is not correct')
        return False
    else:
        return True


phonebook = {}

try:
    with open('phonebook.json', 'r') as file:
        phonebook = json.load(file)
except FileNotFoundError:
    print("Error: phonebook.json not found.")
else:
    print("Phonebook successfully loaded")


print(f'Now in your contacts: {phonebook}')

command = ''

while True:

    if command == '':
        command = input('Enter command here: ')

    # ------------------------------------------------------------------------------------------

    if command == 'stats':
        if len(phonebook) == 1:
            print(f'There is {len(phonebook)} contact in your phonebook')
            print(phonebook)
            command = ''
            continue
        else:
            print(f'There are {len(phonebook)} contacts in your phonebook')
            print(phonebook)
            command = ''
            continue

    # ------------------------------------------------------------------------------------------

    if command == 'add':
        name = input('Type name: ')
        number = input('Type number: ')
        if name not in phonebook:
            if number_validation(number):
                phonebook[name] = number
                with open('phonebook.json', 'w+') as file:
                    json.dump(phonebook, file)
                print('Contact added successfully')
                command = ''
                continue
            else:
                continue
        else:
            print('Name already exist')
    # ------------------------------------------------------------------------------------------

    command_splitted = command.split(" ", 1)
    if command_splitted[0] == 'delete' and len(command_splitted) > 1:
        splitted_value = command.split(" ", 1)[1]
        my_list = phonebook.keys()
        if splitted_value in my_list:
            del phonebook[splitted_value]
            with open('phonebook.json', 'w') as file:
                json.dump(phonebook, file)
            print(f'{splitted_value} successfully deleted')
            print(f'Now you have {len(phonebook)} contacts')
            print(phonebook)
            command = ''
            continue
        else:
            print(f'There is no contact {splitted_value}')
            command = ''
            continue
    elif command_splitted[0] == 'delete':
        print("All data has been deleted")
        phonebook.clear()
        with open('phonebook.json', 'w') as file:
            json.dump(phonebook, file)
        command = ''

    # ------------------------------------------------------------------------------------------

    command_splitted = command.split(" ", 1)
    if command_splitted[0] == 'show' and len(command_splitted) > 1:
        splitted_value = command.split(" ", 1)[1]
        my_list = phonebook.keys()
        if splitted_value in my_list:
            print(f'Here is full info about user {splitted_value}: {phonebook.get(splitted_value)}')
            command = ''
            continue
        else:
            print(f'There is no contact {splitted_value}')
            command = ''
            continue
    elif command_splitted[0] == 'show':
        answer = input('Please enter name to show: ')
        if answer in phonebook.keys():
            print(f'Here is full info about user {answer}: {phonebook.get(answer)}')
        command = ''

    # ------------------------------------------------------------------------------------------

    if command == 'list':
        if len(phonebook) == 0:
            print('Phonebook is empty')
        else:
            for key in phonebook:
                print(key)
                command = ''
            continue
        command = ''

    # ------------------------------------------------------------------------------------------

    if command == 'exit':
        break


# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Function name: {func.__name__}')
        print(f'Function was called at: {time.strftime("%d/%m/%Y, %H:%M:%S")}')
        return func(*args, **kwargs)

    return wrapper


@decorator
def calc():
    print("d")


calc()


# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.

class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)
        with open('exception.txt', 'a+') as file:
            file.write(message + " " + str(time.strftime("%d/%m/%Y, %H:%M:%S")) + '\n')


raise MyException("Message of the exception")
