import time

# 1

printed_value = input("Enter value here: ")

for item in printed_value:
    if item.isdigit():
        if int(item) % 2 == 0:
            print(f"{item} is even number")
        else:
            print(f"{item} is odd number")
    elif item.isalpha():
        if item.islower():
            print(f"{item} is lower letter")
        else:
            print(f"{item} is upper letter")
    else:
        print(f"{item} is symbol")



# 2

while True:
    time.sleep(4.2)
    print("I love Python")