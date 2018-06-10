#Write a python program to:
# Get user input of a first name and last name
# Print the names reversed, but in the same order
# eg. Graham Smith = maharG htimS
#Try to find more than one method
firstName = input('First name: ')
lastName = input('Last name: ')
print(firstName,'=',firstName[::-1])
print(lastName,'=',lastName[::-1])

name = input('First name and last name')
words = name.split(' ')
for word in words:
  lastIndex = len(word) -1
  for index in range(lastIndex, -1, -1):
    print(word[index], end=' ')
  print(end=' ')
print(end='\n')

name = input('First name and last name')
first, last = name.split(' ')
print(first[::-1], last[::-1])