# 1. Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі, використовуючи генератори.

number = int(input('Enter a number for function №1: '))

def fibonacci(n):
    x, y = 0, 1
    for i in range(n + y):
        yield x
        x, y = y, x + y

ls = (list(fibonacci(number)))

print (ls.pop())

# 2. Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі, використовуючи ітератори (необов'язкове виконання).

print("Attention! Function №2 is missing")

# 3. Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі, використовуючи рекурсію (необов'язкове виконання).

n = int(input("Enter a number for function №3: "))

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))


# 4. Написати програму, яка буде повертати факторіал введеного числа, використовуючи рекурсію (необов'язкове виконання).

n = int(input("Enter a number for function №4: "))

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(n))

