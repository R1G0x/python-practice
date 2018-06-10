def stringDisplay():
    while True:
        s = yield
        print(s*3)


c = stringDisplay()
next(c)
c.send('Hi!!')

def nameFeeder():
    while True:
        fname = yield
        print('First Name:', fname)
        lname = yield
        print('Last Name:', lname)

n = nameFeeder()
next(n)
n.send('George')
n.send('Williams')
n.send('John')