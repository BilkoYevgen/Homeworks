print("----------------------------------------------Task №1----------------------------------------------")
# 1.Создать класс Bot с атрибутом name и методами say_name и send_message. send_message должен принимать параметры self и message и печатать message. Метод say_name должен печатать значение атрибута name.
# some_bot = Bot('Marvin') some_bot.say_name() >> > "Marvin"
# some_bot.send_message("Hello") >> > "Hello"

class Bot:

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


some_bot = Bot('Marvin')
some_bot.say_name()
some_bot.send_message("Hello")

print("----------------------------------------------Task №2----------------------------------------------")
# 2. Создать класс TelegramBot, который должен быть унаследован от Bot и должен содержать: собственные атрибуты url, chat_id(None по умолчанию) методы send_message, set_url и set_chat_id Эти методы, кроме self, должны принимать один параметр(url и chat_id соответственно)
# и присваивать значение этого параметра атрибутам url и chat_id соответственно. Также TelegramBot должен переопределить метод send_message – печатать значение параметра message с любым вспомогательным текстом.Этот текст также должен содержать значение url и chat_id
# Результатом должно быть:
# telegram_bot = TelegramBot("TG")
# telegram_bot.say_name() >> > "TG"
# telegram_bot.send_message('Hello') >> > "TG bot says Hello to chat None using None"
# telegram_bot.set_chat_id(1)
# telegram_bot.send_message('Hello') >> > "TG bot says Hello to chat 1 using None"

class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        super().__init__(name)
        self.url = None
        self.chat_id = None

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")

telegram_bot = TelegramBot("TG")
telegram_bot.say_name()
telegram_bot.send_message('Hello')
telegram_bot.set_chat_id(1)
telegram_bot.set_url("www.other.url")
telegram_bot.send_message('Hello')


print("----------------------------------------------Task №3----------------------------------------------")
# 3.(необязательное исполнение) Создать класс MyStr(str), который должен переопределить метод str таким образом, чтобы вместо печати реального значения все буквы были переведены в верхний регистр: my_str = MyStr('test') print(my_str) >> > "TEST"

class MyStr(str):
    def __init__(self, text):
        self.text = text
        super().__init__()

    def __str__(self):
        return self.upper()

my_str = MyStr('This is a test')
print(my_str)

print("----------------------------------------------Task №4----------------------------------------------")
# 4.(необязательное исполнение) Создать класс User, который в конструкторе должен принимать параметр name и инициализировать его в соответствующий атрибут. Переопределить метод eq таким образом,
# чтобы при сравнении 2 объектов типа User у совпадающих атрибутов name мы получили True.При этом не учитывать регистр, в котором записаны каждый из атрибутов. first_user = User('OLEKSII') second_user = User('Oleksii') print(first_user == second_user) >> > True

class User:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()


one = User("des")
two = User("DES")
print(one == two)
tre = User("dfsFfsd")
four = User("DDF")
print(tre == four)


print("----------------------------------------------Task №5----------------------------------------------")
# 5.(необязательное исполнение) Создать класс Bot и TelegramBot из первого задания с помощью функции type

def init_function(self, name):
    self.name = name

def say_name_function(self):
    print(self.name)

def send_message_function(self, message):
    print(message)

type_class = type(
    'Bot',
    (),
    {
        '__init__': init_function,
        'say_name': say_name_function,
        'send_message': send_message_function
    }
)

first_obj = type_class("Marvin")
first_obj.say_name()
first_obj.send_message("Hello")


def new_init(self, name, url=None, chat_id=None):
    type_class.__init__(self, name)
    self.url = url
    self.chat_id = chat_id

def set_url(self, url):
    self.url = url

def set_chat_id(self, chat_id):
    self.chat_id = chat_id

def send_message(self, message):
    print(f"{self.name} bot says {message} to chat {self.chat_id} using URL: {self.url}")

type_class2 = type(
    'TelegramBot',
    (type_class,),
    {
        '__init__': new_init,
        'set_url': set_url,
        'set_chat_id': set_chat_id,
        'send_message': send_message
    }
)


second_obj = type_class2("TG")
second_obj.say_name()
second_obj.send_message('Hello1')
second_obj.set_chat_id(2646666)
second_obj.set_url("www.other.url")
second_obj.send_message('Hello2')
