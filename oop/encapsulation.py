# class A:
#     attr1 = 'public'
#     _attr2 = 'protected'
#     __attr3 = 'private'

# print(A.attr1) #public
# print(A._attr2) #protected
# # print(A.__attr3) # AttributeError: type object 'A' has no attribute '__attr3'. Did you mean: '_A__attr3'?
# print(A._A__attr3) #private
#так как наш attr3 приватный питон придлажил нам переименовать и после этого нам вывелось содержимое

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age

#     def get_age(self):
#         return self.__age
#     def set_age(self, new_age):
#         if new_age > 0 and new_age < 120:
#             self.__age = new_age
#         else:
#             raise Exception('Invalid age')
    
# obj = Person('Amina',22)
# print(obj.name) #Amina
# print(obj.get_age()) #22
# obj.set_age(45)
# print(obj.get_age()) #22
#                      #45

# obj.set_age(125) #Exception: Invalid age
#мы можем вытащить приватные через перезапись

#  def _validate_phone_number(self, phone_number): 
#         if isinstance(phone_number, int) and str(phone_number).startswith('996'): 
#             return phone_number 
#         return None 
#     def __validate_card_number(self, card_number): 
#         if isinstance(card_number, int) and len(str(card_number)) == 16: 
#             return card_number 
#         return None 
# tolik = Person('Sam', 996557551757, 9999999999999999) 
# print(tolik.name) 
# print(tolik._phone_number) 
# print(tolik._Person__card_number)

# class A:
#     @property     #это проперти - декаратор который делает аттрибут
#     def abracadabra(self):
#         return 5
#     #proparty.setter - работает когда мы пишем какой то аттрибут(obj.attr = ...)
#     @abracadabra.setter
#     def abracadabra(self,new_value):
#         print("setter")
#         #property.deleter - работает когда мы пишем del obj.attr
#         @abracadabra.deleter
#         def abracadabra(self):
#             print("deleter")
# obj = A()
# print(obj.abracadabra)  #5
# obj.abracadabra = 'new value' # 'setter'
# del obj.abracadabra #deleter


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, new_age):
#         if new_age > 0 and new_age < 120:
#             self.__age = new_age
#         else:
#             raise Exception("Invalid age")
    
#     @age.deleter
#     def age(self):
#         if self.__age < 100:
#             raise Exception("Cannot delete age")
#         del self.__age

# obj = Person('Amina', 22)
# print(obj.age)
# obj.age = 34  #вдруг мы захотели поменять возраст
# print(obj.age) #22,34
#del obj.age #Exception: Cannot delete age
#пока данные коректны все будет работать, короче хочешь возраст больше 120 то просто перезапиши твою ж мать!

# вот так:
# obj.age = 115
# del obj.age



# РАЗБОР ТАСКОВ (лекции)
# task 1:
#"Создайте класс терминал, создайте обьект-карточку от этого класса передав номер своей карточки и пин-код. При этом,
# необходимо проверить валидность карточки номер карточки должен содержать строго блять 16 цифр, а пин код - 4 цифры 
#(для этого используйте инкапцуляцию) При создании карточки в ней содержится 0 сомов, далее должны быть след методы "

# class Terminal:
#     def _check_card(self, card):
#         if len(card) == 16 and card.isdigit():
#          self.__card = card
#         else:
#             print('Invalid card number')

#     def _check_pin(self,pin):
#        if len(pin) == 4 and pin.isdigit():
#           self.__pin = pin
#           self.money = 0
#        else:
#           print('Invalid pin code')


#     def __init__(self,card,pin):
#         self._check_card(card=card)
#         self._check_pin(pin=pin)

#     def _validation(self, pin):
#        if self.__pin == pin:
#           return True
#        else:
#           return False

#     def put(self,pin, money):
#        if self._validation(pin=pin):
#           self.money += money
#           print(f"There is {self.money} on your balance")
#        else:
#           print(f"Not correct pin code")

#     def __check_money(self,money):
#        if money % 10 == 0:
#           return True
#        else:
#           print("Invalid amount  of money")
#           return False
       
#     def _check_balance(self, money):
#        if self.money < money:
#           print("Not enough money on your balance")
#           return False
#        else:
#           return True
       
#     def get_money(self, pin, money):
#         if self._validation(pin=pin):
#             if self.__check_money(money=money) and self._check_balance(money=money):
#                 self.money -= money
#                 print(f"There is {self.money} on your balance")
#         else:
#             print('Not correct pin code')


# card = Terminal(card='9958552359029458', pin='1111')
# card.put(pin='1111', money=1000)
# card.get_money(pin='1111', money=92)
# print(card.money)
# print(card.card) #ощибка так как он приватный
# print(card.pin) #тоже самое
# print(card.money) #выдается так как моней у нас публичный


# Далее - метод put, который будет принимать в качестве аргументов: пин код карточки вторым аргументом - сумму денег
# которую хотите закинуть на эту карточку, прежде чем закинуть деньги необходимо проверить введенный пин код совпаденин
#(используя инкапсуляцию)
# Далее - метод get_money который также принимает первым аргументом пин код, вторым аргументом - сумму денег, которую
#хотите извлечь из карты, здесь такжн необходимо использовать валидацию: (проверка пин кода + сумма денег должна быть
# округленной до десятичных чисел, типа 10, 100, 200, 5000 и т д) (45, 899, 46,6 - невалидные данные)
# И только после проверки деньги извлекаются
# Примените данные методы к своей карточке несколько раз и в конце выдайте сколько денег на карточке. 
# Примечание: НЕЛЬЗЯ ИЗВЛЕЧЬ СУММУ ДЕНЕГ ЕСЛИ ОНА БОЛЬШЕ ЧЕМ СУММА ДЕНЕГ НА КАРТОЧКЕ! ТАКЖЕ НЕЛЬЗЯ ВЫТАЩИТЬ ПИН 
# КОД КАРТОЧКИ (эти данные должны быть скрыты)


# Task 1
# class A:
#     def public(self):
#         return 'Public method'
#     def _protected(self):
#         return 'Protected method'
#     def __private(self):
#         return 'Private method'
 
# obj1 = A() 
# print(obj1.public()) 
# print(obj1._protected()) 
# print(obj1._A__private())


# Task 2
# class A:
#     def method1(self):
#         return "Hello World"
    
# class B(A):
#     def  b1(self):
#        pass
# b1 = B() 
# print(b1.method1())
        

# Task 3

# class Car:
#     __speed=0 # приватный аттрибут 
#     def set_speed(self,new):
#         self.__speed = new
#         return self.__speed
#     def show_speed(self):
#         return self.__speed
    
# car1 =Car()
# print(car1.show_speed())
# car1.set_speed(20)
# print(car1.show_speed())

# Task 4

# class Car:
#     __speed=0 
#     @property 
#     def speed(self):
#         return self.__speed
#     @speed.setter 
#     def speed(self,new):
#         self.__speed=new 
#         return self.__speed
    
# car1 =Car()
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed)


# Task 5
# Создайте класс Person и объявите в нем 3 атрибута класса: name (public), phone_number(protected) и сard_number(private),
# Атрибуты класса будут равны следующим значениям: "John", "+996 557 55 17 57" и "9999 9999 9999 9999".
# Создайте объект 'john' класса Person и выведите на экран все атрибуты класса.

# class Person: 
#     name = "John" 
#     _phone_number = "+996 557 55 17 57" 
#     __card_number = "9999 9999 9999 9999" 
#     @property 
#     def number(self): 
#         return self.__card_number 
# john = Person() 
# print(john.name) 
# print(john._phone_number) 
# print(john.number)

#Task 6

# class Person:
#     def __init__(self, name, phone_number, card_number) -> None:
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number
    
#     @property
#     def number(self):
#         return self.__card_number

# john = Person("John", "+996 557 55 17 57", "9999 9999 9999 9999") 
# print(john.name) 
# print(john._phone_number) 
# print(john._Person__card_number)


# Task 7
# class Person:
#     name = "John"
#     _phone_number = "+996 557 55 17 57"
#     __card_number =  "9999 9999 9999 9999"
#     @property 
#     def number(self): 
#         return self.__card_number 

# john = Person()
# john.name = None
# john._phone_number = None
# john._Person__card_number = None
# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)

# Task 8
# class Person:
#     def __init__(self, name, phone_number, card_number) -> None:
#         self.name =self.__validate_name(name)
#         self._phone_number = phone_number
#         self.__card_number = card_number
    
#     @property
#     def number(self):
#         return self.__card_number
    
#     @property
#     def __validate_name(self):
#          if len(self.name) < 2:
#              return self.name
#          else:
#              return self.name[0].upper()+self.name[1:].lower()
# sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(sam._Person__validate_name)
# print(sam._phone_number) 
# print(sam.__card_number)
# print("Initial level:", game.get_level()) game.play(3) game.play(5) print("Final level:", game.get_level())


# class Person:
#     def __init__(self, name, phone_number, card_number): 
#         self.name = self.__validate_name(name) 
#         self._phone_number = phone_number 
#         self.__card_number = card_number 
#     def __validate_name(self, name):
#         if len(name) < 2: 
#             return "John" 
#         else: 
#             return name.title() 
#     def get_card_number(self): 
#         return self.__card_number 
#     def set_card_number(self, card_number): 
#         self.__card_number = card_number 

# sam = Person("SAM","+996 557 55 17 57","9999 9999 9999 9999")
# print(sam.name)
# print(sam._phone_number)
# print(sam._Person__card_number)


# Task 9
# class Person: 
#     def __init__(self, name, phone_number, card_number): 
#         self.name = name 
#         self._phone_number = self._validate_phone_number(phone_number) 
#         self.__card_number = self.__validate_card_number(card_number) 
#     def _validate_phone_number(self, phone_number): 
#         if isinstance(phone_number, int) and str(phone_number).startswith('996'): 
#             return phone_number 
#         return None 
#     def __validate_card_number(self, card_number): 
#         if isiard_number, int) and len(str(card_number)) == 16: 
#             return card_number 
#         return None 
# tolik = Person('Sam', 996557551757, 9999999999999999) 
# print(tolik.name) 
# print(tolik._phone_number) 
# print(tolik._Person__card_number)


# Task 10
# class Game:
#     __level = 0
#     def __init__(self,name):
#         self.name = name

#     def play(self,hours):
#         if hours > 2:
#             self.__level += 1

#     def get_level(self):
#         return self.__level 
# game = Game("Nursultan")
# print(game.get_level())
# game.play(4)
# game.play(3)
# print(game.get_level())


#Task 11
class Game:
 __level = 0 
def __init__(self, name): 
    self.name = self.__validate_name(name) 
    def set_level(self, level): 
        if self.name == 'Tolik': 
            self.__level = level 
        else: 
            print(f"{self.name} ты не Tolik!") 
    def __validate_name(self, name): 
        return name.title() 
game = Game('Raychel') 
game.set_level(5) 
print(game._Game__level) 
game2 = Game('TOLIK') 
game2.set_level(5) 
print(game2._Game__level)



