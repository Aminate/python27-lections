#              "Миксины - это классы которые будут использоваться для наследование"
# но от миксинов не создаются обьекты
# 2 Миксины - классы примеси, которые служат для расширение функционала класса

#mixins - от слова микс


# От миксинов нельзя создовать обьекты, поскольку миксины - несамостоятельный классы
#При наследовании миксины должны идти в первую очередь
#(все поля внутри класса атрибутты класса)


# class WalkMixin:
#     def walk(self):
#         print('я могу ходить')

# class SwimMixin:
#     def swim(self):
#         print('я могу плыть')

# class FlyMixin:
#     def fly(self):
#         print('я могу летать')

# class Human(WalkMixin):
#     name = 'человек'

#     def talk(self):
#         print('я могу говорить')


# class Fish(SwimMixin):
#     name = 'рыба'

# class Exocoetidae(SwimMixin, FlyMixin):
#     name = 'летучая рыба'


# class Duck(WalkMixin, SwimMixin, FlyMixin):
#     name = 'утка'

# object = [Human(), Fish(), Exocoetidae(), Duck()]   #создали список и закинули туда все классы

# for obj in object:     #проходимся по циклу
#     # print(obj.name)
# # человек
# # рыба
# # летучая рыба
# # утка

#     attrs = ['fly', 'swim', 'walk', 'talk']   #создали список сейчас будем доставать от туда достаем есть ли такой аттрибут
# # есть ли в классах какой либо обьект
#     for attr in attrs:
#         if hasattr(obj, attr):
#             method = getattr(obj, attr)
#             method()

# obj = Human()

# я могу ходить
# я могу говорить
# я могу плыть
# я могу летать
# я могу плыть
# я могу летать
# я могу плыть
# я могу ходить




# obj = Human()
# print(hasattr(obj, 'fly'))  #False
#hasattr - передаем первым аргументом обьект а вторым передаем есть ли атрибут или переменная в этом классе
#(ГРУБО ГОВОРЯ ОН ЗАХОДИТ И ИЩЕТ ЧТО МЫ ПРОПИШЕМ, ПРОВЕРЯЕТ)
# функция которая принимает обьект и название аттрибута. Возврашает True, если у обьекта есть такой аттрибут(метод)





# getattr() - вызываем как функцию, она тоже принимает в себя обьект и метод(название класса) и показывает
# ячейку памяти тоесть где он хранится.
#функция которая принимает обьект и название аттрибута, возвращает значение аттрибута
#например:

# obj = Human()

# print(getattr(obj, 'name'))  #человек
#она достает еще и содержимое

# method = getattr(obj, 'name')
# method()



# obj = Human()
# obj.talk()
# obj.walk()
# obj.swim()
# obj.fly()
# obj.walk()



# obj = Human()
# print(dir(obj))   #'name', 'talk', 'walk']



# obj = Human()
# setattr(obj, 'new_attribute', 'abracadabra')
# print(dir(obj)) #'new_attribute'
# print(obj.new_attribute) #abracadabra
 
 
 
 #setattr - позволяет нам создавать новые атрибуты со значением тоесть я создала новый атрибут с названием
 # new_attribute а значение сделала 'abracadabra'
# функция которая принимает обьект, название аттрибута и значение аттрибута, добавляет в обьект новый аттрибут или перезапишет
# одноименный аттрибут



# РАЗБОР С ЛЕКЦИИ

# mro - порядок решения методов
#пример:
# class Dad:
#     eye_color = 'green'

# class Mom:
#     eye_color = 'brown'

# class Child(Dad,Mom):   #это дочерний класс
#     pass

# child = Child()
# print(child.eye_color)  #green
# почему нам вывелся зеленый? Потому что он сначала зашол к себе в дочерний класс, там не нашел и пошел искать у отца
#так как мы указали в дочернем классе первым отца  class Child(Dad,Mom):


# Mixin - говоря человечиским языком например у моего отца есть талант хорошо петь, а мама хорошо рисует
# я унаследовала у них но у меня есть еще талант хорошо танцевать а этого таланта нет у моих родителей
#пример:
# class Dad:
#     def logic_skills(self):
#         print('Logic')

# class Mom:
#     def drawing_skills(self):
#         print('Draw')

# class ExtraTalantMixin:
#     def singing_skills(self):
#         print('Sing')

# class Child(Mom, Dad, ExtraTalantMixin):
#     pass

# child = Child()
# child.logic_skills()
# child.drawing_skills()
# child.singing_skills()
# #Logic
#Draw
#вот наследование а чтобы у нас был  свой талант то мы должны добавить в класс Child еще и свой талант  ExtraTalantMixin
#Logic
#Draw
#Sing


#ПОВТОР ООП

#наследование с расширением:

# class Parent:
#     def who_am_i(self):
#         print("I am parent")

# class Child(Parent):
#     def who_am_i(self):
#         super().who_am_i()
#         print("I am a child")

# child = Child()
# child.who_am_i()

# I am parent
# I am a child


#============== множественное наследование ==============================
#когда дочерний класс наследуется от нескольких родительских классов их может быть несколько

# class Father:
#     last_name = 'Ashimov'

# class Mother:
#     last_name = 'Zakirova'


# class Child(Father, Mother):
#     pass
#     # last_name = 'Ashimov'

# child = Child()
# print(child.last_name)
#Ashimov почему вышел? потому что мы в классе чайлд в ласт нейм сами прописали Ашимов

# а если мы удалим его и пропишем пасс, тогда все равно выйдет Ашимов так как первым родителям мы указали отца



# Task 1
# class Auto: 
#     def ride(self): 
#         print('Riding on a ground') 
# class Boat: 
#     def swim(self): 
#         print( 'Floating on water') 
# class Amphibian(Auto,Boat): 
#     pass 
# obj = Amphibian() 
# obj.ride() 
# obj.swim()

#Task 2
# class RadioMixin: 
#     def play_music(self): 
#         class_ = 'tittle' 
#         print(f'Песня называется {class_}') 
# class Auto: 
#     pass 
# class Boat(RadioMixin): 
#     pass 
# class Amphibian(Auto, Boat): 
#     pass 
# auto = Auto() 
# boat = Boat() 
# obj = Amphibian() 
# obj.play_music()

#Task 3
# class Clock:  (не закончен)
#     def current_time(self): 
#         print('17:10:41') 
# class Alarm: 
#     def on(self): 
#         print('08:00:00')
#     def off(self): 
#         print('09:00:00') 
# class AlarmClock(Clock, Alarm): 
#     def alarm_on(self): 
#         print('Будильник включён') 
# clock = AlarmClock() 
# clock.current_time() 
# clock.alarm_on()

# Task 4
# from abc import ABC, abstractmethod 
# class Coder(ABC): 
#     count_code_time = 0 
#     @abstractmethod 
#     def get_info(self): 
#         pass 
#     @abstractmethod 
#     def coding(self, hours): 
#         pass 
# class Backend(Coder): 
#     def __init__(self, experience, languages_backend): 
#         self.experience = experience 
#         self.languages_backend = languages_backend 
#     def get_info(self): 
#         return f"{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование" 
#     def coding(self, hours): 
#         self.count_code_time += hours 
# class Frontend(Coder): 
#     def __init__(self, experience, languages_frontend): 
#         self.experience = experience 
#         self.languages_frontend = languages_frontend 
#     def get_info(self): return f"{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование" 
#     def coding(self, hours): 
#         self.count_code_time += hours 
# class Fullstack(Backend, Frontend): 
#     pass 
# a = Backend('Junior', 'Python') 
# b = Frontend('Middle', 'JavaScript') 
# c = Fullstack('Senior', 'Python and JS') 
# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info())


#Task 5
# class Square: 
#     def __init__(self, side) -> None: 
#         self.side = side 
#     def get_area(self): 
#         return self.side * self.side 
# class Triangle: 
#     def __init__(self, height, base) -> None: 
#         self.height = height 
#         self.base = base 
#     def get_area(self): 
#         return int(0.5*self.base*self.height) 
# class Pyramid(Triangle, Square): 
#     def __init__(self, height, base) -> None: 
#         super().__init__(height, base) 
#     def get_volume(self): 
#         return int(1/3*self.base**2*self.height) 
# obj = Square(3) 
# print(obj.get_area()) 
# obj2 = Triangle(3,5) 
# print(obj2.get_area()) 
# obj3 = Pyramid(10,10) 
# print(obj3.get_volume())

#Task 6
# import datetime 
# class CreateMixin: 
#     def create(self, key, todo): 
#         if key in self.todos.keys(): 
#             return 'Задача под таким ключём уже существует' 
#         self.todos[key] = todo 
#         return self.todos 
# class DeleteMixin: 
#     def delete(self, key): 
#         delete_ = self.todos.pop(key, 'нет такого ключа') if 'нет такого ключа' == delete_: return delete_ 
#         return delete_ 
# class UpdateMixin: 
#     def update(self, key, new_value): 
#         self.todos[key] = new_value 
#         return self.todos 
# class ReadMixin: 
#     def read(self): 
#         res = [x for x in self.todos.items()] 
#         return sorted(res) 
# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin): 
#     todos = {} 
#     def set_deadline(self, deadline): 
# time_ = datetime.datetime.now().strftime('%d/%m/%Y') 
# deadline = deadline.split('/') 
# time_ = time_.split('/') 
# deadline = list(map(int, deadline)) 
# time_ = list(map(int, time_)) 
# time_ = sum((time_[0], time_[1]*30, time_[2]*365)) 
# deadline = datetime.date(deadline[2], deadline[1], deadline[0]) 
# time_ = datetime.date.today() 
#         return (deadline - time_).days 
# task = ToDo() 
# print(task.set_deadline('31/12/2022')) 
# print(task.create(1, 'todo')) 
# print(task.delete(3)) 
# print(task.update(1, 'todo')) 
# print(task.read()) 
# print(task.create(1, 'Do housework')) 
# print(task.create(1, 'Do housework')) 
# print(task.create(2, 'Go for a walk')) 
# print(task.update(1, 'Do homework')) 
# print(task.delete(2)) 
# print(task.read())
# print(task.set_deadline('31/12/2021'))

# Task 7
# class ExtensionMixin: 
#     def add_extension(self, extension): 
#         self.extensions.append(extension) 
#         return f'Добавлено новое расширение {extension} для игры {self.name}' 
#     def remove_extension(self, del_extension): 
#         if del_extension in self.extensions: 
#             self.extensions.remove(del_extension) 
#         return f'{del_extension} был отключен от {self.name}' 
# return 'Такого расширения нет в списке.' 
# class Game(ExtensionMixin): 
#     def __init__(self, type, name): 
#         self.type = type 
#         self.name = name 
#         self.extensions = [] 
#     def get_description(self, description): 
#         return f'{self.name} это {description}' 
#     def get_extensions(self): 
#         res = ' '.join(self.extensions) 
#         return res 
#     if res 
#     else:
#         'Нет подключенных расширений'


# Task 8
# class FlyMixin: 
#     def fly(self): 
#         print('я могу летать') 
# class WalkMixin: 
#     def walk(self): 
#         print('я могу ходить') 
# class SwimMixin: 
#     def swim(self): 
#         print('я могу плавать') 
# class Human(WalkMixin, SwimMixin): 
#     name = 'человек' 
#     def talk(self): 
#         print('я могу говорить') 
# class Fish(SwimMixin): 
#     name = 'рыба' 
# class Exocoetidae(SwimMixin, FlyMixin): 
#     name = 'летучая рыба' 
# class Duck(SwimMixin, WalkMixin, FlyMixin): 
#     name = 'утка'


 