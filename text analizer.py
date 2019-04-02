
#1.sposob
#fukcja otwierajaca text
with open("text.txt") as f:
    text= f.read()
print text

#definiowanie alfabeu
alf="abcdefghijklmnoprstuwxyz "
for lit in alf:

#liczenie ilosi liter
    sum=0
    for i in text:
        if i==lit:
            sum+=1
    prec=(100*sum/float(len(text)))
    print "litera {0} wystepuje {1}% w texcie".format(lit,round(prec,2))

print ""

#2.sposob. wykorzystywanie juz przygotowanej fukcji
def sum_lit(text,l):
    sum=0
    for i in text:
        if i==l:
            sum+=1
    return sum

def procent(alf):
    for l in alf:
        procent=100*sum_lit(text,l)/float(len(text))
        print "lit. {0} jest {1}%".format(l,round(procent,2))

procent(alf)
