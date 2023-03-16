# dunder(double underscore) - это методы у которых 2 __ в начале и в конце
# почему магическими? потому что их можно не вызывать на прямую

class A:
    def __new__(cls):
        print("__NEW__")
        return super().__new__(cls)
    
    def __init__(self):
        print("__INIT__")
        

A()
#__NEW__
#__INIT__


# cls - class

#__new__, __init__ - вызывается при создании обьекта

print(dir(object))      #['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
#'__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
#'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

# __eq__ ==
# __ge__ >=
# __gt__ >
# __le__ <=
# __lt__ <
# __ne__ !=
# __add__ +
# __sub__ -
# __floordiv__ /
# __truediv__ //

