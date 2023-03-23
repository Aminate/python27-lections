#~~~~~~~~~~~~~~~~~~~~~~~СПИСКИ,LIST~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#список- это изменяемый тип данных,итерируемый,индексируемый, и упорядоченный тип данных
#предназначенный для хранения элементов в строгом порядке.

#list1 = [10, 2.5, 'hello', [], (1,2,3), (1,2) None, True, False]
#list1[0] #10
#list1[3] #[1,2,3]
#list[3][-1] # 3
#list1[-1] #False
#list1[2][-1] #'o'

#list2 = list('hello')
#print (list2) #['h','e','l','l','o']

#range = начало конец и шаг
#например:
#list3 = list(range(3,10,2))
#print(list3) #[3,5,7,9]
#print(list(range(5))) #[0,1,2,3,4]


#-----------------изменяемость-------------------
#string = 'hello'
#res = string.upper()
#print(string) #hello
#print(res)  #'HELLO'

#list1 = []
#list1.append (1)
#list1.append (2)
#list1.append(3)
#print(list1) #[1,2,3]

"~~~~~~~~~~~~МЕТОДЫ СПИСКОВ~~~~~~~~~~~~~~~~~~~~~~~~~~"
#append - метод который добавляет элемент в конец списка
#list1 = []
#list1.append('hello')
#list1.append(500)
#list1.append([1,2,3])
#print(list1) #['hello' 500,[1,2,3]]

#как можно удалять
#remove - метод который удаляет элемент из списка по значению но только первого вхождение этого элемента,
#выдаст ошибку ValueError, если такого элемента нет в списке
#list2 = [10,'hello',500, 'world', 1000, 'hello', 500]
#list2.remove('hello')
#print(list2) #[10,500,'world',1000,'hello',500]
#удаляет только первый 'hello' со списка

#pop - метод который удаляет елемент из списка по индексу если этого индекса нет выдаст IndexError
#list3 = [10, 20, 30, 40, 50]
#list3.pop() #удаление с конца
#print(list3) #[10,20,30,40]
#list3.pop(1) #удаляет по индексу 1
#print (list3) #[10,30,40]


#также метод pop возвращает удаленный элемент
#list4 = [10, 20, 30, 40, 50]
#popped = list4.pop(0)
#print(list4) #[20, 30, 40, 50]
#print(popped) #10

#list5 = []
#list5.pop()
#IndexError: pop from empty list
#тоесть пустоту если хотим удалить выдается ощибка

# insert - метод, который добавляет элемент в список по индексу
#list5 = [1,2,3,4]
#list5.insert(0, 'hello')
#print(list5) # ['hello', 1, 2, 3, 4]

# создайте список с числами от 1 до 10
# выведите список с числами в обратном порядке
#list1 = [1,2,3,4,5,6,7,8,9,10]
#list1 = list(range(1,11))
# print(list1[::-1])
# list1.reverse()
# print(list(reversed(list1)))
#str="1 2 3 4 5 6 7 8 9 10" 
#slicedString=str[::-1]
#print (slicedString)

# clear - чистит список
#list1 = [1,2,3,4]
#list1.clear()
#print(list1) # []

# count - считает кол-во элемента, который передаем в метод в списке
#list1 = [1,2,3,4,1,2,1,4,1,6]
#list1.count(1) # 4
#list1.count(3) # 1
#list1.count('hello') # 0

#пример с строками:
#users = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"] 
#users_count = users.count("Tom") 
#print(users_count)
#вывод:
# 3 

#list1 = ['hello', 'hello', 'hello']
#list1.count('hello') # 3
#list1.count('l') # 0

#list1 = [11, 12, 13]
#list1.count(1) # 0

# index - возвращает индекс данного элемента
#list2 = ['hello', 'world', 'makers']
#ind = list2.index('hello')
#print(ind) # 0
#list2.index('makers') # 2

# sort - метод, который сортирует по возрастанию (работает только со списками)
# если передать .sort(reverse=True), то сортирует по убыванию
#list3 = [34,12,67,12,89,45]
#list3.sort()
#print(list3) # [12, 12, 34, 45, 67, 89]
#list3.sort(reverse=True)
#print(list3) # [89, 67, 45, 34, 12, 12]
# list3.sort()
# list3.reverse()

#Сортировка в строках
#users = ["Tom", "Bob", "Alice", "Sam", "Bill"] 
#users.sort() 
#print(users)
# вывод:
# ["Alice", "Bill", "Bob", "Sam", "Tom"]


#Если необходимо отсортировать данные в обратном порядке, то мы можем после сортировки применить метод reverse():

#users = ["Tom", "Bob", "Alice", "Sam", "Bill"] 
#users.sort() 
#users.reverse() 
#print(users)
#вывод:
# ["Tom", "Sam", "Bob", "Bill", "Alice"] 





#list4 = ['a', 'c', 'b', 'B', 'A']
#list4.sort()
#print(list4) # ['A', 'B', 'a', 'b', 'c']

#list5 = [10, 'b', 3, 'c', 5]
# list5.sort() 
# TypeError: '<' not supported between instances of 'str' and 'int'

# copy - возвращает копию списка
#list1 = [1,2,3]
#list2 = list1.copy()
#list2.append(4)
#print(list1)
#print(list2)

# extend - расширяет список другим списком
#list1 = [1,2,3,4]
#list2 = [5,6,7,8]
# list1.append(list2)
# list1  [1,2,3,4, [5,6,7,8]]

#list1.extend(list2)
# list1  [1,2,3,4,5,6,7,8]

#~~~~~~~~~~~~~~~~~МИНИМАЛЬНОЕ И МАКСИМАЛЬНОЕ ЗНАЧЕНИЯ~~~~~~~~~~~~~~~~~~~~~
#Встроенный функции Python:
#  # min() и max() позволяют найти минимальное и максимальное значения соответственно:
#numbers = [9, 21, 12, 1, 3, 15, 18] 
#print(min(numbers))
#вывод: 1

#numbers = [9, 21, 12, 1, 3, 15, 18]
#print(max(numbers))
#вывод: 21 












#~~~~~~~~~~~~~~ПРАКТИКА С ЧИСЛАМИ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#пустые списки определение-создание например:
#numbers1 = []
#numbers2 = list()

#print (type(numbers1))
#print(type(numbers2))

#если хотим создать список в котором повторяется одно и то же значение несколько раз можно 
#использовать '*'

#numbers = [7, 7, 7, 7, 7, 7]
#numbers2 = [7] * 6
#print (numbers)
#print (numbers2)

#например:
#numbers = [5] * 6
#print(numbers)
# [5, 5, 5, 5, 5, 5]  

#последовательный
#range()
#функция range имеет 3 формы:
#1. range(end) (один аргумент)
# numbers = list (range(10))
#print (numbers)
#выдает [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] не влючая конец

#2. range(start,end) тут число strart включается а число end не включается (два аргумента)
#numbers = list(range(1,10))
#print(numbers)
#выдает [1, 2, 3, 4, 5, 6, 7, 8, 9] не включает 0 потому что мы выдали start как 1

#3. range (start, end, step) (тут уже три аргумента)
#numbers = list(range(1,10, 2))
#print(numbers)
#выдает [1, 3, 5, 7, 9]
#step в переводе как шаг, так вышло потому что мы выдали шаг как 2

#можно так же сделать отрицательным: тоесть в обратном порядке
#numbers = list(range(10,0 -1))
#print(numbers)
#выдает [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


#Так же с помощью range мы можем подставить список:
#Перебор с помощью цикла while
#Для перебора с помощью функции len() получаем длину списка.
#  С помощью счетчика i выводит по элементу, пока значение счетчика не станет равно длине списка.
#например:
#companies = ["Microsoft", "Google", "Oracle", "Apple"] 
#i = 0 
#while i < len(companies): 
 #   print(companies[i]) 
 #   i += 1
#вывод:
# Microsoft 
# Google 
# Oracle 
# Apple 

#~~~~~~~~~~~~~~~~~~~~~~~~~~Сравнение списков~~~~~~~~~~~~~~~~~~~~~~~~~~
#Два списка считаются равными, если они содержат один и тот же набор элементов:
#Таким оброзом мы можем сделать так:
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
#numbers2 = list(range(1,10)) 
#if numbers == numbers2: 
 #  print("numbers equal to numbers2") 
#else: 
#   print("numbers is not equal to numbers2")
#вывод:
# numbers equal to numbers2

#~~~~~~~~~~~~~~~~~~~~~ in ~~~~~~~~~~~~~~~
#с помощью ключевого слова in можно проверять его наличие, например перед его удалением:
#companies = ["Microsoft", "Google", "Oracle", "Apple"]
#item = "Oracle" # элемент для удаления  
#if item in companies: 
 #   companies.remove(item)


#print(companies)
#вывод:
# Microsoft 
# Google 
# Apple 






#Добавление и удаление элементов
#Для добавления элемента применяются методы append() и insert(), а для удаления - методы remove(), pop() и clear().







#`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FOR~~~~~~~~~~~~~~~~~~~~~~~~~`
#for синтаксис идет след оброзом:
# for потом i in range(1,11):
#выдает с 1 го до 10 ти 11 не влючительно
#если хотим возвести в квадрат то используем **







