# get and set methods of empid attribute are decorated with property
class Employee:
  
  def __init__(self, emp_id, emp_name):
    self.empid = emp_id 
    self.empname = emp_name
  
  @property
  
  def empid(self):
    return self.__empid
  
  @empid.setter
  
  def empid(self, value):
    if not isinstance(value, int):
      raise TypeError("'empid' must be an integer.")
    
    self.__empid = value

#get, set and del methods of empname are decorated with property
  @property
  
  def empname(self):
    return self.__empname
  
  @empname.setter
  
  def empname(self, value):
    if not isinstance(value, str):
      raise TypeError("'empname' must be a string.")
      
    self.__empname = value
  
  @empname.deleter
  def empname(self):
    del self.__empname

#deleter method corresponding to empname attribute is 
# called when the expression, del e1.empname is executed.

e1 = Employee(123456, 'Juan')
print(e1.empid, '-', e1.empname) #'123456 - John'
del e1.empname 
print(e1.empname)