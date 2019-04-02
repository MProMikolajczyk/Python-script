from random import randint

#generator losowych liczb
random_number = randint(1, 10)
#ilosc prob
guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(raw_input("Your guess: ")) #wprowadz liczbe
  if guess == random_number: #liczba rowna losowej
    print "You win!"
    break
  guesses_left -= 1 #spelnienie petli
  print "pozostalo prob: %s" %(guesses_left)
else:
  print "You lose."