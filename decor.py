def d(x):
    def y():
        print "Start"
        x()
        print"Koniec"
    return y

def d2(x):
    def y():
        print "1"
        x()
        x()
        x()
        print"2"
    return y



@d #odwolanie do fukcji d(x) okreslanie co ma zrobic
@d2 # zagniezdzenie fukcji d2(x)
def h():
    print"chuje" #definiowanie co fykcjia na wstawic

#h(); #wazny znak to sie odwoduje do zdefiniowanej funkcji