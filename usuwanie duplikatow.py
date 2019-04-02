# 1 spsob
def remove_duplicates(lista):
    lista2=[]
    lista3=[]
    sumlista=[]
    lista.sort()
    l=0
    while len(lista)>l:
        if lista[l]>lista[l-1]: #odewanie poprzedniej od nastepnej tak aby w range sie zmiescic
            lista2.append(lista[l])
        l+=1
    lista3.append(lista[0]) #dodanie pierszego skladniaka bo nigdy nie bedzie mniejszy od siebie samego
    sumlista=lista2+lista3 #suma wszystkich list
    sumlista.sort()
    return sumlista

print remove_duplicates([1,2,2,3,1,4,1])


#2 spspob
inputlist=[4,5,6,6,7]


inputlist = sorted(inputlist)
print inputlist

outputlist = [inputlist[0]] #to jest dziwne!!!

for i in inputlist:
    if i > outputlist[-1]: # to oznacza nic innego jak 1 wstecz
        print outputlist[-1]
        outputlist.append(i)
        print outputlist

#wyjasnienie tego dziwnego znawiska
z=[[3,5,7]]
print z[0]
print z[-1]



