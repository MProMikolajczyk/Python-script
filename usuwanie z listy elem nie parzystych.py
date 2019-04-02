lista =[1,2,3,4,7,9,2]

def purify(lista):
    lista2=[]
    for s in range(len(lista)):
        if lista[s]%2==0: #spr zmiena z lisy podzielna przez 2
            lista2.append(lista[s])
    return lista2

print purify(lista)








