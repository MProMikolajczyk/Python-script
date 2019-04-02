def count(item,sequence): #funkcja spr. ile raz w liscie jest drugi argument
    lista=[]

    l=len(item) #chyba daje odpowiedni type()
    while l>0:
        l-=1
        if item[l]==sequence:#miejsce w liscie zalezne od numeru w zmiennej w liscie
            lista.append(sequence)#dodanie do listy
    return len(lista)


print count(["a","a",2,3,1,1],"a")
