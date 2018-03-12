# Write a if-elif-else blocks to determine grade obtained by a student based on the total average obtained. Use the below criteria to determine the grade.

# if total average >= 90, display "Distinct"
# if in range [60 -90), display "Above average"
# if in range [40 -60), display "Average"
# else display "Fail"
# Also determine the grade of a student with average score 68.3

grade = 68.3
if grade >= 90:
  print('Distinct')
elif 60 <= grade <= 90:
  print('Above average')
elif 40 <= grade <= 60:
  print('Average')
else:
  print('Fail')
