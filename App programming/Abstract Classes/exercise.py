# from abc import ABC, abstractmethod

# class A(ABC):
    
#     @abstractmethod
#     def m1():
#         print('In class A, Method m1.')

#     def m2():
#         print('In class A, Method m2.')

# class B(A):

#     def m2():
#         print('In class B, Method m2.')

# b = B()
# b.m2()
# from abc import ABC, abstractmethod

# class A(ABC):

#     @classmethod
#     @abstractmethod
#     def m1(self):
#         print('In class A, Method m1.')

# class B(A):

#     @classmethod
#     def m1(self):
#         print('In class B, Method m1.')

# b = B()
# b.m1()
# B.m1()
# A.m1()
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def m1():
        print('In class A.')

a = A()
a.m1()