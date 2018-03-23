# In Example 1, square function is defined outside the class Circle.
# It determines square of a number, x.
# It can be used outside and also inside the class Circle.
# Though existing square function serves the purpose, it is not packaged properly and does not appear as integral part of class Circle.
def square(x):
  return x**2

class Circle(object):
  
  def __init__(self, radius):
    self.__radius = radius
    
  def area(self):
    return 3.14*square(self.__radius)
    

c1 = Circle(3.9)

print(c1.area())
print(square(10))

