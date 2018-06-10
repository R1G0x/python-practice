# Corrected class definition of Circle, that contains perimeter definition too.
from abc import ABC, abstractmethod

class Shape(ABC):
  
  @abstractmethod
  def area(self):
    pass
  
  @abstractmethod
  def perimeter(self):
    pass
  
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius


    @staticmethod
    def square(x):
        return x**2

    def area(self):
        return 3.14*self.square(self.__radius)


    def perimeter(self):
        return 2*3.14*self.__radius



c1 = Circle(3.9)
print(c1.area())