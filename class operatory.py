class mniej:
    def __init__(self,cont): #konstruktor clasy
        self.cont=cont

    def __gt__(self,other): #oprator wiekszosci
        for index in range(len(other.cont)+1):
            total=other.cont[:index]+">"+self.cont
            total+=">"+other.cont[index:]
            print total
    def __len__(self): #oprator dlugosci
       return len(self.cont)*2

znak1=mniej("dog")
znak2=mniej("pies")
result=znak1 > znak2
result
print len(znak1) #liczy znaki podwojnie

class dog: #uywanie atrybutow clasy za pomoca "__aa" i jego wywolanie
    __legs=4
    def __init__(self,name):
        self.name=name

frido=dog("dupa")
print frido._dog__legs
print ""
#przypomnienie funkcji @decor
def dec(fun):
    def abc():
        print "+"
        fun()
        print "-"
    return abc

@dec
def af():
    print "x*x"
af();

dupa=dec(af)
dupa()