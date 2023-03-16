# Инкапсуляция - принцип ООП
> у которого есть 2 трактовки:
1. все что нужно для работы класса - лежит в классе
2. ограничение доступа к аттрибутом(сокрытие данных)

# в питоне есть 3 доступа ввида:
1. public (публичный)
2. proteccted(защищенный) - когда один underscore в начале
3. private (приватный)   - когда два underscore а начале


> В Python инкапсуляция реализованна на уровне соглашение



# Getters / Setters
> методы с помощью которых мы указываем каким образом мы можем получать и изменять какие-то аттрибуты


# Property
> декаратор  - который превращает метод в аттрибут с декаратороми getter, setter, deleter
> setter - будет работать - вызываться когда мы будем записывать в аттрибут значение
> deleter - будет работать - вызываться когда мы удаляем аттрибут через del


``` py
class A:
    @property
    def hello(self):
        return 5

    # property.setter работает когда мы пишем obj.attr = ... 
    @hello.setter
    def hello(self, new_value):
        print("setter")

    # property.deleter работает когда мы пишем del obj.attr
    @hello.deleter
    def hello(self):
        print("deleter")

obj = A()
print(obj.hello) #5
obj.hello = 'new value' #setter
del obj.hello #deleter
```
