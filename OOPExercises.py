# Define the class Point that represents x, y, and z coordinates of 3D coordinate system.
# Hint : Define the initializer method, __init__ that takes three values 
# and assigns them to attributes x, y and z respectively.
# Now create an object p1 = Point(4, 2, 9) and print it using the statementprint(p1). 
# You may type python3.5 to use the latest version for the exercise

class Point:
  
  def __init__(self, x=1, y=2,z=3):
    self.x = x
    self.y = y
    self.z = z
  

p1 = Point(4,2,9)
print(p1)

# Improvise the class definition of Point such that any Point object is displayed in the format point : (x, y, z).
# Hint : Define the method __str__ inside the class Point.
# Execute your code and observe the output of statement print(p1). You may type python3.5 to use the latest version for the exercise


# Determine distance between two point Objects.
# Hint : Define the method distance, which determines distance between two points. 
# Use formula distance = sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1 -z2)**2 ).
# Now create two Point objects p1 = Point(4, 5, 6) and p2 = Point(-2, -1, 4) and distance of p1 from p2 using defined distance method. 
# You may type python3.5 to use the latest version for the exercise


# Improvise Point class definition such that,
# adding any two Point objects using + operator, results in a new Point object with corresponding x, y and z values being added.
# For e.g: Point(1, 2, 3) + Point(2, 3, 4) -> Point(3, 5, 7)
# - Hint : Define `__add__` method inside the class `Point`.
# Try executing print(p1 + p2) and view the result. You may type python3.5 to use the latest version for the exercise


# Define the function isEven which returns True, if a given number is even and returns False, if the number is odd.
# Define a simple class TestIsEvenMethod derived from unittest.TestCase class.
# Hint : Import unittest module and use TestCase utility of it. You may type python3.5 to use the latest version for the exercise


# Define a test test_isEven1, inside TestIsEvenMethod, that checks if isEven(5) returns False or not.
# Hint : Use assertEqual method to verify the function output with expected output. 
# You may type python3.5 to use the latest version for the exercise


# Define another test test_isEven2, inside TestIsEvenMethod, that checks if isEven(10) returns True or not.
# Hint : Use assertEqual method to verify the function output with expected output
# You may type python3.5 to use the latest version for the exercise



# Define one more test test_isEven3, inside TestIsEvenMethod, that checks if isEven 
# function raises TypeError when a string hello is passed as argument.
# Hint : Use assertRaises
# Run the entire Test case and ensure that you pass all above three defined tests.
# Hint : Make use of unittest.main() for running the test case. 
# You may type python3.5 to use the latest version for the exercise