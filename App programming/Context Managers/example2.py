import sqlite3

class DbConnect(object):
  
  def __init__(self):
    self.dbConnection = sqlite3.connect(self.dbname)
    return self.dbConnection
    
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.dbConnection.close()

with DbConnect('TEST.db') as db:
  cursor = db.cursor()
  
  # Few db operations