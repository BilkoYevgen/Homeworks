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


phonebook = {
    'Ryan Murphy': '+380634325465',
    'Brad Falchuk': '+380503291582',
    'Evan Peters': '+380983452362',
    'Sarah Paulson': '+380739547827',
}

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
        for key in phonebook:
            print(key)
            command = ''
        continue
    command = ''


