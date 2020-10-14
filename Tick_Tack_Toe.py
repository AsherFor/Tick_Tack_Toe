'''
Asher Forman
Tick Tack Toe Board
10/1/20
'''
# Welcome Code
# draw board
# Choose number of players 0, 2
# Choose x or o
# Pick who goes first
# Place first entry on the board
# Gameplay
# We need to do an insertion of an x or an o into an array
# Check for a winning or tie condition
# Outcome message
# Ascii art
# Would you like to play again message if y refresh if n exit

win_condition = False

print("Welcome to tick tack toe!")
#Why do we need multiple players
num_of_players = input("Choose the number of players. Valid inputs are: 0, 1, or 2. ")
print(f'You have chosen {num_of_players} players.')
player1_x_or_o = input("Chose X or O. ")
upper_case_x_o = player1_x_or_o.upper()
#What happens if they don't click X or O
print(f'You have chosen {upper_case_x_o}.')

#The code is telling the players if they are going to be X's or O's based on the first input.
if upper_case_x_o == "X":
    player2_x_or_o = "O"
    print("Player 1 is X's, Player 2 is O's")
else:
    player2_x_or_o = "X"
    print("Player 1 is O's and player 2 is X's")

board = [
    [" ", " ", ""],
    [" ", " ", " "],
    [" ", " ", " "]
]

def player_1_turn():
    player1_row = input("Player 1, pick your row. ")
    player1_col = input("Player 1, pick your col. ")

    int_player1_row = int(player1_row)
    int_player1_col = int(player1_col)


    print(f'Player 1 picked row {int_player1_row} and column {int_player1_col}')

    board[int_player1_row] [int_player1_col] = player1_x_or_o

def player_2_turn():
    player2_row = input("Player 2, pick your row. ")
    player2_col = input("Player 2, pick your col. ")

    int_player2_row = int(player2_row)
    int_player2_col = int(player2_col)

    print(f'Player 2 picked row {int_player2_row} and column {int_player2_col}')
    board[int_player2_row] [int_player2_col] = player2_x_or_o



def didIWin():
    global win_condition
    #How do you make a tie condition
    #Row 0 Across
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] != " ":
        win_condition = True

    #Column 0 Down
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != " ":
        win_condition = True

    #Row 1 Across
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] != " ":
        win_condition = True

    #Column 1 Down
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] != " ":
        win_condition = True

    #Row 2 Across
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] != " ":
        win_condition = True

    #Column 2 Down
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] != " ":
        win_condition = True

    #Diagonal Starting with Row and Column 0
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != " ":
        win_condition = True

    #Diagonal Starting Row 0 Column 2
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != " ":
        win_condition = True
    else:
        print("No one has one yet, keep playing.")


def drawBoard():
    print(f'''
        0 1 2
       _______
    0 | {board[0][0]}|{board[0][1]}|{board[0][2]} |
      | -+-+- | 
    1 | {board[1][0]}|{board[1][1]}|{board[1][2]} |
      | -+-+- |                                    
    2 | {board[2][0]}|{board[2][1]}|{board[2][2]} | 
       -------
    ''')

# def game_play():
#     player_1_turn()
#     drawBoard()
#     didIWin()
#     player_2_turn()
#     drawBoard()
#     didIWin()
#How do I make the win condition
while win_condition == False:
    player_1_turn()
    drawBoard()
    didIWin()
    if win_condition == True:
        print("Congratulations, Player 1 won the Game!")
        print("♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪")
        play_again_or_end = input("Type y to play again, or type n to stop.")
        if play_again_or_end == "y" or "Y":
            win_condition = False
            player_1_turn()
        else:
            print("Game over!")
            exit()
    player_2_turn()
    drawBoard()
    didIWin()
    if win_condition == True:
        print("Congratulations, Player 2 won the Game")
        print("♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪")
        play_again_or_end = input("Type y to play again, or type n to stop.")
        if play_again_or_end == "n" or "o":
            print("hi")
        else:
            print("Game over!")
            exit()
# while True:
#     game_play()

