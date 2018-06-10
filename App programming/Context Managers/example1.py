# consider the following example, which tries to establish a connection to a database,
# perform few db operations and finally close the connection.

import sqlite3

try:
  dbConnection = sqlite3.connect('TEST.db')
  cursor = dbConnection.cursor()
  
  # '''
  
  # Few db operations
  
  # '''
  
  # '''

except Exception:
  print('No Connection.')

finally:
  dbConnection.close()
  