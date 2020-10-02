'''
Tick Tack Toe Board
10/1/20
'''

print("Welcome to tick tak toe!")
first_row = ['  |   |  ']
second_row = ['_   _   _']

def tick_tack_toe_board():
    for i in range(0, 3):
        print(first_row[0])
        if i < 2:
            print(second_row[0])

tick_tack_toe_board()
