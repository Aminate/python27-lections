# class Dog:
#     def speak(self):     #speak - это один интерфейс 
#         print("гав гав")


# class Cat:
#     def speak(self):
#         print("мяу-мяу")

# class Frog:
#     def speak(self):
#         print("ква ква")


# animals = [Cat(), Frog(), Dog(), Cat(), Frog(), Dog()]
# for animal in animals:
#     animal.speak()
# # мяу-мяу
# # ква ква
# # гав гав
# # мяу-мяу
# # ква ква
# # гав гав  
# print(animal) #<__main__.Dog object at 0x1027794d0>




list1 = [1,2,3,4,5]
dict1 = {"a": 1, "b": 2}

list1.pop(0)  #удаление по индексу
dict1.pop("a") #удаление по ключу

# например тут метод поп удаляет но в первом примере по индексу а во втором по ключу, один метод работает по разному



# 1 + 5
# "a" + "b"

# __add__
# складывает  и возвращает новый список

a = 4
b = 3
print(a+b)  #7
print(a.__add__(b))  #7

a = [1,2,3]
b = [4,5,6]
print(a.__add__(b))   #[1, 2, 3, 4, 5, 6]


#__len__

a = 'abc'
print(len(a))
print(a.__len__())

b = [1,2,3[4,5,6]]
print()