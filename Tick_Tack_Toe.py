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
# Check for a winning or tie condition
# Outcome message
# Ascii art
# Would you like to play again message if y refresh if n exit

print("Welcome to tick tack toe!")
num_of_players = input("Choose the number of players. Valid inputs are: 0, 1, or 2. ")
print(f'You have chosen {num_of_players} players.')
choose_x_or_o = input("Chose X or O. ")
upper_case_x_o = choose_x_or_o.upper()
print(f'You have chosen {upper_case_x_o}.')
#The code is telling the players is they are going to be x or o based on the first input.
if upper_case_x_o == "X":
    print("Player 1 is X's, Player 2 is O's")
else:
    print("Player 1 is O's and player 2 is X's")

first_row = ['  |   |  ']
second_row = ['_   _   _']

def tick_tack_toe_board():
    for i in range(0, 3):
        print(first_row[0])
        if i < 2:
            print(second_row[0])


tick_tack_toe_board()
