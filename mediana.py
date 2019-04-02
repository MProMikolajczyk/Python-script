def median(lista):
    lista.sort()
    l=len(lista)
    l2=l/2
    #zbior liczb parzystych
    if l%2==0:
        lpm=l2-1
        ls=float(lista[l2])/2+float(lista[lpm])/2
        return ls
    #zbior licz nieparzystych
    else:
        lnp=lista[l2]
        return lnp

print median([1,3,8,11,13,15])

