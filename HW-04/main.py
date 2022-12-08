input_type_checker = input("Enter word or integer: ")

if input_type_checker.isdigit():
    if int(input_type_checker) % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")
else:
    length = len(input_type_checker)
    print(f"This is {length} lettеr word")

