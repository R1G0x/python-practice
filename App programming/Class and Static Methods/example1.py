class Circle(object):
  
  no_of_circles = 0
  
  def __init__(self, radius):
    self.__radius = radius
    Circle.no_of_circles += 1
    
  
  def getCirclesCount(self):
    return Circle.no_of_circles


c1 = Circle(3.5)
c2 = Circle(5.2)
c3 = Circle(4.8)

print(c1.getCirclesCount()) # -> 3
print(c2.getCirclesCount()) # -> 3
print(Circle.getCirclesCount(c3)) # -> 3
print(Circle.getCirclesCount()) # -> TypeError

# getCirclesCount method is bound to objects of Circle
# Hence when calling it,
  # - on objects c1, and c2 resulted in 3
  # - on class Circle with object c3 as argument resulted in 3 again
  # - on class circle without any object information resulted in TypeError