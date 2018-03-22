import sqlite3

#Establish the connection
con = sqlite3.connect('TEST.db')

#prepare a cursor object
cursor = con.cursor()

#Prepare sql statement

sql = '''
        SELECT * FROM EMPLOYEE
      '''

#Execute the sql statement using try ... except

try:
  cursor.execute(sql)
except:
  print('Unable to fetch data.')
  
#Fetching the records
records = cursor.fetchall()

#Display the records
for record in records:
  print(record)

#close the connection 
con.close()