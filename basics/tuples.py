"=========================TUPLE Это Кортеж============================================="
#tuple - это неизменяемый тип данных,итерируемый,индексируемый, и упорядоченный тип данных
#предназначенный для хранения элементов в строгом порядке.(в целом нечем не отличается от списков просто
# неизменяемый поэтому занимает меньше памяти)

# tuple1 = (1,2,3,4)

# tuple2 = (5)
# print(type(tuple2))
# #int
# tuple3 = 1,2,3,4 #tuple
# tuple5 = (1,'hello', [2,3,4])
# tuple5 
# tuple5 = (1,'hello', [2,3,4,5])
# print (tuple5)




#~~~~~~~~~~~~~~~~~~~~~~~~~~МЕТОДЫ TUPLE~~~~~~~~~~~~~~~~~~~~~~~~~


# count - считает кол-во данного элемента в tuple
# tuple1 = (1,2,1,4,1,5,1,6)
# print(tuple1.count(1)) # 4
# print(tuple1.count('hello')) # 0

# # index - возвращает индекс данного элемента в tuple
# tuple1 = ('hello', 'world', 105)
# print(tuple1.index('hello')) # 0
# print(tuple1.index('w')) # ValueError: tuple.index(x): x not in tuple

def x(values):
    values[0] = 1
    v = [2,3,4]
    x(v)
    print(v)