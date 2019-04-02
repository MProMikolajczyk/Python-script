class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print "Hello, %s" % other.name

class CEO(Employee):
  def greet(self, other):
    print "Get back to work, %s!" % other.name

ceo = CEO("Emily") # zdefiniowanie pracownika Emily, wykonanie polecenia init
emp = Employee("Steve") #zdefiniowanie pracowanika Steve wykoanie poleceni init
emp.greet(ceo) # Pracownik Emily ma zrobić do co w klasie Employee w greet
ceo.greet(emp) # Pracownik Steve ma zrobić to co w clasie CEO

