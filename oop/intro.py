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


class Car:
#тут интересное то что я хочу чтобы при каждом добавлении к машине,был счечик который добавляет 1(количество обьектов)
    car_count = 0


    def __init__(self):
        Car.car_count += 1

car1 = Car()
print(Car.car_count)
 #1 тут у нас сработал счечик
car2 = Car()
print(Car.car_count) #2
#и так каждый раз добавляется новая машина

