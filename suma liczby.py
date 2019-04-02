def sumowanie(l):
    l=str(l) #zmiana na string
    z=[]
    total=0
    for i in l:
        z.append(int(i)) #dodanie do listy zmiennych int
    for x in z:
        total+=x #suma zmiennych
    print total

sumowanie(123456)


