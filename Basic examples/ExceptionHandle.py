try:

    a = pow(2, 4)

    print("Value of 'a' :", a)

    b = pow(2, 'hello')   # results in exception

    print("Value of 'b' :", b)

except TypeError as e:

    print('oops!!!',e)

print('Out of try ... except.')

#Raising Exceptions
#raise keyword is used when a programmer wants a specific exception to occur.
try:
    a = 2; b = 'hello'
    if not (isinstance(a, int)
            and isinstance(b, int)):
        raise TypeError('Two inputs must be integers.')
    c = a**b
except TypeError as e:
    print(e)

# User Defined Functions
# There are many built-in exceptions in Python, which are directly or indirectly derived from Exceptionclass.
# Python also allows a programmer to create custom exceptions, derived from base Exception class.
class CustomError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


#User defined function Example 1
try:
    a = 2; b = 'hello'
    if not (isinstance(a, int)
            and isinstance(b, int)):
        raise CustomError('Two inputs must be integers.')
    c = a**b
except CustomError as e:
    print(e)
    
#Using 'finally' clause
# finally clause is an optional one that can be used with try ... except clauses.
# All the statements under finally clause are executed irrespective of exception occurrence.
def divide(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Dividing by Zero.")
    finally:
        print("In finally clause.")
        

#Example 1
#Statements inside finally clause are executed in both function calls.
print('First call')
print(divide(14, 7))
print('Second call')
print(divide(14, 0))

# Using 'else' clause
# else clause is also an optional clause with try ... except clauses.
# Statements under else clause are executed only when no exception occurs in try clause.
try:
    a = 14 / 7
except ZeroDivisionError:
    print('oops!!!')
else:
    print('First ELSE')
try:
    a = 14 / 0
except ZeroDivisionError:
    print('oops!!!')
else:
    print('Second ELSE')
    

# Give a Try P3 # 7.1
# Write a script that reads a number from STDIN and raise ValueError exception 
# if the number is not between 0 and 100.


# Give a Try P3 # 7.2
# Write a script that reads a string from STDIN and raise ValueError exception 
# if the string has more than 10 characters. 


# Give a Try P3 # 7.3
# Write a script that handles opening a non-existing file 
# and prints the message File not found to the user. 


# Give a Try P3 # 7.4
# Define a class Circle, whose objects are initialized with radius as it's attribute.
# Ensure that the object creation raises RadiusInputError, a user defined exception, when the input radius is not a number.
# For e.g : Circle('hello') -> RadiusInputError : 'hello' is not a number 


