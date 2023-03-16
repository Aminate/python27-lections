# # class Dog:
# #     def speak(self):     #speak - это один интерфейс 
# #         print("гав гав")


# # class Cat:
# #     def speak(self):
# #         print("мяу-мяу")

# # class Frog:
# #     def speak(self):
# #         print("ква ква")


# # animals = [Cat(), Frog(), Dog(), Cat(), Frog(), Dog()]
# # for animal in animals:
# #     animal.speak()
# # # мяу-мяу
# # # ква ква
# # # гав гав
# # # мяу-мяу
# # # ква ква
# # # гав гав  
# # print(animal) #<__main__.Dog object at 0x1027794d0>




# list1 = [1,2,3,4,5]
# dict1 = {"a": 1, "b": 2}

# list1.pop(0)  #удаление по индексу
# dict1.pop("a") #удаление по ключу

# # например тут метод поп удаляет но в первом примере по индексу а во втором по ключу, один метод работает по разному



# # 1 + 5
# # "a" + "b"

# # __add__
# # складывает  и возвращает новый список

# a = 4
# b = 3
# print(a+b)  #7
# print(a.__add__(b))  #7

# a = [1,2,3]
# b = [4,5,6]
# print(a.__add__(b))   #[1, 2, 3, 4, 5, 6]


# #__len__

# a = 'abc'
# print(len(a))
# print(a.__len__())

# b = [1,2,3[4,5,6]]
# print()



#РАЗБОР С ЛЕКЦИИ
#Пример полиморфизма в операторе +

# a = 9
# b = 9
# print(a+b)  #18
# c ='6'
# d = '1'
# print(c+d)  #61
#так как переменные c и d считаются классом стринг

# f = [4,5,1,3]
# e = [6,8,2,9]
# print(f + e)  #[4, 5, 1, 3, 6, 8, 2, 9]

#во всех случаях мы использовали оператор + но получили разный результат, это зависит от того какие обьекты классов мы
# использовали

#dir()

# a = 'amina'
# b = 1
# c = [True, 'joji', 69]
# d = {'abracadabra':'potter'}
# e = [1,2,3]
# f = {False, 'suka', 6, 8, 9}
# print(f"This is string methods: {dir(a)}")
# print(f"This is integer methods: {dir(b)}")
# print(f"This is list methods: {dir(c)}")
# print(f"This is dict methods: {dir(d)}")
# print(f"This is tuple methods: {dir(e)}")
# print(f"This is set methods: {dir(f)}")
#короче при принте оно покажет нам всю хуйню которая входит в этот метод, показывает что в различных классах есть 
#различные методы, и прикол в том что один метод может входить в нес-ких классах

# Полиморфизм на примере встроенных методов:

#есть же методы которые делают различную хуйню тоесть разнарабочие:
#pop() -> list, dict, set
# list_ =[3,4,5,6]
# dict_ = dict(a=1, b=2, c=3)
# set_ = {True, 'abracadabra', 90, 0}

# list_.pop(0)
# dict_.pop('a')
# set_.pop()

# print(list_)  #[4, 5, 6]
# print(dict_)  #{'b': 2, 'c': 3}
# print(set_)   #{True, 90, 'abracadabra'}



#update() -> dict, set

# dict_ = dict(a=1, b=2, c=3)
# set_ = {True, 'abracadabra', 90, 0}

# dict_.update(d=4, e=5)
# set_.update({8, 5, -3})
# print(dict_)   #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# print(set_)   #{0, True, 'abracadabra', 5, 8, 90, -3}


# Одним из самых распространенных примеров полиморфизма в Python является оператор + . 
# Напишем простую функцию, складывающую два параметра:
# def add(x, y): 
#     print(x + y) 



#Task 1(polimorfizm)
#короче прикол в том что у меня есть список,строка,словарь и мне нужно посчитать длину всех разом.
# так что ж я делаю беру и создаю еще одну переменную (f) и запихну туда все три (a,b,c) и потом там прохожу
# по циклу(круто? -очень круто)
# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'}  
# f = [a,b,c] 
# for i in f: print(len(i))
#результат:
# 11
# 6
# 3


# Task 2

# class Dog:
#     def voice(self):    
#         print("Гав")


# class Cat:
#      def voice(self):
#         print("Мяу")

# def to_pet(obj):
#     return obj.voice()
    

# rex = Dog()
# barsik = Cat()

# to_pet(barsik) 
# to_pet(rex) 

# class Person: 
#     def __init__(self,name,last_name): 
#         self.name = name 
#         self.last_name = last_name 
#     def get_info(self): 
#         return f'Привет, меня зовут {self.name} {self.last_name}.' 
# class Employee(Person): 
#     def __init__(self,work,status, name, last_name):
#         super().__init__(name,last_name) 
#         self.work = work 
#         self.status = status 
#     def get_info(self): 
#         return f'Привет, меня зовут {self.name} {self.last_name} я работаю в компании {self.work} на должности {self.status}.' 
# class Student(Person): 
#     def __init__(self,university,cource, name, last_name): 
#         super().__init__(name,last_name) 
#         self.university = university 
#         self.cource = cource 
#     def get_info(self): 
#         return f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.cource}.' 
# person = Person('Иван', 'Петров') 
# employee = Employee('Рога и Копыта', 'директор','Иван', 'Петров') 
# student = Student('КГТУ', '3 курсе','Иван', 'Петров') 
# def get_human_info(object): print(object.get_info()) 


# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person)



# class Person:
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name
    
#     def get_info(self):
#         return(f'Привет меня зовут{self.name} {self.last_name}')

# class Employee(Person):
#     def __init__(self,work,status,name,last_name):
#         super().__init__(name,last_name) 
#         self.work = work
#         self.status = status
#     def get_info(self):
#         return f'Привет,меня зовут {self.name} {self.last_name} я работаю в компании {self.work} на должности{self.status}.'
# class Student(Person):
#     def __init__(self,name,last_name,university,cource):
#         super().__init__(name, last_name)
#         self.university = university
#         self.cource = cource
#     def get_info(self):
#         return f'Привет,меня зовут{self.name}{self.last_name}, я учусь в {self.university} на {self.cource}.'
# person = Person('Иван','Петров')
# employee = Employee('Рога и Копыта', 'директор','Иван','Петров')
# student = Student('КГТУ', '3 курсе', 'Иван','Петров')
# def get_human_info(object):
#     print(object.get_info())

# get_human_info(employee)
# get_human_info(student)
# get_human_info(person)
#правельное решение:

# class Person:
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}')

# class Employee(Person):
#     def __init__(self,name,last_name,work,status):
#         super().__init__(name,last_name)
#         self.work = work
#         self.status = status
#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}')

# class Student(Person):
#     def __init__(self,name,last_name,university,course):
#         super().__init__(name,last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе')

# def get_human_info(func1):
#     return func1.get_info() 

# person = Person('ivan', 'petrov')
# employee = Employee('ivan', 'petrov', 'roga i kopyta', 'direktor')
# student = Student('ivan', 'petrov', 'kgtu', 3)

# get_human_info(person) 
# get_human_info(employee) 
# get_human_info(student)


# Task 4

# from abc import ABC, abstractmethod 
# from math import pi 
# class Shape(ABC): 
#     @abstractmethod 
#     def get_area(self): 
#         pass 
# class Triangle(Shape): 
#     def __init__(self, base, height): 
#         self.base = base 
#         self.height = height 
#     def get_area(self): 
#         return self.base * self.height * 0.5 
# class Square(Shape): 
#     def __init__(self, length): 
#         self.length = length 
#     def get_area(self): 
#         return self.length ** 2 
# class Circle(Shape):
#      def __init__(self, radius): 
#          self.radius = radius 
#      def get_area(self): 
#         return pi * self.radius ** 2 
# triangle = Triangle(5, 5) 
# square = Square(5) 
# circle = Circle(4) 
# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area())

#Task 5


# class OS:
#     def __init__(self,version):
#         self.version = version

# class Windows(OS):
#     def copy(self,text):
#         # self.text = text
#         return f'скопирован текст "{text}" горячими клавишами CTRL + C'
    
# class MacOS(OS):
#   def copy(self,text):
#       return f'скопирован текст "{text}" горячими клавишами COMMAND + C'
  
# class Linux(OS):
#  def copy(self,text):
#     return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'
 
# win = Windows('10')
# mac =   MacOS('Big Sur')
# lin = Linux('Ubutu')
# print(win.copy('Полиморфизм — одна из основных парадигм ООП')) 

#Task 6

# class Language:
#     def __init__(self,level,type):
#         self.level = level
#         self.type = type

# class Python(Language):
#     def write_function(self,func_name,arg):
#         self.func_name = func_name
#         self.arg = arg
#         return f"def {func_name}({arg}):"

#     def create_variable(self,var_name,value):
#         self.var_name = var_name
#         self.value = value
#         if isinstance(value, str):
#              return f"{var_name} = '{value}'"
#         else:
#             return f"{var_name} = {value}"
        
# class JavaScript(Language):
#     def write_function(self, func_name, arg): 
#         self.func_name = func_name
#         self.arg = arg
#         return f"function {func_name}({arg}) {{ }};" 
#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             return f"let {var_name} = '{value}';"
#         else:
#             return f"let {var_name} = {value};"

# py = Python('Intermediate', 'Backend')
# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))
# js = JavaScript('Advanced', 'Frontend') 
# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', 'john@123'))


#   Task 7
# class Money:
#     def __init__(self,country,symbol):
#         self.country = country
#         self.symbol = symbol
# class Dollar(Money):
#     rate = 84.80
#     def exchange(self, amount):
#         return f"$ {amount} равен {Dollar.rate * amount} сомам" 

# class Euro(Money):
#     rate = 98.40
#     def exchange(self, amount): 
#         return f"€ {amount} равен {Euro.rate * amount} сомам" 
# dol = Dollar('Alaska', '$') 
# eu = Euro('France', '€') 

# print(dol.exchange (100)) 
# print(eu.exchange (80))

#Task 8
# class Planet: 
#     def __init__(self, orbit): 
#         self.orbit = orbit 
# class Mercury(Planet):
#    def get_age(self, earth_age):
#         return f'на Меркурии ваш возраст составляет {int(earth_age * 365 /self.orbit)} лет' 

# class Venus(Planet):
#     def get_age(self, earth_age): 
#          return f'на Венере ваш возраст составляет {round(earth_age * 365 / self.orbit * 365)} дней' 
    
# class Jupiter(Planet):
#     def get_age(self, earth_age):
#         return f'на Юпитере ваш возраст составляет {round(earth_age * 365 // self.orbit * 365 * 24)} часов' 

# mercury = Mercury(88) 
# venus = Venus(225) 
# jupiter = Jupiter(12) 
# print(venus.get_age(20)) 
# print(jupiter.get_age(20)) 
# print(mercury.get_age(20))