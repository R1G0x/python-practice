class Employee:
  def __init__(self, emp_id, emp_name):
    self.empid=emp_id
    self.empname=emp_name
  
  def getEmpID(self):
    return self.__empid
  
  def setEmpID(self, value):
    if not isinstance(value, int):
      raise TypeError("'empid' must be an integer.")
    
    self.__empid = value
  # empid attribute created using property  
  empid = property(getEmpID, setEmpID)
  
  # empname attribute created using property.
  # It is deleted when delEmpName method is called.
  def getEmpName(self):
    return self.__empname
    
  def setEmpName(self, value):
    if not isinstance(value, str):
      raise TypeError("'empname' must be a string.")
    
    self.__empname = value
  
  def delEmpName(self):
    del self.__empname
  
  empname = property(getEmpName, setEmpName, delEmpName)

#When del e1.empname is executed, it in turn calls 
# delEmpName method

#Hence accessing empname attribute after the del expression
# results in AttributeError
e1 = Employee(123456, 'John')
  
print(e1.empid, '-', e1.empname) # -> '123456 - John'
  
del e1.empname #Deletes 'empname'
  
print(e1.empname) #raises 'AttributeError'