def censor(text,word):
    slowo=text.split()

    stars=''
    for i in word:
        i='*'
        stars+=i

    num_slowa=0
    rezult=''
    for s in slowo:
        if s==word:
            slowo[num_slowa]=stars #zmiana przez index zmiennej w zbiorze
        num_slowa+=1 #okreslenie numeru zmiennej w zbiorze
    return ' '.join(slowo)

print censor("chuj w dupe","dupe")


