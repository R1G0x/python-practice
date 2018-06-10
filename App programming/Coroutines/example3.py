# As seen in Example1 and Example2, passing input to coroutine is possible only after the first next function call.
# Many programmers may forget to do so, which results in error.
# Such a scenario can be avoided using a decorator as shown in Example 3.

def coroutine_decorator(func):
  def wrapper(*args, **kwdargs):
    c = func(*args, **kwdargs)
    
    next(c)
    return c
  
  return wrapper

#################################
@coroutine_decorator
def TokenIssuer(tokenId=0):

    try:
        while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)

    except GeneratorExit:
        print('Last issued Token is :', tokenId)


# In Example 3, coroutine_decorator takes care of calling next on the created coroutine t.
t = TokenIssuer(100)
t.send('George')
t.send('Rosy')
t.send('Smith')
t.close()