# # ООП на Python: концепции, принципы и примеры реализации
# # Программирование на Python допускает различные методологии, но в его основе лежит объектный подход,
# # поэтому работать в стиле ООП на Python очень просто.
# # ООП на Python (Объектно-ориентированная парадигма имеет несколько принципов:)
# # Данные структурируются в виде объектов, каждый из которых имеет определенный тип, то есть принадлежит к какому-либо классу.
# # Классы – результат формализации решаемой задачи, выделения главных ее аспектов.
# # Внутри объекта инкапсулируется логика работы с относящейся к нему информацией.
# # Объекты в программе взаимодействуют друг с другом, обмениваются запросами и ответами.
# # При этом объекты одного типа сходным образом отвечают на одни и те же запросы.
# # Объекты могут организовываться в более сложные структуры, например, включать другие объекты 
# # или наследовать от одного или нескольких объектов.
# # Если вам интересно, что думает об этой концепции сам ее создатель Алан Кэй, загляните сюда.

# # Язык Python – типичный представитель ООП-семейства, обладающий элегантной и мощной объектной моделью. 
# # В этом языке от объектов никуда не спрятаться (ведь даже числа являются ими), 
# # поэтому давайте разбираться, как это все реализовано.

# # Основы ООП на Python для начинающих
# # Классы
# # Создавать классы в Python очень просто:

# class SomeClass(object):
#   # поля и методы класса SomeClass
# # Классы-родители перечисляются в скобках через запятую:

# #class SomeClass(ParentClass1, ParentClass2):
#   # поля и методы класса SomeClass
# # С реализацией наследования разберемся чуть позже.
# # Свойства классов устанавливаются с помощью простого присваивания:

# #class SomeClass(object):
#     attr1 = 42
#     attr2 = "Hello, World"
# # Методы объявляются как простые функции:

# class SomeClass(object):
#     def method1(self, x):
#         # код метода
# # Обратите внимание на первый аргумент – self – общепринятое имя для ссылки на объект, 
# # в контексте которого вызывается метод. Этот параметр обязателен и отличает метод класса от обычной функции.
# # Все пользовательские атрибуты сохраняются в атрибуте __dict__, который является словарем.
# # Экземпляры классов
# # Инстанцировать класс в Python тоже очень просто:

# #class SomeClass(object):
#     attr1 = 42

#     def method1(self, x):
#         return 2*x

# obj = SomeClass()
# obj.method1(6) # 12
# obj.attr1 # 42
# # Можно создавать разные инстансы одного класса с заранее заданными параметрами с помощью инициализатора
# #  (специальный метод __init__). Для примера возьмем класс Point (точка пространства), 
# #  объекты которого должны иметь определенные координаты:

# class Point(object):
#     def __init__(self, x, y, z):
#         self.coord = (x, y, z)

# p = Point(13, 14, 15)
# p.coord # (13, 14, 15)
# # Подробнее о других специальных методах жизненного цикла объектов поговорим чуть ниже.
# # Динамическое изменение
# # Можно обойтись даже без определения атрибутов и методов:

# class SomeClass(object):
#     pass
# # Кажется, этот класс совершенно бесполезен? 
# # Отнюдь. Классы в Python могут динамически изменяться после определения:

# class SomeClass(object):
#     pass

# def squareMethod(self, x):
#     return x*x

# SomeClass.square = squareMethod
# obj = SomeClass()
# obj.square(5) # 25
# # Статические и классовые методы
# # Для создания статических методов в Python предназначен декоратор @staticmethod. 
# # У них нет обязательных параметров-ссылок вроде self. 
# # Доступ к таким методам можно получить как из экземпляра класса, так и из самого  класса:

# class SomeClass(object):
#     @staticmethod
#     def hello():
#         print("Hello, world")

# SomeClass.hello() # Hello, world
# obj = SomeClass()
# obj.hello() # Hello, world
# # Еще есть так называемые методы классов. Они аналогичны методам экземпляров, 
# # но выполняются не в контексте объекта, а в контексте самого класса  (классы – это тоже объекты). 
# # Такие методы создаются с помощью декоратора @classmethod и требуют обязательную ссылку на класс (cls).

# class SomeClass(object):
#     @classmethod
#     def hello(cls):
#         print('Hello, класс {}'.format(cls.__name__))

# SomeClass.hello() # Hello, класс SomeClass
# # Статические и классовые методы доступны без инстанцирования.
# # Специальные методы
# # Жизненный цикл объекта
# # С инициализатором объектов __init__ вы уже знакомы. Кроме него есть еще и метод __new__,
# #  который непосредственно создает новый экземпляр класса. Первым параметром он принимает ссылку на сам класс:

# class SomeClass(object):
#     def __new__(cls):
#         print("new")
#         return super(SomeClass, cls).__new__(cls)

#     def __init__(self):
#         print("init")

# obj = SomeClass():
# # new
# # init
# # Это обсуждение на stackoverflow поможет лучше разобраться с инстанцированием классов.
# # Метод __new__ может быть очень полезен для решения ряда задач, например,
# #  создания иммутабельных объектов или реализации паттерна Синглтон:

# class Singleton(object):
#     obj = None # единственный экземпляр класса

#     def __new__(cls, *args, **kwargs):
#     if cls.obj is None:
#         cls.obj = object.__new__(cls, *args, **kwargs)
#     return cls.obj

# single = Singleton()
# single.attr = 42
# newSingle = Singleton()
# newSingle.attr # 42
# newSingle is single # true
# # В Python вы можете поучаствовать не только в создании объекта, но и в его удалении. 
# # Специально для этого предназначен метод-деструктор __del__.

# class SomeClass(object):
#     def __init__(self, name):
#         self.name = name

#     def __del__(self):
#         print('удаляется объект {} класса SomeClass'.format(self.name))

# obj = SomeClass("John");
# del obj # удаляется объект John класса SomeClass
# # На практике деструктор используется редко, 
# # в основном для тех ресурсов, которые требуют явного освобождения памяти при удалении объекта. 
# # Не следует совершать в нем сложные вычисления.
# # Объект как функция
# # Объект класса может имитировать стандартную функцию, то есть при желании его можно "вызвать"
# #  с параметрами. За эту возможность отвечает специальный метод __call__:

# class Multiplier:
#     def __call__(self, x, y):
#         return x*y

# multiply = Multiplier()
# multiply(19, 19) # 361
# # то же самое
# multiply.__call__(19, 19) # 361
# # Имитация контейнеров
# # Вы знакомы с функцией len(), которая умеет вычислять длину списков значений?

# list = ['hello', 'world']
# len(list) # 2
# # Но для объектов вашего пользовательского класса это не пройдет:

# class Collection:
#     def __init__(self, list):
#         self.list = list

# collection = Collection(list)
# len(collection)
# # Этот код выдаст ошибку object of type 'Collection' has no len(). Интерпретатор просто не понимает, 
# # как ему посчитать длину collection.
# # Решить эту проблему поможет специальный метод __len__:

# class Collection:
#     def __init__(self, list):
#         self.list = list

#     def __len__(self):
#         return len(self.list)

# collection = Collection([1, 2, 3])
# len(collection) # 3
# # Можно работать с объектом как с коллекцией значений,
# #  определив для него интерфейс классического списка с помощью специальных методов:

# # __getItem__ – реализация синтаксиса obj[key], получение значения по ключу;
# # __setItem__ – установка значения для ключа;
# # __delItem__ – удаление значения;
# # __contains__ – проверка наличия значения.
# # Имитация числовых типов
# # Ваши объекты могут участвовать в математических операциях, если у них определены  специальные методы.
# #  Например, __mul__ позволяет умножать объект на число по определенной программистом логике:

# class SomeClass:
#     def __init__(self, value):
#         self.value = value

#     def __mul__(self, number):
#         return self.value*number

# obj = SomeClass(42)
# print(obj * 100) # 4200
# # Другие специальные методы
# # В Python существует огромное количество специальных методов, 
# # расширяющих возможности пользовательских классов. Например, можно определить вид объекта на печати, его "официальное" 
# # строковое представление или поведение при сравнениях. Узнать о них подробнее вы можете в официальной документации языка.
# # Эти методы могут эмулировать поведение встроенных классов, 
# # но при этом они необязательно существуют у самих встроенных классов. Например, у объектов int при
# #  сложении не вызывается метод __add__. Таким образом, их нельзя переопределить.
# # Принципы ООП на Python
# # Рассмотрим "большую тройку" объектно-ориентированной концепции: инкапсуляцию, полиморфизм и наследование.
# # Инкапсуляция
# # Все объекты в Python инкапсулируют внутри себя данные и методы работы с ними, предоставляя публичные 
# # интерфейсы для взаимодействия.

# # Атрибут может быть объявлен приватным (внутренним) с 
# # помощью нижнего подчеркивания перед именем, но настоящего скрытия на самом деле не происходит – все на уровне соглашений.

# class SomeClass:
#     def _private(self):
#         print("Это внутренний метод объекта")

# obj = SomeClass()
# obj._private() # это внутренний метод объекта
# # Если поставить перед именем атрибута два подчеркивания, 
# # к нему нельзя будет обратиться напрямую. Но все равно остается обходной путь:

# class SomeClass():
#     def __init__(self):
#         self.__param = 42 # защищенный атрибут

# obj = SomeClass()
# obj.__param # AttributeError: 'SomeClass' object has no attribute '__param'
# obj._SomeClass__param # 42
# # Специальные свойства и методы класса, некоторые из которых вам уже знакомы, имеют двойные подчеркивания до и после имени.
# # Кроме прямого доступа к атрибутам (obj.attrName), могут быть использованы специальные методы доступа 
# # (геттеры, сеттеры и деструкторы):

# class SomeClass():
#     def __init__(self, value):
#         self._value = value

#     def getvalue(self): # получение значения атрибута
#         return self._value

#     def setvalue(self, value): # установка значения атрибута
#         self._value = value

#     def delvalue(self): # удаление атрибута
#         del self._value

#     value = property(getvalue, setvalue, delvalue, "Свойство value")

# obj = SomeClass(42)
# print(obj.value)
# obj.value = 43
# # Такой подход очень удобен, если получение или установка значения атрибута требует сложной логики.
# # Вместо того чтобы вручную создавать геттеры и сеттеры для каждого атрибута, 
# # можно перегрузить встроенные методы __getattr__, __setattr__ и __delattr__. Например,
# #  так можно перехватить обращение к свойствам и методам, которых в объекте не существует:

# class SomeClass():
#     attr1 = 42

#     def __getattr__(self, attr):
#         return attr.upper()

# obj = SomeClass()
# obj.attr1 # 42 &nbsp;&nbsp;
# obj.attr2 # ATTR2
# #__getattribute__ перехватывает все обращения (в том числе и к существующим атрибутам):

# class SomeClass():
#     attr1 = 42

#     def __getattribute__(self, attr):
#         return attr.upper()

# obj = SomeClass()
# obj.attr1 # ATTR1
# obj.attr2 # ATTR2
# # Таким образом, можно организовать динамический доступ к методам и свойствам объекта, 
# # как действуют, например,  RPC-системы.
# # Наследование
# # Язык программирования Python реализует как стандартное одиночное наследование:

# class Mammal():
#     className = 'Mammal'

# class Dog(Mammal):
#     species = 'Canis lupus'

# dog = Dog()
# dog.className # Mammal
# так и множественное:

# class Horse():
#     isHorse = True

# class Donkey():
#     isDonkey = True

# class Mule(Horse, Donkey):
# mule = Mule()
# mule.isHorse # True
# mule.isDonkey # True
# ООП на Python

# # Используя множественное наследования можно создавать классы-миксины (примеси), 
# # представляющие собой определенную особенность поведения. Такой микси можно "примешать" к любому классу.
# # Ассоциация
# # Кроме наследования, существует и другой способ организации межклассового взаимодействия – ассоциация (агрегация или композиция),
# #  при которой один класс является полем другого.

# # Пример композиции:

# class Salary:
#     def __init__(self,pay):
#         self.pay = pay

#     def getTotal(self):
#         return (self.pay*12)

# class Employee:
#     def __init__(self,pay,bonus):
#         self.pay = pay
#         self.bonus = bonus
#         self.salary = Salary(self.pay)

#     def annualSalary(self):
#         return "Total: " + str(self.salary.getTotal() + self.bonus)

# employee = Employee(100,10)
# print(employee.annualSalary())
# # Пример агрегации:

# class Salary(object):
#     def __init__(self, pay):
#         self.pay = pay

#     def getTotal(self):
#         return (self.pay * 12)

# class Employee(object):
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus

#     def annualSalary(self):
#         return "Total: " + str(self.pay.getTotal() + self.bonus)

# salary = Salary(100)
# employee = Employee(salary, 10)
# print(employee.annualSalary())
# # Ассоциированные объекты могут циклически ссылаться друг на друга, что ломает стандартный 
# # механизм сборки мусора. Избежать подобных проблем при ассоциации помогают слабые ссылки (модуль weakref).
# # Полиморфизм
# # Концепция полиморфизма – важная часть ООП на Python. Все методы в языке изначально виртуальные. 
# # Это значит, что дочерние классы могут их переопределять и решать одну и ту же задачу разными путями,
#  #а конкретная реализация будет выбрана только во время исполнения программы. Такие классы называют полиморфными.

# class Mammal:
#     def move(self):
#         print('Двигается')

# class Hare(Mammal):
#     def move(self):
#         print('Прыгает')

# animal = Mammal()
# animal.move() # Двигается
# hare = Hare()
# hare.move() # Прыгает
# #Впрочем, можно получить и доступ к методам класса-предка либо по прямому обращению, либо с помощью функции super:

# class Parent():
#     def __init__(self):
#         print('Parent init')

#     def method(self):
#         print('Parent method')

# class Child(Parent):
#     def __init__(self):
#         Parent.__init__(self)

#     def method(self):
#         super(Child, self).method()

# child = Child() # Parent init
# child.
# method() # Parent method
# # Одинаковый интерфейс с разной реализацией могут иметь и классы, не связанные родственными узами.
# #  В следующем примере код может одинаково удобно работать с классами English и French, так как они обладают 
# #  одинаковым интерфейсом:

# class English:
#   def greeting(self):
#     print ("Hello")

# class French:
#   def greeting(self):
#     print ("Bonjour")

# def intro(language):
#   language.greeting()

# john = English()
# gerard = French()
# intro(john) # Hello
# intro(gerard) # Bonjour
# # Это возможно благодаря утиной типизации.
# # Множественная диспетчеризация
# # Виртуальные методы обеспечивают одиночную диспетчеризацию, 
# # при которой выбор конкретного метода зависит от объекта, в контексте которого произошел вызов.
# #  Мультиметоды позволяют выбирать нужную функциональность в зависимости от количества, типов или значений аргументов.
# # Программирование на Python не поддерживает мультиметоды из коробки,
# #  поэтому для их реализации необходимо подключать сторонние Python библиотеки, например, multimethods.py.
# # Порядок разрешения доступа к атрибутам
# # Складывается достаточно интересная картина: 
# # у одного объекта может быть несколько родительских классов, а также специальные методы вроде __getattribute__, 
# # которые перехватывают запросы к атрибутам.
# # Каким же образом интерпретатор разрешает сложные запросы к свойствам и методам? 
# # Рассмотрим последовательность поиска на примере запроса obj.field:
# # Вызов obj.__getattribute__('field'), если он определен. 
# # При установке или удалении атрибута проверяется соответственно наличие __setattr__ или __delattr__.
# # Поиск в obj.__dict__ (пользовательские атрибуты).
# # Поиск в object.__class__.__slots__.
# # Рекурсивный поиск в поле __dict__ всех родительских классов. Если класс имеет несколько предков, порядок проверки соответствует порядку их перечисления в определении.
# # Если определен метод __getattr__, то происходит вызов obj.__getattr__('field')
# # Выбрасывается исключение несуществующего атрибута – AttributeError.
# # Наконец, когда атрибут нашелся, проверяется наличие метода __get__ (при установке – __set__, при удалении – __delete__).
# # Все эти проверки совершаются только для пользовательских атрибутов.
# # Метаклассы
# # Метаклассы – это классы, инстансы которых тоже являются классами.

# class MetaClass(type):
#     # выделение памяти для класса
#     def __new__(cls, name, bases, dict):
#         print("Создание нового класса {}".format(name))
#         return type.__new__(cls, name, bases, dict)

#     # инициализация класса
#     def __init__(cls, name, bases, dict):
#         print("Инициализация нового класса {}".format(name))
#         return super(MetaClass, cls).__init__(name, bases, dict)

# # порождение класса на основе метакласса
# SomeClass = MetaClass("SomeClass", (), {})

# # обычное наследование
# class Child(SomeClass):
#     def __init__(self, param):
#         print(param)

# получение экземпляра класса
#obj = Child("Hello")
# Подведем краткий итог всему вышесказанному и выделим основные особенности реализации ООП на Python:
# Классы в Python – это тоже объекты.
# Допустимо динамическое изменение и добавление атрибутов классов.
# Жизненным циклом объекта можно управлять.
# Многие операторы могут быть перезагружены.
# Многие методы встроенных объектов можно эмулировать.
# Для скрытия внутренних данных используются синтаксические соглашения.
# Поддерживается наследование.
# Полиморфизм обеспечивается виртуальностью всех методов.
# Доступно метапрограммирование.

# class Car():
#     """Описание автомобиля"""
#     def __init__(self, brand, model, years):
#         """Инициализирует атрибуты"""
#         self.brand = brand
#         self.model = model
#         self.years = years
#         self.mileage = 0

#     def get_full_name(self):
#         """Автомобиль"""
#         name = f"Автомобиль {self.brand} {self.model} {self.years}"
#         return name.title()

#     def read_mileage(self):
#         """Пробег автомобиля"""
#         print(f"Пробег автомобиля {self.mileage} км.")

#     def update_mileage(self, new_mileage):
#         """Устанавливает новое значение пробега"""
#         self.mileage = new_mileage

# car_2 = Car('audi', 'a4', 2019)
# print(car_2.get_full_name())

# car_2.read_mileage()
# car_2.update_mileage(17100)
# car_2.read_mileage()


# class MyClass:
#     """docstring for MyClass"""
#     def __init__(self):
#         super(MyClass, self).__init__()

#     def ipdate_val(self, x):
#         self.val = x

#     def recieve_val(self):
#         while True:
#             x = input('Введите количество клеток в квадрате ')
#             str_x = str(x)
#             self.ipdate_val(x)
#             if x == 'stop':
#                 break
#             elif not str_x.isdigit():
#                 print ('вы ввели не число')
#             else:
#                 num = int(x)
#                 if num < 40:
#                     print ('слишком маленкое число')
#                 else:
#                     summaMassiv1 = int(num) * int(num)
#                     print ( summaMassiv1 )
#                     print ( summaMassiv1 )
                    

# obj = MyClass()

# obj.recieve_val()

# # печатаем объект
# print (obj.val)



# class Python27:
#     students = 'Amina'
#     def __init__(self) -> None:
#         super(Python27,self).__init__()
#     def amina_val(self,x):
#         self.val = x

#     def dina_val(self):
#         while True:
#             x = input('Введите имя студента ')
#             str_x = True
#             self.amina_val(x)
#             if x == 'stop':
#                 break
#             elif not str_x.isdigit():
#                 print('Такого студента нет в группе Python27')
#             else:
#                 str = int(x)
#                 if str < 0:
#                     print('Я не понимаю вас!')
#                 else:
#                     return Python27
                
# obj = Python27()
# obj.dina_val()
# p1 = Python27("Amina", "Sam")
# print(obj.val)
            
                

# class Python27:
#     def __init__(self) -> None:
#         pass


# class Person:
#     def __init__(self, n, s):
#         self.name = n
#         self.surname = s
 
 
# p1 = Person("Sam", "Baker")
# print(p1.name, p1.surname)


# class Python27:
#     def __init__(self,name,last_name) -> None:
#         self.nm = name
#         self.ln = last_name
#     def __init__(self):
#          super(Python27, self).__init__()
#     def amin_val(self, x):
#         self.a = x
        
#     def hal_val(self):
#         while True:
#             x = input ('Введите имя студента ')
#             if x == str:
#                 return 'Студент учится 2 месяц'
#             elif str != str:
#                 return 'Такого студента нет в группе'
#             else:
#                 return 'Я вас не понимаю'
          

# self.name = Python27("Sam", "Baker")     



# class WalkMixin:
#     def walk(self):
#         print("обьект ходить")

# class WalkingPerson(WalkMixin):
#     pass

# obj = WalkMixin()
# obj.walk()



#\l - показывает список база данных
# psql postgres - вход 
# create database (название база данных); - создание база данных
# drop database (название база данных);- 
# \c - коннект с другой база данных

