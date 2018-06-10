# The descriptor, EmpNameDescriptor is defined to manage
# empname attribute.

# It checks if the value of empname attribute is a string or not.
class EmpNameDescriptor:
  
  def __get__(self,obj,owner):
    return self.__empname
  
  def __set__(self, obj, value):
    if not isinstance(value, str):
      raise TypeError("'empname' must be a string.")
    
    self.__empname = value


#The descriptor, EmpIdDescriptor is defined to manage empid attribute

class EmpIdDescriptor:
  
  def __get__(self, obj, owner):
    return self.__empid
    
  def __set__(self, obj, value):
    if hasattr(obj, 'empid'):
      raise ValueError("'empid' is read only attribute")
    
    if not isinstance(value, int):
      raise TypeError("'empid' must be an integer.")
    
    self.__empid = value
    

#Employee class is defined such that, it creates empid and empname
# attributes from descriptors EmpIdDescriptor and EmpNameDescriptor
class Employee:
  
  empid = EmpIdDescriptor()
  empname = EmpNameDescriptor()
  
  def __init__(self, emp_id, emp_name):
    self.empid = emp_id
    self.empname = emp_name


# You can observe that accessing attributes empid and
# empname appear as if you are accessing them directly

# However when executing the expression e1.empid = 76347322,
# the __set__ method defined in EmpIdDescriptor
# is executed and raises "ValueError: 'empid' is read only attribute"
e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)

e1.empname = 'Williams'
print(e1.empid, '-', e1.empname)

e1.empid = 76347322

