score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


text="Dupa biskupa"
text=text.lower()


#pierwszy sposob scrabli
def sclable1(text):
    total_score=0
    for li in text:
        if li in score:
            war=score[li]
        total_score+=war
    return total_score

print sclable1(text)

#drugi spsob scrabli
def sclable2(text):
    total_score=0
    for li in text:
        for z in score:
            if z==li:
                war=score[z]
        total_score+=war
    return total_score


print sclable2(text)



