class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,z): #dzieki temu mozna dodoac dwie funckje
        return (self.x + z.x,self.y + z.y)

vector1=Vector(5,7)
vector2=Vector(4,3)
print vector1.x,vector1.y
print vector2.x,vector2.y
result=vector1+vector2
print result

print ""

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __rtruediv__(self, other):
        line = '=' * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello) #to nie dziala error type nie wiadomo dlaczego
