class Circle(object):
    no_of_circles = 0

    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1


    @classmethod
    def getCirclesCount(self):
        return Circle.no_of_circles



c1 = Circle(3.5)
c2 = Circle(5.2)
c3 = Circle(4.8)

# getCirclesCount is decorated with classmethod
# Thus making it a class method, which bounds to class Circle.
# In Example 2, class Circle is passed as argument to getCirclesCount in both cases. i.e when it is called on objects and the class.