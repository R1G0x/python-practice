# Consider the string 's' having the value 'tata consultancy services limited'
# Determine the no. of vowels present in it, using for loop. Store the number in variable 'count' and print it.

s = 'tata consultancy services limited'
s = list(s)
count = 0
for char in s:
  if char in ('aeiouAEIOU'):
    count+=1
print(count)