def outer():
  def inner():
    s = 'Hello world!'
    return s
  
  return inner()

print(outer())

#You can observe from the output that the return value of 'outer'
# function is the return value of 'inner' function i.e. 'Hello World!'
def outer(x, y):

    def inner1():
        return x+y

    def inner2(z):
        return inner1() + z

    return inner2


f = outer(10, 25)

print(f(15))

v = 'Hello'

def f():
    v = 'World'
    return v

print(f())
print(v)

def outer(x, y):

    def inner1():
        return x+y

    def inner2():
        return x*y

    return (inner1, inner2)


(f1, f2) = outer(10, 25)

print(f1())
print(f2())