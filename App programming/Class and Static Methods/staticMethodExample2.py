# In Example 2, the square method is defined inside the class Circle and decorated with staticmethod.
# Then it is accessed as self.square.
# You can also observe that square method is no longer accessible from outside the class Circle.
# However, it is possible to access the static method using Class or the Object as shown below.
class Circle(object):

    def __init__(self, radius):
        self.__radius = radius


    @staticmethod
    def square(x):
        return x**2

  
    def area(self):
        return 3.14*self.square(self.__radius)



c1 = Circle(3.9)
print(c1.area())  
print(square(10)) # -> NameError