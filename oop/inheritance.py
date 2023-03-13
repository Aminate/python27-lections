# class A:
#     def method(self):
#         print("метод в классе А")

# obj_a = A()
# obj_a.method()
# #метод в классе А

# class B(A):
#     pass

# obj_b = B()
# obj_b.method()
# #метод в классе А


# obj_b = B()
# obj_b.method()
# #метод в классе А



# class C(A):
#     def method(self):
#         print("метод в классе С")

# obj_c = C()
# obj_c.method()
#метод в классе С


# class A:
#     def method(self):
#         print("метод в классе А")
#         return "aaa"
    
# class B(A):
#     def method(self):
#         print("метод в классе Б")
#         return_from_super=super().method()
#         print("super().method() вернул", return_from_super)
#         return "BBB"
    
# obj_a =A()
# res_a = obj_a.method()
# print("A.method вернул" , res_a)
    
# #     метод в классе А
# # A.method вернул aaa

# obj_b = B()
# res_b = obj_b.method()
# print("B.method вернул", res_b)

# class Range:
#     def create(self, num):       #create - принимает число
#         """Принимает число и возвращает список чисел от 0 до данного
#         числа включительно"""
#         return list(range(num+1))
    
# class Range10(Range):
#     def create(self):
#         """этот метод возвращает список чисел от 0 до 10 включительно"""
#         return super().create(10) #позволяет обращатся к родителю
   
    
# range_obj = Range()
# res = range_obj.create(5)
# print(res)
# # #[0, 1, 2, 3, 4, 5]


# range10_obj = Range10()
# res = range10_obj.create()
# print(res)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class A:
    alone1 ='a'
    def method(self):
        print("Метод в классе A")

class B:
    alone2 = 'b'

    def method(self):
        print("Метод в классе B")

class C(A,B):
    pass

obj_c = C()

print(obj_c.alone1) #a
print(obj_c.alone2) #b
obj_c.method()
#Метод в классе A потому что она стоит первым

#метод для (MRO) порядок поиска методов (method resolution or der) 


print(C.mro())
#[<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>]

#перекрестное наследование

class A:
    pass
class B:
    pass
class C(A,B):
    pass
class D(B,A):
    pass
class  E(C,D):
    pass
#TypeError: Cannot create a consistent method resolution
#order (MRO) for bases A, B