# Написать собственный декоратор, задачей которого должна быть печать названия функции и времени, когда она была вызвана. Декоратор должен работать для разных функций одинаково.
import time

print("------------------------------TasK №1-----------------------------")

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Function name: {func.__name__}')
        print(f'Function was called at: {time.strftime("%d/%m/%Y, %H:%M:%S")}')
        return result
    return wrapper

@decorator
def calc():
    print("Function without args")

calc()

print("_____________Other function example after 2 seconds_________________")

@decorator
def another_calc(a, b):
    time.sleep(2)
    print(f"Function with args a + b = {a + b}")

another_calc(3,4)


print("------------------------------TasK №2-----------------------------")
# Написать кастомный Exception класс MyCustomException, который должен сообщать "Custom exception is occured".

class MyCustomException(Exception):
    pass

def myFuncError():
    if (1==1):
        raise MyCustomException("Custom exception is occured")

print(MyCustomException)

print("------------------------------TasK №3-----------------------------")
# Написать собственный менеджер контекста, задачей которого будет печатать "==========" – 10 знаков равно перед выполнением кода и после выполнения кода, таким образом выделяя блок кода символами равен.
# В случае возникновения какой-либо ошибки она должна быть напечатана текстом, однако программа не должна завершить свою работу.

class MyManager(object):
    def __init__(self):
        pass

    def __enter__(self):
        print("==========")

    def __exit__(self, type, value, traceback):
        if type is not None:
            print(value)
        print('=' * 10)
        return True

with MyManager():
    print("Some text inside task №3")

print("____________Context manager with exception example________________")

with MyManager():
    print(1/0)

print("------------------------------TasK №4-----------------------------")
# Написать конструкцию try...except...else...finally, которая будет делать точно то же, что и менеджер контекста из предыдущего задания.

def try_except(func):
    try:
        print("==========")
        func()
    except Exception as Err:
        print(Err)
    else:
        print("Else part of task №4")
    finally:
        print("Finally part of task №4")
        print("==========")



try_except(lambda: print("Try part of task №4"))

print("____________Try..except with exception example________________")

try_except(lambda: print(1/0))
