# "============Строки============="
# # строки- неизменяемые тип данных, предназначенные  для хранение текста (последовательные символов)

# string1 = 'строка в одинарных кавычках'
# string2 = "строка в двойных кавычках"
# string3 = "don't"
# string4 = 'Study in "Makers Incubator"'
# string5 = ''' Многострочный текст ''' тут можно использовать любые кавычки ''  ''
# string6 = "'"""'  Многострочный текст тут использовать любые кавычки
# string7 = 'hello' + ' ' +  'world' # 'hello world'
# string8 = 'hello' * 3 # 'hellohellohello'
# string9 = 'hello'  + str(1)

# '==============================Экранизация строк================'
# print('hello/nworld') /n 
# /n # это перенос на новую строку 
# /t # отступ (табуляция-таб)
# print ('/n - это перенос на новую строку')
# '\\' #отображение \
# '\''#отображение '
# "\"" #отображение ""
# '\r' #перенос коретки на начало строки
# '\v' # перенос на новую строку со смещением вправо на длину предыдущей строки


# 'hello\nworld'
# #hello
# #world

# 'hello\tworld'
# # hello    world

# 'экранизация \\'
# #экранизация \

# '123456789\rhello'
# # hello6789

# 'hello\vworld\vmakers'
# #hello
# #      world
# #            makers 

# '===============================Индексы============================='
# # индекс - это порядковый номер символа в строке (начиная с 0)
# # пример 'hello'
#         # 01234


# string = 'hello world'
# print (string[5])
# string = 'hello world'
# string = [0] #'h'
# string [-1] # 'd'
# string [5] # ''

# # срез - часть строки
# string [6:9] # 'wor'
# string [0:5] # 'hello'
# string [0:6] # 'hello '
# string [:6] # 'hello '
# string [7:] # 'orld'
# string [:] # 'hello world'
# string [0:11:2] #'hlowrd'
# string [::2] 'hlowrd'
# string [::-2]
# string[::-1] #перевернут от конца до начало


# '=========================Форматирование строк=========================='
# title = 'Пирог'
# price = 35
# string = f'Название: {title}, цена: {price}'
# # Название: Пирог, цена: 35

# format1 = 'Название: %s, цена: %s'
# print(format1 % ('Яблоко', 80))
# # Название: Яблоко, цена: 80

# format2 = 'Название: {}, цена: {}'
# print(format2.format('Груша', 60))
# # Название: Груша, цена: 60

# "==============================Методы строк===================="
#  # метод- функция, это функция которая принадлежит определенному типу данных, обращаемся к ней через точку

# (dir(str))  #посмотреть все доступные для данного типа данных

# 'hello'.upper() # 'HELLO'
# 'HELLO'.lower() #'hello'

# 'hello WORLD' .swapcase() #'HELLO world'
# 'Hello' .swapcase()  #'hELLO'
# 'hello world' .title() #'Hello World'
# 'hello world' .capitalize() #'Hello world'

# 'hello' .center(11) #'  hello  ' 
# 'hello' .center(11'-') #'---hello---'

# 'hello' .count('l') #2
# 'hello' .count('ll') #1
# 'Hello' .count ('hello') #0
# 'hello' .count ('') #6

# 'hello world'.split(' ') # ['hello', 'world']
# 'hello world'.split('o') #['hell', ' w', 'rld']

# ' ' .join(['hello', 'world']) # 'hello world'
# '%' .join (['hello', 'world']) # 'hello%world'

# 'hello world' .find('w') # 6
# 'hello world' .find('wor') #6
# 'hello world' .find ('o') #4
# 'hello world' .rfind (o) #7














 

