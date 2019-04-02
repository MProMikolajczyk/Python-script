class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee): # zdefiniowanie nazwy pracownika przez classe Employer i skorzystanie z niej. dotyczy init, tego co ona wykonuje
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  def full_time_wage(self,hours):
#tutaj wazne jest to ze PartTimeEmployee odnosi sie do siebe (self), a calculate_wage dotyczy paramtru hours. Bez podania tego fukcja nie bedzie dzialac
    return super(PartTimeEmployee,self).calculate_wage(hours) #super przywoliuje do 1 fukkcji gdzie wystapila ta nazwa. w tym wypadku naspil powrot do classy poprzednie i tam zosalo wykonane zadanie

milton=PartTimeEmployee("Milton")
print milton.full_time_wage(10) # funkcja wykonana w klasie poprzedniej
print milton.calculate_wage(2) # fuknkcja calculate_wage ostatnia pytana