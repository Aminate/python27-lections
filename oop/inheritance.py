# class A:
#     def method(self):
#         print("метод в классе А")

# obj_a = A()
# obj_a.method()
# #метод в классе А

# class B(A):
#     pass

# obj_b = B()
# obj_b.method()
# #метод в классе А


# obj_b = B()
# obj_b.method()
# #метод в классе А



# class C(A):
#     def method(self):
#         print("метод в классе С")

# obj_c = C()
# obj_c.method()
#метод в классе С


# class A:
#     def method(self):
#         print("метод в классе А")
#         return "aaa"
    
# class B(A):
#     def method(self):
#         print("метод в классе Б")
#         return_from_super=super().method()
#         print("super().method() вернул", return_from_super)
#         return "BBB"
    
# obj_a =A()
# res_a = obj_a.method()
# print("A.method вернул" , res_a)
    
# #     метод в классе А
# # A.method вернул aaa

# obj_b = B()
# res_b = obj_b.method()
# print("B.method вернул", res_b)

# class Range:
#     def create(self, num):       #create - принимает число
#         """Принимает число и возвращает список чисел от 0 до данного
#         числа включительно"""
#         return list(range(num+1))
    
# class Range10(Range):
#     def create(self):
#         """этот метод возвращает список чисел от 0 до 10 включительно"""
#         return super().create(10) #позволяет обращатся к родителю
   
    
# range_obj = Range()
# res = range_obj.create(5)
# print(res)
# # #[0, 1, 2, 3, 4, 5]


# range10_obj = Range10()
# res = range10_obj.create()
# print(res)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# class A:
#     alone1 ='a'
#     def method(self):
#         print("Метод в классе A")

# class B:
#     alone2 = 'b'

#     def method(self):
#         print("Метод в классе B")

# class C(A,B):
#     pass

# obj_c = C()

# print(obj_c.alone1) #a
# print(obj_c.alone2) #b
# obj_c.method()
#Метод в классе A потому что она стоит первым

#метод для (MRO) порядок поиска методов (method resolution or der) 


# print(C.mro())
#[<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>]

#перекрестное наследование

# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     pass
# class D(B,A):
#     pass
# class  E(C,D):
#     pass
#TypeError: Cannot create a consistent method resolution
#order (MRO) for bases A, B

# class Polygon:
#     width = 0
#     height = 0
#     def set_values( self, width, height):
#         Polygon.width = width
#         Polygon.height = height

# class Rectangle(Polygon):
#     def area(self):
#         return self.width * self.height

# class Triangle(Polygon):
#     def area(self):
#         return(self.width * self.height) / 2

# rect = Rectangle()
# trey = Triangle()

# rect.set_values(4, 5)
# trey.set_values(4, 5)

# print('Rectangle Area:', rect.area())
# print('Triangle Area:', trey.area())

# Rectangle Area: 20
# Triangle Area: 10.0

#РАЗБОР С ЛЕКЦИИ

#НАСЛЕДОВАНИЕ

# inheritance - наследование
#создание родительского и дочернего класса(синтаксис):
#РОДИТЕЛЬСКИЙ КЛАСС НЕ ОТ ЧЕГО НЕ ЗАВИСИТ
# class Parent: #(круглые скопки не ставится так как он является родительским)
#     pass

# class Child(Parent):
#     pass   #нужно запомнить что каким бы классом чтото не наследовалось корень всегда остается(obj)


#еще пример:
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass      #тут в теле классов нечего нет

# isinstance(obj, class) - проверяет является ли класс экземпляром какого то обьекта, тоесть принимает в себя первым аргументом
# обьект а вторым класс
#например:
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass 
# peremennnaya = C()
# print(isinstance(peremennnaya,A))     
#True
#нам выдали true да и вправду с явл обьектом A


#НАСЛЕДОВАНИЕ МЕТОДОВ И АТРИБУТОВ НА ПРИМЕРАХ

#с примером многоугольника

# class Polygon:
#     sides = 'many' #короче сказала чтобы many добавлялась всегда когда принт вывожу

#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs  
#         # print(self.args)
#         # print(self.kwargs)
# # (8, 9, 3)
# # {}

#     def get_perimeter(self):
#         if self.args:
#             return sum(self.args)
#         elif self.kwargs:
#             return sum(self.kwargs.values())
        
# poligon1 = Polygon (8, 9, 3) # позиционные аргументы
# poligon2 = Polygon(a=9, b=8, c=10, d=9, e=5) #именнованные

# print(poligon1.get_perimeter())
# #20
# print(poligon1.sides)
# #41
# #many
# # ==================(не поняла вообще)

# print(poligon2.get_perimeter())
# #20
# print(poligon2.sides)


#переопределение методов и атрибутов

#встроенные классы(int, tuple, dict, list, bool, str, set, frozenset)
#как можно переопределить метод?(например в словарях(dict))

# class MyDict(dict):
#     def get(self, key, default='Amina'):   #get-получаем значение по ключу
#         print('She so cool girl')
#         return dict.get(self, key, default)

# dict1 = dict(a=3, b=5, c=8)
# print(dict1.get('d'))

# dict2 = MyDict(a=3, b=5, c=8)
# print(dict2.get('d'))

# None
# She so cool girl
# Amina



# class Person:
#     def __init__(self, name, last_name, id_num):
#         self.name = name
#         self.last_name = last_name
#         self.id = id_num

#     def get_info(self):
#         print(f'{self.name} {self.last_name}, id:{self.id}')

# class Employee(Person):
#     def __init__(self, name, last_name, id_num,position, salary):
#         Person.__init__(self,name,last_name,id_num)
#         self.position = position
#         self.salary = salary

#     def get_info(self):
#         Person.get_info(self)
#         print(f'She works as{self.position} and his salary is {self.salary}')

# employee = Employee(name='Amina', last_name='Ashimova', id_num=9958552854, position='barista', salary=90000)

# employee.get_info()
#Amina Ashimova, id:9958552854
#She works asbarista and his salary is 90000

#super - возвращает все методы из родительского класса и не обезательно записывать self
#так как она на прямую заходит к родительскому классу

# class Nurgul:
#     eyes = 'asian'

#     def hands(self):
#         print('moms hands')

# class Amina(Nurgul):
    
#     def hands(self):
#         super().hands()
#         return 'dads hands'

# a = Amina()
# print(a.hands())



#Наследование позволяет нам не повторяться и делает наш код более организованным. Давайте рассмотрим простой пример:

# class Parent: 
#      def __init__(self): 
#          pass 

#      def method(self): 
#          return 'Метод класса Parent' 

# class Child(Parent): 
#      pass

# для того чтобы наследовать класс Child от класса Parent, после названия Child, в скобках прописываем название 
# класса от которого наследуем - class Child(Parent).
# Теперь все методы и свойства которые есть у Parent, будут доступны в Child:

# obj = Child() 
# print(obj.method()) 
# распечатает в терминале:

# Метод класса Parent 
# несмотря на то, что мы создали объект obj от класса Child, внутри которого данного метода нет.

# Дочерние классы могут наследовать методы от родительских и переопределять(изменять) 
# их внутри своего класса и при этом это никак не повлияет и не изменит сам родительский класс.


# Task 1


# class Dad:
#     def first(self):
#         print("Aihan is first child")
#     def second(self):
#         print("Yasin is second child ")
# class Dad2(Dad):
#     def third(self):
#         print("Amina is third child")
#     def fourth(self):
#         print("Halima is fourth child")

# obj = Dad2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()

#Task2
# class A:
#     def method1(self): 
#         print('Основной функционал') 
# class B(A): 
#     def method1(self): 
#         super().method1() 
#         print('Дополнительный функционал') 
# obj = B() 
# obj.method1()


# class Amina:
#     def method(self):
#         print('Основная работа')
# class Sofya(Amina):
#     def method(self):
#         return super().method()
#     print('Помощница')
# obj =Sofya()
# obj.method()


#Помощница
#Основная работа


#Task 3
# class Number(int): 
#      def __init__(self, value): 
#          self.value = value
    
#      def count_digits(self): 
#          digits = len(str(self.value)) 
#          return digits 
# num = Number(123) 
# print(num.count_digits()) 
#3
#т.к цифр в числе 123 - три.


#Task 4

# class MyDict(dict): 
#     def get(self,key,default = 'Are you kidding?'): 
#         return dict.get(self,key,default) 
# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some'))



# class TomHardy(dict):
#     def get(self,key,default = 'Do you want me?'):
#         return dict.get(self,key,default)
# obj_dict = TomHardy({'some_title': 2})
# print(obj_dict.get('some'))

#Task 5

# class Person: 
#     def __init__(self,name, age): 
#         self.name = name 
#         self.age = age
#     def display(self): 
#         return f'name:{self.name}, age:{self.age}' 
# class Student(Person): 
#     def __init__(self, name, age, faculty): 
#         super().__init__(name, age) 
#         self.faculty = faculty 
#     def display_student(self): 
#         info = super().display() 
#         info += f', faculty:{self.faculty}' 
#         return info 
# obj_student = Student('Amina', 22, 'science') 



# class Python27:
#     def __init__(self,name,last_name,age,gender):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#         self.gender = gender
#     def get_info(self):
#          print(f'{self.name} {self.last_name},{self.age},{self.gender}')
#     def get_info(self):
#         Python27.get_info(self)
#         print(f'stydent{self.name} {self.last_name} she is {self.age} {self.gender}')
# peremennaya = 'girl'
# if Python27 == 'girl':
#         print('girl')
# else:
# #      print('boy')
# Python27 = (1,5)
# num1 = float(input('Введите id студента: '))
# if num1 == Python27:
#      print('Она учиться в python27')
# else:
#      print('Такого студента в группе нет')



#Task 6
# class ContactList(list): 
#     def __init__(self, list_): 
#         self.list_ = list_ 
#     def search_by_name(self, name): 
#         a = [] 
#         for i in self.list_: 
#             if name in i: a.append(i) 
#             return a 
#         all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
#         print(all_contacts.search_by_name('Olya'))


#Task 7
# import datetime 
# class SmartPhones: 
#     def __init__(self, name, color, memory): 
#         self.name = name 
#         self.color = color 
#         self.memory = memory 
#         self.battery = 0 
#     def __str__(self): 
#         return f"{self.name} {self.memory}" 
#     def charge(self, number): self.battery += number 
# class Iphone(SmartPhones): 
#     def __init__(self, name, color, memory, ios): 
#         super().__init__(name, color, memory) 
#         self.ios = ios 
#     def send_imessage(self, string): 
#         return f"sending {string} from {self.name} {self.memory}" 
# class Samsung(SmartPhones): 
#     def __init__(self, name, color, memory, android): 
#         super().__init__(name, color, memory) 
#         self.android = android 
#     def show_time(self): 
#             return datetime.datetime.now().time() 
# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7) 
# print(iphone7.send_imessage('hello')) 
# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())





#разбор тасков
# cоздайте класс languages в этом классе должен быть атрибут класса который обозначает количество студентов,изучающие
#какой-либо язык программирование. От класса Languages создайте два дочерних класса:
#python, javascript В них также должны быть атрибуты указывающие на количество студентов,
#изучающие тот или иной язык. При создании обьекта-студента от одного из дочерних
#классов автоматически количество студентов в классах меняется если студент изучает язык python то количество студентов
#должно увеличится на один и в классе python  и в классе languages
#Анологично со студентами javascript. Далее в дочерних классах должен быть переопределен метод coding, в классах python
# он должен выдовать вам строку 'I am Python student. I am coding now', а в классе javascript
# 'I am JavaScript student. I am coding now' Создайте двух студентов от двух дочерних классов. Далее программа сама
#рандомно будет выбирать студентов и предлогает вам угадать какого студента она выбрала. После вашего выбара он вызывает
# метод coding у загаданного студента и выдает вам результат если вы отгадали правильно,пишет "Good job" если нет 
# "No bueno :("

# import random

# class Languages:
#     students_count = 0
#     def  __init__(self):
#      Languages.students_count += 1

#     def coding(self):
#        raise NotImplementedError

# class Python(Languages):
#     students_count = 0
#     def __init__(self):
#        super().__init__()
#        Python.students_count += 1

#     def __str__(self) -> str:
#        return 'Python'

#     def coding(self):
#        print("I am Python student.  I am coding now")

# class JavaScript(Languages):
#     students_count = 0
#     def __init__(self):
#        super().__init__()
#        JavaScript.students_count += 1

#     def __str__(self):
#        return 'JavaScript'

#     def coding(self):
#        print("I am JavaScript student. I am coding now")

# student1 = Python()
# student2 = JavaScript()

# my_choice = input("Guess the student's language\n")
# programm_choice = random.choice([student1, student2])

# programm_choice.coding()

# if programm_choice.__str__ () == my_choice:
#    print("Good job!!!")
# else:
#    print("No bueno :( ")




# import random

# class Person:
#     people_count = 0
#     def __init__(self):
#         Person.people_count += 1

#     def coding(self):
#         raise NameError
    
# class Boy(Person):
#     people_count = 0
#     def __init__(self):
#         super().__init__()
#         Boy.people_count += 1
#     def __str__(self) -> str:
#          return 'Boy'
#     def coding(self):
#         print("I am Boy")


# class Girl(Person):
#     people_count = 0
#     def __init__(self):
#         super().__init__()
#         Girl.people_count += 1
#     def __str__(self) -> str:
#         return 'Girl'
#     def coding(self):
#         print("I am girl")

# people1 = Girl()
# people2 = Boy()

# my_choice = input("Guess the people gender\n")
# programm_choice = random.choice([people1, people2])

# programm_choice.coding

# if programm_choice.__str__() == my_choice:
#     print("Good job!")
# else:
#     print("fuck you")
        

#Task 2
#Создайте свой класс My_list который наследует от list переопредилите метод списка insert() который
# обычно принимает первым аргументом индекс а вторым элемент в своем классе My_list переопредилите этот метод так чтобы
#он принимал аргументы в обратном порядке первым элемент вторым индекс

# class My_list(list):
#     def insert(self, arg1, arg2):
#         print("First arg - element, second arg - index")
#         return super().insert(arg2, arg1)
    
# list1 = My_list([1, 2, 3, 4, 5])
# list1.insert('Amina', 0)

# print(list1)
#['Amina', 1, 2, 3, 4, 5]


















# student3 = Python()
# student2.coding()
# student1.coding()
# print(Python.students_count)
# print(JavaScript.students_count)
# print(Languages.students_count)

