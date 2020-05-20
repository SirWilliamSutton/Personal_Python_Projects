
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('--|---|--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|---|--')
    print(board[1]+' | '+board[2]+' | '+board[3])
    


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Welcome to the glorious game of Tic-Tak-Toe! I Shall be your host, Winston.\nThe positions are set up like that of a numpad, with the bottom left position being one, and the top right position being nine. \nYou will be player1, your input must be capitalized. Which marker would you like, X or O?: ')
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 ='X'
    return (player1,player2)


def place_marker(board, marker, position):
    
    board[position] = marker
    
def win_check(board, mark):
    
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark))

import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'player1'
    else:
        return 'player2'
    
def space_check(board, position):
    
    return board[position] == ' '


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board):
    
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose a position. (1-9'))
    return position

def replay():
    
    choice = input('Play again? Enter Yes or No: ').capitalize()
    return choice == 'Yes'


print('Welcome to Tic Tac Toe!')

while True:
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Ready to play? y or n?')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        
        if turn =='player1':
            
            #show the board
            
            display_board(the_board)
             # choose a position
            position = player_choice(the_board)
                
            # place the position
            place_marker(the_board, player1_marker, position)
            
            # check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!!')
                game_on = False
                
                #check if tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                    
                     # no tie and no win - next players turn
                else:
                    turn = 'player2'
                    
        if turn =='player2':
            
            #show the board
            display_board(the_board)
            
             # choose a position    
            position = player_choice(the_board)
                
            # place the position
            place_marker(the_board, player2_marker, position)
            
            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!!')
                game_on = False
                
                 #check if tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                    
                     # no tie and no win - next players turn
                else:
                    turn = 'player1'
    
    if not replay():
        print('Thanks for playing Winton\'s tictactoe!')
        break





















