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



class Person:
    arms = 2
    legs = 2
    name = 'Amina'
    def __init__(self, name) -> None:
        # __init__ - dunder (дабл андерскор) метод, который будет добавлят в обьект self атрибуты 
        # которые отличаются у разных обьектов

        self.name = name

    def walk(self):
        print(self)
        print("я хожу")


person1 = Person('Amina')   #(name: Any) -> None
person2 = Person('Nurik')
print(person1.name, person2.name)






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

class A:
    var1 = 'переменная класса'

    def __init__(self):
        self.var2 = 'переменная обьекта'

# print(dir(A))  
#  #['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
#'__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
#  '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#  '__weakref__', 'var1']

obj = A()
print(dir(obj))
 #['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
# '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']

print(A.var1)  #переменная класса

print(obj.var1)  #переменная класса
print(obj.var2)   #переменная обьекта


#инкапсуляция - когда все лежит в одной коробке 