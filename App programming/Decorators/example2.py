def outer(func):
  def inner():
    print("Accessing :", func.__name__)
    return func()
  return inner
  
def greet():
  return 'Hello!'

greet = outer(greet) #Decorating greet

greet() #calling new greet

#The function returned by outer is assigned to greet i.e the function name passed as argument to outer
#this makes outer a decorator to greet.

