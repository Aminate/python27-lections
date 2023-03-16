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


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else:
            raise Exception("Invalid age")
    
    @age.deleter
    def age(self):
        if self.__age < 100:
            raise Exception("Cannot delete age")
        del self.__age

obj = Person('Amina', 22)
print(obj.age)
obj.age = 34  #вдруг мы захотели поменять возраст
print(obj.age) #22,34
#del obj.age #Exception: Cannot delete age
#пока данные коректны все будет работать, короче хочешь возраст больше 120 то просто перезапиши твою ж мать!

# вот так:
obj.age = 115
del obj.age


