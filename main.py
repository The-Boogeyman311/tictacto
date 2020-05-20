#-----Gllobal Variable-------

#Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

#game_is_still_going
game_is_still_going = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (X goes first)
current_player = "X"


def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
  print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
  print(board[6] + " | " + board[7] + " | " + board[8] + " | ")
  

def play_game():  

  # Display initial board 
  display_board()

  while game_is_still_going:

    handle_turn(current_player)

    check_if_game_over()

    flip_player()


def handle_turn(player):
  position = input("Choose a position from 1 - 9 :")
  position = int(position) - 1

  board[position] = "X"

  display_board()


def check_if_game_over():
  check_if_win()
  check_if_tie()


def check_if_win():
  #check rows
  #check columns
  #check diagonals
  return

def check_if_tie():  
  return


def flip_player():
  return

play_game()


#board
#display board
#play game
#handle turn
#check win
  #check rows
  #check columns
  #check diagonals
#check tie
#flip player


