#dwa spsoby reserwed po rozbicu
#1 sposob przez while
x="abcd"
def reverse(x):
    word = ""
    l = len(x) - 1
    while l >= 0:
        word = word + x[l]
        l -= 1
    print word

reverse(x)

#2 sposob przez for
def dwa(x):
    l=1
    for i in x:
        i=x[len(x)-l]
        l+=1
        print i,


dwa(x)

