import sqlite3

#Establishing the connection
con = sqlite3.connect('TEST.db')

#Preparing a cursor object
cursor = con.cursor()

#preparing sql statement
rec = (456789, 'Frodo', 45, 'M', 100000.00)

sql = '''
        INSERT INTO EMPLOYEE VALUES (?,?,?,?,?)
      '''
      
#executing sql statement using try ... except blocks

try:
  cursor.execute(sql, rec)
  con.commit()
except Exception as e:
  print("Error Message: ", str(e))
  con.rollback()

#closing the database connection
con.close()