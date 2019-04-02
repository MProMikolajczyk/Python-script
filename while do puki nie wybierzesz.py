#funkcja while do puki nie wybierzesz y/n
choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # do puku nie jest rowne y i n
  choice = raw_input("Sorry, I didn't catch that. Enter again: ") #co stanie sie jak nie wybierzesz y albo n