#~~~~~~~~~~~~~~~~~~~~~~~~             EXCEPTIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Исключение  (ощибки) - это обьекты которые обрывают работу кода если не были обработаны

#SyntaxError
#исключение которое выходит если допущена синтаксическая ошибка
# ""''
# (
     #SyntaxError: '(' was never closed
#     ''''''

#TypeError 
#исключение которое выходит когда мы делаем чтото не свойственное
#данному типу данных

#например когда пытаемся добавит число со строкой
# 1 + '1'
#TypeError


# еще когда мы даем функцую больше или меньше аргументов чем она требует
#например
# list1 = []
# list1.pop(1,2,3,4)
# print(list1)        #TypeError: pop expected at most 1 argument, got 4


#или нечего не передаем
# list1 = []
# list1.append()
# print(list1) #TypeError: list.append() takes exactly one argument (0 given)

#KeyError
#когда мы обращаемся по несуществуещему ключу или пытаемся удалить несуществуеший ключ

# dict_ = {'a':1, 'b':2}
# dict_['c']
# print(dict_) #KeyError: 'c'



#NameError
#ощибка если нет такой переменнной
# print(ngjnfgb) #NameError: name 'ngjnfgb' is not defined

# a = 5
# if a == 6:
#     b = 7  #переменная создастся только если первое условия верное
#     print(b) #NameError: name 'ngjnfgb' is not defined



#ValueError 
#выходит такая ощибка когда мы передаем функцию то что оно не может корекктно отработать
# int('10a')
# print(int) #ValueError: invalid literal for int() with base 10: '10a'

#еще когда мы пытаемся распоковать не достаточное (не такое количество элементов) в несколько переменных
# a,b = 1,2,3
# a,b,c = 1,2
# a,b = 1,2,3,4
# print(a,b,c) #ValueError: too many values to unpack (expected 2)

#AttributeError
#выходит когда мы пытаемся вызвать несуществуещему методу в каком то типе данных
# list1 = []
# list1.lower()
# print(list1) #AttributeError: 'list' object has no attribute 'lower'


#IndexError
#выходит когда пытаемся обратиться по несуществуещему индексу

# list1 = [1,2,3]
# list1[100]
# print(list1) #IndexError: list index out of range

#или пытаемся удалить обьект по не сущ индексу


#import django
 #ModuleNotFoundError:  когда пытаемся обратиться к несущес библиотеке

#10 / 0
#ZeroDivisionError: division by zero
#когда делим на ноль

#  v = 10
# IndentationError: unexpected indent
#когда оступ не требовался а мы не соблюдали отступы

"========================Обработка исключений========================"
# чтобы наш код не ломался, мы можем использовать конструкцию try-except и обраюотать исключение

#try:
    # код, который возможно вызовет ошибку
   # num = int(input("Введите число: "))
#except ValueError:
    # код, который отработает только если в блоке try вызвалась ошибка ValueError
  #  print("Вы ввели не число")


#так же и с другими ошибками

#но можем еще добавить else
#код который отрабатывает только  если в блоке try  не вызвалась
# print("Введенное число", num)

# finally: 
# это код который отрабатывается вообще в любом случае
#хоть вызвалась ошибка хоть не вызвалась
#     ("До свидания")

#минимальная конструкция состоит из try-except или try-finnaly
#МОЖНО ИСПОЛЬЗОВАТЬ НЕСКОЛЬКО except 
#например

# try:
#     num1 = int(input("Введите 1 число "))
#     num2 = int(input("Введите 2 число "))
#     print(num1 // num2)
# except ValueError:
#     print('Вы ввели не число')
# except ZeroDivisionError:
#     print("Нельзя делить на 0")

# try:
#     num1 = int(input("Введите 1 число "))
#     num2 = int(input("Введите 2 число "))
#     print(num1 // num2)
# except (ValueError, ZeroDivisionError):
#     print('Введены не корректные данные')

# можно отловить любые исключения используя просто except
# try:
#     raise NameError
# except:
#     print("Любая ошибка")

# # можно отловить любые ошибки отлавливая Exception
# try:
#     int('12d')
# except Exception as e:
#     print(type(e))

# try:
#     print(1+'1') # TypeError
# except TypeError:
#     try:
#         print(int('10a')) # ValueError
#         print("первый except")
#     except ValueError:
#         print("вложенный except")
# except ValueError:
#     print("второй except")
# finally:
#     print("все")

# raise - вызвать ощибку
# raise exception("Ощибка")




#~~~~~~~~~~~~~~~~~~~ РАЗБОР С ЛЕКЦИИ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# try - значит попытаться
# except - значит исключение
# finally - наконец
# else - иначе


# task 1
# try: 
#     pass 
# except Exception: 
#     pass 
# else: 
#     pass 
# finally: 
#     pass


# task 2
# b = 10
# c = 11

# try:
#     print(a)
# except NameError:
#     print("Такой переменной не существует!")

# task 3
# num1 = input("Введите первое число: ")
# num2 = input("Введите второе число: ")

# try:
#     result = float(num1) / float(num2)
#     print(f"Результат деления {num1} на {num2} равен {result}")
# except ZeroDivisionError:
#     print("На ноль делить нельзя")


# task 5
# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# try: 
#   print(dict_['key1']) 
# except KeyError: 
#   print('Нет такого ключа!')

# task 6
# list_ = [1, 4, 9, 16, 25, 36] 
# try:
#       print(list_[3]) 
# except: 
#       print('Нет такого элемента!')


# Task 7
# try: 
#   age = int(input()) 
#   if age < 18: 
#         raise 
#   ValueError('Доступ запрещён') 
# except: 
#       print('Введён некорректный возраст') 
# else: 
#       print('Спасибо') 
# finally:
#       print('До свидания!')


# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ] 

# def func21(a:list,b:str)->list: 
#   result=list() 
#   for i in a: 
#     if b.lower() == i['category'].lower(): 
#       result.append(i) 
#       return result

# num = 3 
# def mul(): global num 
# num = num**2 
# mul() 
# mul() 
# mul() 
# print(num)

# num = 3 
# def mul(): 
#   global num 
#   num = num**2 
#   return num 
# mul() 
# mul() 
# mul() 
# print(num)




# balance = 0 
# def get_salary(amount): 
#   global balance 
#   balance = balance + amount 
# def pay_bills(amount, long_name): 
#     global balance 
#     balance = balance - amount 
#     print(f'Вы заплатили {amount} сом за {long_name}') 
#     return balance 
# def get_balance(): 
#     global balance 
#     print(f'У вас на счету {balance} сом') 
# get_salary(1000) 
# get_balance() 
# pay_bills(400, 'кабельное тв') 
# get_balance()


# result = 0 
# def pow_first(x,y): 
#   global result 
#   result = x ** y 
# def pow_second(z): 
#   global result 
#   result = result % z 
# pow_first(2, 3) 
# pow_second(3) 
# print(result)

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16} 
# for k, v in a.items(): 
#   if v >= 17: 
#     print(f'{k}, Вы можете войти в клуб') 
#   else: 
#     print(f'{k}, извините, Вы не проходите по age-control')


# a = ['pipi', 'papa', 'mama'] 
# b = [] 
# for i in a: b.append(i.capitalize()) 
# print(b)


# def count_symbols(word): 
#   glasnye = 0 
#   soglasnye = 0 
#   drugie = 0 
#   for letter in word: 
#     if letter.lower() in 'аяуюоеёэиы': glasnye += 1 
#     elif letter.lower() in 'бвгджзйклмнпрстфхцчшщ': soglasnye += 1 
#     else: drugie += 1 
#     return (f'Количество гласных: {glasnye}, согласных: {soglasnye}, остальных символов: {drugie}') 
# print(count_symbols('Мурат супер!'))

# a = [i for i in range(101)]
# print(a)


# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3] 
# def lower_7(): 
#   lower_7 = [i for i in a if i < 7] 
#   return lower_7 
# print(lower_7())

# list_ = ['123hello@gmail.com', '123', 'hello'] 
# result = list(map(lambda x: x if '@gmail.com' in x else 'Not valid email', list_)) 
# print(result)

list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56] 
list1=list(filter(lambda x:x>0,list_)) 
list2=list(filter(lambda x:not x>0,list_)) 
res=list(zip(list1,list2)) 
print(res)

