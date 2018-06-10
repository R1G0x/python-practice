def greet():
  return 'Hello Everyone!'

print(greet())

# 'greet' function assigned to variable 'wish'
wish = greet

print(type(wish))
print(wish())