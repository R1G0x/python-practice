# from contextlib import contextmanager

# @contextmanager
# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)

# with tag('h1') :
#     print('Hello')

from contextlib import contextmanager

@contextmanager
def context():
    print('Entering Context')
    yield 
    print("Exiting Context")

with context():
    print('In Context')