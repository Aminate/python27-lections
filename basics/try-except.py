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







