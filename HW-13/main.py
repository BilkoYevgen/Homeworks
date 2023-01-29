# 1. До завдання, в якому ви реалізовували телефонну книгу, додати валідацію номера телефону за допомогою RegEx. Врахувати можливість декількох форматів: +380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX

import json
import re


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
            if re.search(r'^(\+380|380|0)\d{9}$', number):      # REGEX IS HERE
                phonebook[name] = number
                with open('phonebook.json', 'w+') as file:
                    json.dump(phonebook, file)
                print('Contact added successfully')
                command = ''
                continue
            else:
                print("Wrong number")
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
            with open('phonebook.json', 'w+') as file:
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


# 3. (необов'язкове виконання) Написати програму, яка буде:
# зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
# знаходити всі email в тексті і змінювати їх на X***@****X, де замість Х мають бути перша і остання літери справжньої адреси, а весь інший текст має бути замінений на *. Кількість * необовʼязково має відповідати кількості замінених символів


def replace_emails(file_name):
    with open(file_name, "r") as file:
        text = file.read()
    email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    emails = re.findall(email_regex, text)
    for email in emails:
        first_char = email[0]
        last_char = email[-1]
        middle = "*" * (len(email) - 2)
        new_email = f"{first_char}{middle}@{middle}{last_char}"
        text = text.replace(email, new_email)
    print(text)

file_name = input("Enter the name of the file: ")
replace_emails(file_name)
