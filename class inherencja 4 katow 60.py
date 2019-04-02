class Triangle(object): #classy z katami
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3

  def check_angles(self): #spr. czy dla 180 jest true czy false
    if (self.angle1 + self.angle2 + self.angle3) == 180:
      return True
    else:
      return False
class Equilateral(Triangle): #przypisanie salej wartosci katow
    angle=60
    def __init__(self):
      self.angle1 = self.angle
      self.angle2 = self.angle
      self.angle3 = self.angle

my_triangle1 = Triangle(70,60,10) #definicja metody Triangle
my_triangle2 = Equilateral() #definicja metody Equilateral
print my_triangle1.check_angles() #wyduk metody Triangle
print my_triangle2.check_angles() #wydruk inherencji z metody Triangle za pomoca metody Equilateral
print my_triangle2.angle1 #wydruk parametru z metody Equilateral