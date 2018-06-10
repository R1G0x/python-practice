# In Python, an Abstract Base Class can be created using module abc.

#Abstract base calss Shape is defined with two abstract methods area and perimeter.

#With existing abstract class definition of Shape, if you try creating a Shape object it
# results in TypeError
# s1 = Shape()
# Output 
# TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter
from abc import ABC, abstractmethod

class Shape(ABC):
  
  @abstractmethod
  def area(self):
    pass
  
  @abstractmethod
  def perimeter(self):
    pass

#Creating object c1, with out definingperimeter inside derived class, Circle, resulted in TypeError.
class Circle(Shape):
  def __init__(self, radius):
    self.__radius = radius
  
  @staticmethod
  def square(x):
    return x**2
    
  def area(self):
    return 3.14*self.square(self.__radius)

c1 = Circle(3.9)
  