
def fun(x):
    if x==1:
        return 1
    else:
        return x*fun(x-1)


print fun(5)

#rozwianie zagadki x=5
#fun(5) daje 5*(5-1)=20
#potem  daje 20*(4-1)=60
#potem  daje 60*(3-1)=120
#potem  daje 120*(2-1)=120
#potem dla x rowne 1 fukcja przyjmuje wartosc 1


