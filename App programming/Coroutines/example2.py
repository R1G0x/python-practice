def TokenIssuer(tokenId=0):
    try:
        while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)

    except GeneratorExit:
        print('Last issued Token is :', tokenId)



t = TokenIssuer(100)

next(t)


t.send('George')
t.send('Rosy')
t.send('Smith')
t.close()

# In Example 2, the coroutine function TokenIssuer takes an argument, 
# which is used to set a starting number for tokens.

# When coroutine t is closed, statements under GeneratorExit block are executed.
