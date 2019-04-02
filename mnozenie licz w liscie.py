lista=[2,4,6]

def product(lista):
    total=1 #pierwszu sposob mnozenia zmiennych w liscie
    for i in lista:
        total*=i
    return total

def product2(lista):
    totali=1 #drugi sposob mnozenia zmiennych w liscie
    l=len(lista)
    while l>0:
        l-=1
        totali*=lista[l]
    return totali

print product(lista)
print product2(lista)