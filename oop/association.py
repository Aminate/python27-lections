#============================Ассоциация======================================"
#Ассоциация - принцип ООП, в котором два класса друг с другом связаны
# ассоциация делится на 2 принципа
# 1 - агрегация (более слабая связь)
# 2 - композиция (более сильная связь)

class Battery:
    power = 100

    def charge(self):
        if self.power <100:
            self.power = 100

class Iphone:
    def __init__(self,color):
        self.color = color
        self.battery = Battery()
# когда мы создаем обьект от другого класса прям внутри другого - композиция

iphone = Iphone('gold')
del iphone
# обьект батарейки удаляется вместе  с обьектом iphone

class Nokia:
    def __init__(self, color, battery) -> None:
        self.color = color
        self.battery = battery
# когда мы принимаем уже созданный вне класса обьект - это агрегация

battery = Battery()
nokia = Nokia('black',battery)
#print(nokia.battery.power)  #100
del nokia
# удаляется только обьект nokia

(battery.power)
# если даже мы наследовались от класса battery и удалили класс nokia, у нас остается battery









# iphone = Iphone('gold')
# iphone.battery.power=50
# # print(iphone.battery.power)

# del iphone
# print(iphone) 

#агрегация это более слабая связь
