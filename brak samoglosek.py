# pierwszy sposob
def anti_vowel1(text):
    t=""
    for i in text:
        if i=="e" or i=="o" or i=="u" or i=="i" or i=="a" or i=="E" or i=="O" or i=="U" or i=="I" or i=="A":
             i=""
        else:
             t+=i
    return t


print anti_vowel1("Hey you!")


# drugi sposob
def anti_vowel2(text):
    t=""
    for c in text:
        for i in "ieaouIEAOU": #dla kazdego wyraz i ze zboiru samoglosek
            if c==i:
                c=""
            else:
                c=c
        t=t+c
    return t

print anti_vowel2("Hey you!")

