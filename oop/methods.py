# class A:
#     def instance_method(self):
#         print("метод обьекта") #метод обьекта
#         print("self",self)  #self <__main__.A object at 0x102a34bd0>

# obj = A() #создание обьекта класса
# obj.instance_method()
# #когда мы вызываем метод у обьекта, то нам не нужно передовать его в self,
# # он передается автоматически

# A.instance_method(obj)
# # метод обьекта
# # self <__main__.A object at 0x104f48dd0>
# #Когда мы вызываем метод у класса, то нам нужно передавать обьект

# A.instance_method(7) #self 7 не совсем правельный вызов 


# class Amina:
#     @classmethod  #задекарировали
#     def class_method(cls):
#         print("метод класса")
#         print("cls", cls)


# Amina.class_method()  #метод класса
# #cls <class '__main__.Amina'>


# obj = Amina()
# obj.class_method()
# # метод класса
# # cls <class '__main__.Amina'>
# #все равно от куда мы будем вызывать classmethod (от обьекта или класса)
# # первым аргументом будет приходить класс

# # примеры:
# class C:
#     counter = 0
#     def __init__(self):
#         #обьект создается
#         # Counterr.counter += 1
#         self._inc_counter()

#     def __del__(self):
#         #обьект удаляется
#         # Counterr.counter -= 1
#         self._dec_counter()

#     @classmethod
#     def _inc_counter(cls):
#         #cls = class C
#         #увеличиваем атрибут класса counter на один
#         cls.counter += 1

#     @classmethod
#     def _dec_counter(cls):
#         cls.counter -= 1
#         # уменьшаем на один

# obj1 = C()
# obj2 = C()
# obj3 = C()
# obj4 = C()
# print(C.counter) #4
# del obj4
# print(C.counter) #3
# #через запитую можно удалить несколько обьектов (obj1, obj2)

# class Pizza:
#     def __init__(self, radius, *ingridients):   # * - много можем 
#         self.r = radius
#         self.ingridients = ingridients

#     def cook(self):
#         print(f"Пицца размером {self.r * 2}")
#         print(f"Ингридиенты: {self.ingridients}")

#     @classmethod
#     def four_cheeze(cls, radius):
#         pizza = cls(radius, "1 cheeze", "2 cheeze", "3 cheeze", "4 cheeze")
#         return pizza

    

# pizza1 = Pizza(15, "Сыр", "Колбаса", "Помидоры")
# pizza1.cook()
# # Пицца размером 30
# # Ингридиенты: ('Сыр', 'Колбаса', 'Помидоры')

# pizza2 = Pizza(10, "1 cheeze", "2 cheeze", "3 cheeze", "4 cheeze")
# pizza2.cook()
# # Пицца размером 20
# # Ингридиенты: ('1 cheeze', '2 cheeze', '3 cheeze', '4 cheeze')
# # метод который создает несколько - но 
# pizza4 = Pizza.four_cheeze(10)
# pizza4.cook()

# # pizza5 = Pizza.four_cheeze(15)
# # pizza5.cook()
    


#     #Nastya:
# class A:
#     def instance_method(self):
#         print("метод обьекта")
#         print("self", self)

# obj = A()
# obj.instance_method()
# # метод обьекта
# # self <__main__.A object at 0x10054ccd0>
# # когда мы вызываем метод у обьекта, то нам не нужно передавать его в self, он передается автоматически

# A.instance_method(obj)
# # метод обьекта
# # self <__main__.A object at 0x10054ccd0>
# # когда мы вызываем метод у класса, то нам нужно передавать обьект



# class A:
#     @classmethod
#     def class_method(cls):
#         print("метод класса")
#         print("cls", cls)

# A.class_method()
# # метод класса
# # cls <class '__main__.A'>

# obj = A()
# obj.class_method()
# # метод класса
# # cls <class '__main__.A'>

# # все равно от куда вы будете вызывать classmethod (от обьекта или класса), первым аргументом будет приходить class



# # примеры
# class C:
#     counter = 0

#     def __init__(self):
#         # обьект создается
#         # C.counter += 1
#         self._inc_counter()

#     def __del__(self):
#         # обьект удаляется
#         # C.counter -= 1
#         self._dec_counter()

#     @classmethod
#     def _inc_counter(cls):
#         # cls - class C
#         # увеличиваем аттрибут класса counter на один
#         cls.counter += 1
    
#     @classmethod
#     def _dec_counter(cls):
#         cls.counter -= 1


# obj1 = C()
# obj2 = C()
# obj3 = C()
# obj4 = C()
# print(C.counter) # 4
# del obj1
# print(C.counter) # 3



# class Pizza:
#     def __init__(self, radius, *ingredients):
#         self.r = radius
#         self.ingredients = ingredients

#     def cook(self):
#         print(f"Пицца размером {self.r * 2}")    
#         print(f"Ингридиенты: {self.ingredients}")
    
#     @classmethod
#     def four_cheeze(cls, radius):
#         pizza = cls(radius, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
#         # pizza = Pizza(15, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
#         return pizza

# pizza1 = Pizza(15, "Сыр", "Колбаса", "Cherry")
# pizza1.cook()

# pizza2 = Pizza(10, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
# pizza2.cook()

# pizza3 = Pizza(15, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
# pizza3.cook()

# pizza4 = Pizza.four_cheeze(10)
# pizza4.cook()

# pizza5 = Pizza.four_cheeze(15)
# pizza5.cook()




# class A:
#     @staticmethod
#     def static_method():
#         print("статик метод")

# obj = A()
# obj.static_method()


# class Cylinder:
#     def __init__(self, diameter, height):
#         self.di = diameter
#         self.h = height
#         self.area = self.get_area(diameter, height)

#     @staticmethod
#     def get_area(di, h):
#         from math import pi
#         circle_area = pi * di**2 / 4
#         side_area = pi * di * h
#         return circle_area*2 + side_area

# cylinder1 = Cylinder(4, 10)
# print(cylinder1.area)

# print(Cylinder.get_area(4, 10))
# # мы не создали обьект, но получили нужные нам расчеты





# def get_area_cylinder(di, h):
#     from math import pi
#     circle_area = pi * di**2 / 4
#     side_area = pi * di * h
#     return circle_area*2 + side_area

# print(get_area_cylinder(4, 10))



# Task 1
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

# class Python27:
#     base_salary = 300
#     def __init__(self,name,age,laptop,hour) -> None:
#         self.name = name
#         self.age = age
#         self.laptop = laptop
#         self.hour = hour

#     def working_hours(self,hour):
#         if hour - self.hour > 2:
#             return "Вы слишком долго работаете"
#         else:
#             return "Вы наняты на работу"
        
#     @classmethod
#     def change_price(cls,rate):
#         cls.base_salary += cls.base_salary * rate / 100
#         return cls.base_salary
    
# obj = Python27('Amina', 5, 'girl', 9) 
# obj.change_price(2) 
# print(obj.working_hours(2)) 
# print(obj.base_salary) 


# Task 2
# class User:
#     def __init__(self, name, lastname, email):
#         self.name = name
#         self.lastname = lastname
#         self.email = email

#     @staticmethod
#     def validate_email(email):
#         return '@' in email

#     @classmethod
#     def create_user(cls, user_string):
#         name, lastname, email = user_string.split(', ')
#         return cls(name, lastname, email)

#     def __str__(self):
#         if self.validate_email(self.email):
#             return f"{self.name}: {self.email}"
#         else:
#             return "email в неправильном формате"


# user1 = User.create_user('John, Snow, john@gmail.com')
# user2 = User.create_user('Alice, Smith, alice#smith.com')

# print(user1)
# print(user2) 
# class User:
#     def __init__(self,name, email):
#         self.name = name
#         self.email = email


#     def get_info(self):
#         return f"{self.name}, {self.email}"
    
#     @classmethod
#     def add_data(cls, user_info:list):
#         name = user_info
#         email = user_info
#         return cls(name,email)


# list_of_users = [
#     ['Amina','aminuwko@gmail.com'
#      'Sofya', 'sofiyanna2mail.com'
#      'Halima', 'holly@mail.com']
# ]


# for info in list_of_users:
#     user = User.add_data(info)
    # print(user.get_info())


#user1 = User(name='Amina', email='aminuwko@gmail.com')
#print(user1.get_info())  #Amina, aminuwko@gmail.com

# class SomeClass(object):
#     @staticmethod
#     def hello():
#         print("Hello, world")

# SomeClass.hello() # Hello, world
# obj = SomeClass()
# obj.hello() # Hello, world

# class SomeClass(object):
#     def __new__(cls):
#         print("new")
#         return super(SomeClass, cls).__new__(cls)

#     def __init__(self):
#         print("init")

# obj = SomeClass()
#new
#init

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


# Task 3
# class Makers:
#     student_count=0
#     def __init__(self,name,language,kpi):
#         self.name = name
#         self.language = language
#         self.kpi = kpi

#     @classmethod
#     def new_student(cls,name,language,kpi):
#         cls.student_count+=1
#         return cls(name,language,kpi)
        
#     def get_info(self):
#         return f"Student name: {self.name}, Language: {self.language}"
    
#     def set_kpi(self,kpi):
#         self.kpi = kpi
#         return self.kpi

# student1 =Makers.new_student("Marat","JS",'89')
# student2 =Makers.new_student("Oleg", "Python",'55')
# print(student1.set_kpi(89)) 
# print(student1.get_info()) 
# print(student2.set_kpi(89)) 
# print(student2.get_info()) 
# print(Makers.student_count)


# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# #result = dict(sorted(d.items(), key=operator.itemgetter(1)))
# result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
# print(result)


#Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
# import collections

# text = 'lorem ipsum dolor sit amet amet amet'
# words = text.split()
# counter = collections.Counter(words)
# most_common, occurrences = counter.most_common()[0]

# longest = max(words, key=len)
# print(most_common, longest)

# import collections
# text = 'amina clean drink amina see your eays'
# words = text.split()
# counter = collections.Counter(words)
# most_common, occurrences = counter.most_common() [0]
# longest = max(words, key=len)
# print(most_common, longest)
#amina amina


# Task 4
# class Bike:
#     def __init__(self, cost, make, model, year, min_profit):
#         self.cost = cost #стоимость
#         self.make = make #производитель
#         self.model = model #модель
#         self.year = year #год
#         self._sale_price = None #цена для продажи
#         self.sold = False #продан или нет
#         self.min_profit = min_profit #мин.прибыль


#     def set_cost(self, sale_price):
#         if sale_price < self.cost:
#             self._sale_price = sale_price + self.min_profit
#         else:
#             self._sale_price = sale_price

#     def service(self, cost):
#         self._sale_price += cost
#         return self._sale_price

#     def sell(self):
#         self.sold = True
#         profit = self.cost - self._sale_price
#         return profit

#     @classmethod
#     def get_default_bike(cls, cost=10000, make='Author', model='Basic ASL', year=2020, min_profit=2000):
#         return cls(cost, make,model, year, min_profit)

    
# bike = Bike.get_default_bike() 
# bike.set_cost(6000) 
# bike.service(300) 
# print(bike.sell()) 
# print(bike.cost) 
# print(bike.make) 
# print(bike.year) 
# print(bike._sale_price) 
# print(bike.sold) 
# print(bike.min_profit)

# Task 5
# def dollarize(float_num):
#   if float_num>=0:
#     return "${:,.2f}".format(float_num)
#   else:
#     return "-${:,.2f}".format(-float_num)

# class MoneyFmt:
#   def __init__(self, amount):
#     self.amount = amount

#   def update(self, new_value):
#     self.amount = new_value
#     return self.amount

#   def __repr__(self):
#     return str(self.amount)

#   def __str__(self):
#     return dollarize(self.amount)

# cash = MoneyFmt(12345678.021)
# print(cash)
# cash.update(100000.4567)
# print(cash)
# cash.update(-0.3)
# print(cash)
# print(repr(cash)) 

# def dollarize(float_num):
#   if float_num>=0:
#     return "${:,.2f}".format(float_num)
#   else:
#     return "-${:,.2f}".format(-float_num)

# class MoneyFmt:
#   def __init__(self, amount):
#     self.amount = amount

#   def update(self, new_value):
#     self.amount = new_value
#     return self.amount

#   def __repr__(self):
#     return str(self.amount)

#   def __str__(self):
#     return dollarize(self.amount)

# cash = MoneyFmt(12345678.021)
# print(cash)
# cash.update(100000.4567)
# print(cash)
# cash.update(-0.3)
# print(cash)
# print(repr(cash)) 

# class MoneyFmt:
#     def _init_(self,amout):
#         self.amout = amout

#     @staticmethod
#     def dollarize(float_num):
#         if float_num>=0:
#             return "${:,.2f}".format(float_num)
#         else:
#             return "-${:,.2f}".format(-float_num)
#     def update(self, new_value):
#         self.amount = new_value
#         return self.amount

#     def __repr__(self):
#       return str(self.amount)

#     def __str__(self):
#        return (self.amount)

# cash = MoneyFmt(12345678.021)
# print(cash)
# cash.update(100000.4567)
# print(cash)
# cash.update(-0.3)
# print(cash)
# print(repr(cash))  




# class MoneyFmt:
#     def _init_(self,amout):
#         self.amout = amout

#     @staticmethod
#     def dollarize(float_num):
#         float_num = round(float_num, 2)
#         if float_num>=0:
#             return f"${float_num:,}"
#         float_num = abs(float_num)
#         return f"-${float_num: ,}"
    
#     def update(self, new_amount):
#         self.amount = new_amount

#     def __repr__(self):
#         return str(self,amount)
    
#     def 

# правельное решение
# class MoneyFmt:
#     def __init__(self,amount):
#         self.amount = amount

#     @staticmethod
#     def dollarize(float_num):
#         if float_num>=0:
#             return "${:,.2f}".format(float_num)
#         else:
#             return "-${:,.2f}".format(-float_num)
#     def update(self, new_value):
#         self.amount = new_value
#         return self.amount

#     def __repr__(self):
#         return str(self.amount)

#     def __str__(self):
#         return self.dollarize(self.amount)

# cash = MoneyFmt(12345678.021)
# print(cash)
# cash.update(100000.4567)
# print(cash)
# cash.update(-0.3)
# print(cash)
# print(repr(cash))  


# Разбор тасков
# 1 - создайте класс pasport, в котором есть сле-щее атрибуты
# 1) атрибут класса users images в котором хранится пустой список, и атрибут класса black_list - тоже пустой список
# 2) атрибуты экземпляра класса при инициализации обьекта name, list_name, date_of_birth, image, INN
#(NN при создании обьекта равен None)
# Метод check_dublicate_person который при вызове через созданный обьект класса заносит атрибут данного обьекта 
# image в список users_image если такой фотки еще нет если же она уже есть те если чел с такой фоткой уже есть в 
# базе данных то этот обьект - чел через который мы вызвали данный метод, заносит в чс


# class Passport:
#     users_images = []
#     black_list = []

#     def __init__(self,name,last_name,date_of_birth,image) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.date_of_birth = date_of_birth
#         self.image = image
#         self.INN = None

#     def __repr__(self) -> str:
#         return f"{self.name} {self.last_name}"

#     def check_dublicate_person(self):
#         if self.image in self.__class__.users_images:
#             self.__class__.black_list.append(self)
#         else:
#             self.__class__.users_images.append(self.image)

#     @staticmethod
#     def _generate_inn():
#         import random
#         return random.randrange(19999,1999999)
    


#     def get_inn(self):
#         if not self in self.__class__.black_list:
#             self.INN = self._generate_inn()
#             return f"{self.name}{self.INN}"
#         else:
#             return 'Для обьекта черного списка INN не генерируется'
        

# person1 = Passport('Amina','Ashimova','12/12/1990','amina.jpg')
# person2 = Passport('Aihan','Sayanov','12/12/1990','amina.jpg')
# person3 = Passport('Yasin','Tarasoba','12/12/1990','amina.jpg')
# person4 = Passport('Halima','Kerimova','12/12/1990','amina.jpg')
# person5 = Passport('Sofiya','Imanova','12/12/1990','amina.jpg')
# person6 = Passport('Maryam','Ulyanova','12/12/1990','amina.jpg')
# person7 = Passport('amina','Zakirova','12/12/1990','amina.jpg')

# for person in [person1, person2, person3, person4, person5, person6, person7]:
#     person.check_dublicate_person()
#     print(person.get_inn())

# print(Passport.users_images)
# print(Passport.black_list)
