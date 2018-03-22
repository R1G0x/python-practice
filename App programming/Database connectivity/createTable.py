import sqlite3

#Establish a database connection
con = sqlite3.connect('TEST.db')

#Preparing a cursor object
cursor = con.cursor()

#Preparing sql statements
sql1 = 'DROP TABLE IF EXISTS EMPLOYEE'

sql2 = '''
        CREATE TABLE EMPLOYEE (
          EMPID INT(6) NOT NULL,
          NAME CHAR(20) NOT NULL,
          AGE INT,
          SEX CHAR(1),
          INCOME FLOAT
        )
       '''

#Executing sql statements
cursor.execute(sql1)
cursor.execute(sql2)

#closing the connection
con.close()
