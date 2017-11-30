# https://www.tutorialspoint.com/python/python_classes_objects.htm

class Employee:
   'Common base class for all employees'
   empCount = 0
   __test = 1

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
     print "Name : ", self.name,  ", Salary: ", self.salary

   def __printTest(self):
     print "__test = ", __test

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

   def myMethod(self):
      print 'Calling parent method'

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

   def myMethod(self):
      print 'Calling child method'

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

def main():
  "This would create first object of Employee class"
  emp1 = Employee("Zara", 2000)
  "This would create second object of Employee class"
  emp2 = Employee("Manni", 5000)
  emp1.displayEmployee()
  emp2.displayEmployee()
  print "Total Employee %d" % Employee.empCount
  #emp2.__printTest()

  setattr(emp2,'test',1)
  print 'emp2.test', emp2.test

  print 'Employee.__doc__:', Employee.__doc__
  print 'Employee.__name__:', Employee.__name__
  print 'Employee.__module__:', Employee.__module__
  print 'Employee.__bases__:', Employee.__bases__
  print 'Employee.__dict__:', Employee.__dict__

  c = Child()          # instance of child
  c.childMethod()      # child calls its method
  c.parentMethod()     # calls parent's method
  c.setAttr(200)       # again call parent's method
  c.getAttr()          # again call parent's method
  c.myMethod()         # child calls overridden method

  v1 = Vector(2,10)
  v2 = Vector(5,-2)
  print v1 + v2

if __name__ == "__main__":
  main()
