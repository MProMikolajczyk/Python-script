def is_prime(x):
    if x < 2:
        return False
    else:
        num=x
        while x>2:
            x-=1
            t=float(num)%x
            if t==0:
                return False # nie moze byc dalej else bo wystarczy ze jedna jest True i wszystkie sa. Moze by print i wtedy dziala else z True
        return True #wazna linika zwraca True do calej funkcji jezeli wszytki argumenty sa true



print is_prime(1)
print is_prime(2)
print is_prime(3)
print is_prime(4)
print is_prime(5)
print is_prime(6)
print is_prime(7)
print is_prime(8)
print is_prime(9)



