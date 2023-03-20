class A:
    def instance_method(self):
        print("метод обьекта") #метод обьекта
        print("self",self)  #self <__main__.A object at 0x102a34bd0>

obj = A() #создание обьекта класса
obj.instance_method()
#когда мы вызываем метод у обьекта, то нам не нужно передовать его в self,
# он передается автоматически

A.instance_method(obj)
# метод обьекта
# self <__main__.A object at 0x104f48dd0>
#Когда мы вызываем метод у класса, то нам нужно передавать обьект

A.instance_method(7) #self 7 не совсем правельный вызов 


class Amina:
    @classmethod  #задекарировали
    def class_method(cls):
        print("метод класса")
        print("cls", cls)


Amina.class_method()  #метод класса
#cls <class '__main__.Amina'>


obj = Amina()
obj.class_method()
# метод класса
# cls <class '__main__.Amina'>
#все равно от куда мы будем вызывать classmethod (от обьекта или класса)
# первым аргументом будет приходить класс

# примеры:
class C:
    counter = 0
    def __init__(self):
        #обьект создается
        # Counterr.counter += 1
        self._inc_counter()

    def __del__(self):
        #обьект удаляется
        # Counterr.counter -= 1
        self._dec_counter()

    @classmethod
    def _inc_counter(cls):
        #cls = class C
        #увеличиваем атрибут класса counter на один
        cls.counter += 1

    @classmethod
    def _dec_counter(cls):
        cls.counter -= 1
        # уменьшаем на один

obj1 = C()
obj2 = C()
obj3 = C()
obj4 = C()
print(C.counter) #4
del obj4
print(C.counter) #3
#через запитую можно удалить несколько обьектов (obj1, obj2)

class Pizza:
    def __init__(self, radius, *ingridients):   # * - много можем 
        self.r = radius
        self.ingridients = ingridients

    def cook(self):
        print(f"Пицца размером {self.r * 2}")
        print(f"Ингридиенты: {self.ingridients}")

@classmethod
def four_cheeze(cls, radius):
    pizza = cls(radius, "1 cheeze", "2 cheeze", "3 cheeze", "4 cheeze")
    return pizza

    

pizza1 = Pizza(15, "Сыр", "Колбаса", "Помидоры")
pizza1.cook()
# Пицца размером 30
# Ингридиенты: ('Сыр', 'Колбаса', 'Помидоры')

pizza2 = Pizza(10, "1 cheeze", "2 cheeze", "3 cheeze", "4 cheeze")
pizza2.cook()
# Пицца размером 20
# Ингридиенты: ('1 cheeze', '2 cheeze', '3 cheeze', '4 cheeze')
# метод который создает несколько - но 
pizza4 = Pizza.four_cheeze(10)
pizza4.cook()

pizza5 = Pizza.four_cheeze(15)
pizza5.cook()
    


    #Nastya:
class A:
    def instance_method(self):
        print("метод обьекта")
        print("self", self)

obj = A()
obj.instance_method()
# метод обьекта
# self <__main__.A object at 0x10054ccd0>
# когда мы вызываем метод у обьекта, то нам не нужно передавать его в self, он передается автоматически

A.instance_method(obj)
# метод обьекта
# self <__main__.A object at 0x10054ccd0>
# когда мы вызываем метод у класса, то нам нужно передавать обьект



class A:
    @classmethod
    def class_method(cls):
        print("метод класса")
        print("cls", cls)

A.class_method()
# метод класса
# cls <class '__main__.A'>

obj = A()
obj.class_method()
# метод класса
# cls <class '__main__.A'>

# все равно от куда вы будете вызывать classmethod (от обьекта или класса), первым аргументом будет приходить class



# примеры
class C:
    counter = 0

    def __init__(self):
        # обьект создается
        # C.counter += 1
        self._inc_counter()

    def __del__(self):
        # обьект удаляется
        # C.counter -= 1
        self._dec_counter()

    @classmethod
    def _inc_counter(cls):
        # cls - class C
        # увеличиваем аттрибут класса counter на один
        cls.counter += 1
    
    @classmethod
    def _dec_counter(cls):
        cls.counter -= 1


obj1 = C()
obj2 = C()
obj3 = C()
obj4 = C()
print(C.counter) # 4
del obj1
print(C.counter) # 3



class Pizza:
    def __init__(self, radius, *ingredients):
        self.r = radius
        self.ingredients = ingredients

    def cook(self):
        print(f"Пицца размером {self.r * 2}")    
        print(f"Ингридиенты: {self.ingredients}")
    
    @classmethod
    def four_cheeze(cls, radius):
        pizza = cls(radius, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
        # pizza = Pizza(15, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
        return pizza

pizza1 = Pizza(15, "Сыр", "Колбаса", "Cherry")
pizza1.cook()

pizza2 = Pizza(10, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
pizza2.cook()

pizza3 = Pizza(15, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
pizza3.cook()

pizza4 = Pizza.four_cheeze(10)
pizza4.cook()

pizza5 = Pizza.four_cheeze(15)
pizza5.cook()




class A:
    @staticmethod
    def static_method():
        print("статик метод")

obj = A()
obj.static_method()


class Cylinder:
    def __init__(self, diameter, height):
        self.di = diameter
        self.h = height
        self.area = self.get_area(diameter, height)

    @staticmethod
    def get_area(di, h):
        from math import pi
        circle_area = pi * di**2 / 4
        side_area = pi * di * h
        return circle_area*2 + side_area

cylinder1 = Cylinder(4, 10)
print(cylinder1.area)

print(Cylinder.get_area(4, 10))
# мы не создали обьект, но получили нужные нам расчеты





def get_area_cylinder(di, h):
    from math import pi
    circle_area = pi * di**2 / 4
    side_area = pi * di * h
    return circle_area*2 + side_area

print(get_area_cylinder(4, 10))