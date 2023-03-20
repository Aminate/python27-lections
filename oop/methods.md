# class/static/instance methods
> instance method - это метод, который первым аргументом принимает обьект класса
(instance,self). Используется они для работы с обьектами и его аттрибутами


```
class A:
    def instance_method(self):
        print("метод обьекта") #метод обьекта
        print("self",self)  #self <__main__.A object at 0x102a34bd0>

obj = A() #создание обьекта класса
obj.instance_method()

```

> class methods - это метод, который первым аргументом принимает класс
(instance,self). Используется они для работы с классом и его аттрибутами
```
class Amina:
    @classmethod 
    def class_method(cls):
        print("метод класса")
        print("cls", cls)


Amina.class_method()  
#cls <class '__main__.Amina'>


obj = Amina()
obj.class_method()
```


для создания class метода, нужно использовать декоратор classmethod
static method - методы, которые не взаимодействуют с обьектом и классом, но находятся внутри класса (по принципу инкапсуляции (все, что нужно для работы класса лежит внутри класса))

