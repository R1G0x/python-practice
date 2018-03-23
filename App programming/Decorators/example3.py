# In Python, decorating a function can also be achieved by writing decorator function name, 
# prefixed with @ symbol, just above the function to be decorated.
# Hence, greet = outer(greet) expression is same as @outer.

def outer(func):
    def inner():
        print("Accessing :", 
                func.__name__)
        return func()
    return inner

@outer

def greet():
    return 'Hello!'

greet()
