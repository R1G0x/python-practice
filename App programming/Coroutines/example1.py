#TokenIssuer is a coroutine function, which uses yield to accept name as input.
def TokenIssuer():
  tokenId = 0
  
  while True:
    name = yield 
    tokenId += 1
    print('Token number of', name, ':', tokenId)
    

t = TokenIssuer()

next(t)

t.send('George')
t.send('Rosy')
t.send('Smith')

# Execution of coroutine function begins only when next is called on coroutine t.
# This results in the execution of all the statements till a yield statement is encountered.
# Further execution of function resumes when an input is passed using send, and processes all statements till next yield statement.