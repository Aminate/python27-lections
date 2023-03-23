# class Person:
#     arms = 2
#     legs = 2

#     def walk(odj): #обьект от класса,если принтить то придет  None
#         print("я хожу")
        
# person1 = Person()
# # print(person1) #<__main__.Person object
# print(type(person1))  #<class '__main__.Person'>
# print(__name__)   #__main__   
# print(dir(person1))   #'arms', 'legs', 'walk'] 
# print(person1.arms) #2
# print(person1.legs) #2
# print(person1.walk()) #TypeError: Person.walk() takes 0 positional arguments but 1 was given



# class Person:
#     arms = 2
#     legs = 2
#     name = 'Amina'
#     def __init__(self, name) -> None:
#         # __init__ - dunder (дабл андерскор) метод, который будет добавлят в обьект self атрибуты 
#         # которые отличаются у разных обьектов

#         self.name = name

#     def walk(self):
#         print(self)
#         print("я хожу")


# person1 = Person('Amina')   #(name: Any) -> None
# person2 = Person('Nurik')
# print(person1.name, person2.name)






# person1 = Person()
# Person.walk(person1)
# person1.walk()
    
# p1 = Person()
# p2 = Person()
# p3 = Person()
# print(p1.name, p2.name, p3.name)  #Amina Amina Amina
# print(dir(Person))

# self это ссылка на обьекте у которого мы вызываем данный метод


# Атрибуты класса и атрибуты обьекта класса

# class A:
#     var1 = 'переменная класса'

#     def __init__(self):
#         self.var2 = 'переменная обьекта'

# print(dir(A))  
#  #['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
#'__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
#  '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#  '__weakref__', 'var1']

# obj = A()
# print(dir(obj))
 #['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
# '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']

# print(A.var1)  #переменная класса

# print(obj.var1)  #переменная класса
# print(obj.var2)   #переменная обьекта


#инкапсуляция - когда все лежит в одной коробке 



#разбор с лекции

#синтаксис oop-
# class SomeClass:    #создание класса
#     pass 

# class A:
#     pass
# a = A()

#print(isinstance(a,A))   #isinstance- принимает обьект и typle (тоесть первый аргумент это какой-нибудь обьект
#а далее через запитую передаем второй это класс ну допустим я хочу проперить является ли 'a' обьектом от
# класса 'a')
# обьект класса или можно назвать экземпляром класса (instance-экземпляр) (object-обьект) но и то и то одно и то же

#True- что является правдой

#================= РАБОТА С ВСТРОЕННЫМИ КЛАССАМИ ==============

# print(type(int)) 
#<class 'type'>
#мы знаем что тайп определяет класс,например инт это класс тайп

#но если мы создадим переменную с интежером и запринтим выйдет класс инт, мы не видим но там внутри питона
#описаны какие то свойство этого класса. НАПРИМЕР:
# a = 4
# print(type(a)) 
#<class 'int'>

#то же самое и с другими классами

#pass - это пустота на случае если мы не знаем что наша функция будет делать, иными словами пока проспускаем,
#но когда нам станет ясно мы должны допоплнить нашу пустоту, тоесть вместо pass прописываем то что хотели


#встроенные классы или же типы данных это:
#int,str,list,tuple,dict,bool,set,frozenset #(итд)
# и весь этот класс тоже относится к классу и этот класс type
# print(type(int))
#<class 'type'> что означает класс type

# a = 5
# print(type(a))

# b = 'amina'
# print(type(b))
#<class 'str'> хранит в себе экземпляр

#Мы можем создать сопственный класс и прописать все его свойство,методы и будем знать как оно работает внутри класса
#
#например:
#__init__ это инициализатор и приминяет только 1 обьект

# class Dog:
#     name ='Django'
#     age = 3

#     def __init__(self):
#         pass

# dog1 = Dog()
# print(dog1.name) #Django
# print(dog1.age)  #3
#<__main__.Dog object at 0x102ab8ad0>  выдается такая строка что означает что наш дог1 является обьектом DOG OBJECT
#name age - являются атрибутами обьякта Dog

#но если я создам еще одну переменную с названием dog2 и запринчу то выйдет еще раз имя джанго, так как
#мы создаем один обьект и сколько бы догов не было имя будет одинаковым то же самое и с возростом
# dog2= Dog()
# print(dog2.name)

# class Person:
#     name = 'Amina'
#     lastname = 'Ashimova'
#     age = 22
#     city = 'Mocsow'
#     gender = 'girl'


#     def __init__(self):
#         pass
# per1 = Person()
# print(per1.name)
# print(per1.lastname)
# print(per1.age)
# print(per1.city)
# print(per1.gender)

# Amina
# Ashimova
# 22
# Mocsow
# girl

#так не очень та и правельно, нужно создавать атрибуты внутри инита.
#например:


# class Person:
#     name = 'Amina'
#     lastname = 'Ashimova'
#     age = 22
#     city = 'Mocsow'
#     gender = 'girl'


#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# per1 = Person(name='Amina', age=22)
# print(per1.name)
# print(per1.lastname)
# print(per1.age)
# print(per1.city)
# print(per1.gender)


#СОЗДАНИЕ КЛАССА RECTANGLE(прямоугольный)

# class Rectangle:
#     default_color = 'red'





#     def __init__(self,width, length):
#         self.width = width
#         self.length = length

#     def area(self):
#         return self.width * self.length
    

# rec1 = Rectangle(4, 6)
# rec2 = Rectangle(2, 7)
# rec2.default_color = 'yellow' #так же мы можем на ходу менять значения
# print(rec1.area()) #24
# print(rec1.width) #4
# print(rec2.area()) #14
# print(rec2.width) #2
# print(rec1.default_color) #red
# print(rec2.default_color) #red
# print(rec2.default_color)  #yellow




#СОЗДАНИЕ КЛАССА Car


# class Car:
# #тут интересное то что я хочу чтобы при каждом добавлении к машине,был счечик который добавляет 1(количество обьектов)
#     car_count = 0


#     def __init__(self):
#         Car.car_count += 1

# car1 = Car()
# print(Car.car_count)
#  #1 тут у нас сработал счечик
# car2 = Car()
# print(Car.car_count) #2
#и так каждый раз добавляется новая машина



#TASK

#1
# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_title(self):
#         return(f'Название этой песни {self.title}')

#     def show_author(self):
#         return(f'Автор этой песни{self.author}')

#     def show_year(self):
#         return(f'Эта песня вышла в {self.year} году')

# song =Song("Happier than ever", "Billie Elish", 2021)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())


#2


# class Circle: 
#     color = 'Синий' 
#     pi = 3.14 
#     def __init__(self, radius): 
#         self.radius = radius 
#     def get_area(self): 
#             return self.pi*(self.radius**2) 
# circle = Circle(radius = 13) 
# circle.color = 'желтый' 
# print(circle.color) 
# print(circle.get_area())



#3 (не окончен)

# class BankAccount: 
#     balance = 0 
#     def withdraw(self, amount): 
#      self.balance -= amount 
#      print(f'Ваш баланс:{self.balance} сом') 
#     def deposit(self,amount): 
#        self.balance += amount 
#        print(f'Ваш баланс:{self.balance} сом') 
# account = BankAccount() 
# print(account.deposit(1000)) 
# print(account.withdraw(500))


#4

# class Taxi: 
#     def __init__(self, name, cost, cost_km): 
#         self.name = name 
#         self.cost = cost 
#         self.cost_km = cost_km 
#     def get_total_cost(self, km): 
#         self.cost = self.cost_km * km + self.cost 
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом' 
# taxi1 = Taxi(name='Namba',cost=29, cost_km=15) 
# taxi2 = Taxi(name='Yandex',cost=25, cost_km=17) 
# taxi3 = Taxi(name='Jorgo',cost=28, cost_km=15) 
# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))


#5
# class Phone: 
#     def __init__(self, name, last_name, phone) -> None: 
#         self.name = name 
#         self.last_name = last_name 
#         self.phone = phone 
#     def get_info(self): 
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}') 
# contact = Phone('John', 'Snow','996707707707') 
# contact.get_info()

# class Product:
#     base_price = 20000
#     def __init__(self, model, year, color) -> None:
#         self.model = model
#         self.year = year
#         self.color = color

#     def has_garantiya(self, year):
#         if year - self.year > 2:
#             return "Ваша гарантия истекла"
#         else:
#             return "Гарантия действительна"

#     @classmethod
#     def change_price(cls,rate):
#         cls.base_price += cls.base_price * rate / 100
#         return cls.base_price

# obj = Product('A218', 2008, 'red') 
# obj.change_price(2) 
# print(obj.has_garantiya(2015)) 
# print(obj.base_price) 



#   Task 3

# class BankAccount: 
#     balance = 0 
#     def withdraw(self, amount): 
#         self.balance -= amount 
#         print(f'Ваш баланс: {self.balance} сом') 
#     def deposit(self,amount): 
#         self.balance += amount 
#         print(f'Ваш баланс: {self.balance} сом') 
# account = BankAccount() 
# print(account.deposit(1000)) 
# print(account.withdraw(500))

# Task 6

# class Salary: 
#     percent = 8 
#     def __init__(self, salary, experience): 
#         self.salary = salary 
#         self.experience = experience 
#     def count_percent(self): 
#         return self.salary * self.percent / 100 * self.experience 
# obj = Salary(1000, 8) 
# print(obj.count_percent())

# Task 7
# import datetime 
# class Nobel(): 
#     def __init__(self, category, year, winner) -> None: 
#         self.category = category 
#         self.year = year 
#         self.winner = winner 
#     def get_year(self): 
#         a = str(datetime.date.today()).split('-')[0]
#         res = int(a) - self.year 
#         return f'выиграл {res} лет назад' 
# winner1 = Nobel("Литература", 1970, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())
# winner2 = Nobel("Литература", 1993, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

#(решение от Дины)stupit madafucka

# import datetime
# now = datetime.datetime.now()
# now2 = str(now).split()[0].split('-')[0]
# date_now = int(now2)

# class Nobel:
#     def init(self, category, year, winner):
#         self.category = category 
#         self.year = year
#         self.winner = winner
#     def get_year(self):
#         return f'выиграл {date_now - self.year} лет назад'
# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())



# Литература 1971 Пабло Неруда
# выиграл 51 лет назад 
# Литература 1994 Кэндзабуро Оэ 
# выиграл 28 лет назад