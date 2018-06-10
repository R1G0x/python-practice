age = 0
if age:
  print('False conditions do not execute')

age = 1
if age:
  print('True conditions execute')
  
age = 17
if age >= 10:
  print('You are old enough')
else:
  print('You are too young to vote')
  
score = 91
print('The grade is: ', end=' ')
if score < 60:
  print('F')
elif 60 <= score < 70:
  print('D')
elif 70 <= score < 79:
  print('C')
elif 80 <= score < 90:
  print('B')
elif 90 <= score < 100:
  print('A')
else:
  print('Impossible')