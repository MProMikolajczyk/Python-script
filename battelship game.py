from random import randint

board = []

#kolumny
for x in range(0, 5):
  board.append(["O"] * 5)

#wiersze
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

#losowanie liczby z wierszy
def random_row(board):
  return randint(0, len(board) - 1)

#losowanie liczby z kolumn
def random_col(board):
  return randint(0, len(board[0]) - 1)

#pokazuje co wylosowalo
ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

#tury
for turn in range(4):
    #wprowadzanie danych
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

    #wygrana
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break
  else:
      #jesli wybierze sie liczbe za obszarem
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
      #jezli wybierzes jeszcze raz to samo czyli juz jest x
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
      #jezeli nie trafisz to poajawiaja sie X w miejsce O
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    print_board(board)

    #jezeli przekroczysz 4 tury
    if turn==3:
      print "Game Over"
#wydruk obecnej tury
  print "Turn", turn+1
