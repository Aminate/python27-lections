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



