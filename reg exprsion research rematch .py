import re

pattern=r"dupa" #definiowanie czego szukamy
#re.match
if re.match(pattern,"adupaojakadupa"): #szuka tylko na poczatku czy jest
    print ("Jest")
else:
    print ("Nie ma")

#re.search
if re.search(pattern,"adupaojakadupa"): #szuka wszedzie
    print ("Jest")
else:
    print ("Nie ma")

#re.findall
print re.findall(pattern,"adupaojakadupa") #tworzy liste z tego co szukamy

#re.finditer
if re.finditer(pattern,"adupaojakadupa"): #szuka tworzoa listy i ileruje je (poddaje petli)
    print ("Jest")
else:
    print ("Nie ma")

#podmiana text za pomoca re.sub
string="Siema tu dupa"
pattern2=r"dupa"
print re.sub(pattern2,"chuj",string)

#Metaclass dot (".")
def Metaclass_dot():
    pattern=r"sp.m"
    lista=["spam","spum","spim","sram"]
    for i in lista:
        if re.match(pattern,i):
            print "{} match \t\t{}".format(i,pattern) #\t to taki tabuloator przestrzen
        else:
            print "{} doesnt match \t{}".format(i,pattern)

Metaclass_dot()

#Metaclass "^","$"
def Meta_zk():
    pattern=r"^du.a$"
    if re.search(pattern,"dupa"):
        print "Y1"
    if re.search(pattern,"zdupa"): #tego nie wyswietla do "zdupa" nie zaczyna sie du
        print "Y2"

Meta_zk()