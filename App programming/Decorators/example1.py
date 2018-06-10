def outer(func):
  
  def inner():
    print("Accessing :", func.__name__)
    return func()
  
  return inner

def greet():
  return 'Hello!'
  
wish = outer(greet)

wish()

# wish is the closure function obtained by calling an outer
# function with the argument greet.

# When wish function is called, inner function gets executed.
def decorator_func(func):
    def wrapper(*args, **kwdargs):
        return func(*args, **kwdargs)
    wrapper.__name__ = func.__name__
    return wrapper


@decorator_func
def square(x):
    return x**2

print(square.__name__)

from functools import wraps

def decorator_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def square(x):
    return x**2

print(square.__name__)

def bind(func):
    func.data = 9
    return func

@bind
def add(x, y):
    return x + y

print(add(3, 10))
print(add.data)