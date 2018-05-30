import os
import random

def clear():

	os.system('cls')

# Display board
def display_board(board):

        clear()
        print('   |   |   ')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |   ')

# Assign player markers
def player_input():

	marker = ''
	
	while not (marker == 'O' or marker == 'X'):
		marker = raw_input('Player 1: Do you want to be X or O? ').upper()

	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

# Assign markers to positions on board
def place_marker(board, marker, position):

        board[position] = marker
        
def win_check(board, mark):
        
        return ((board[7] == mark and board[8] == mark and board[9] == mark) or # Across top
                (board[4] == mark and board[5] == mark and board[6] == mark) or # Across middle
                (board[1] == mark and board[2] == mark and board[3] == mark) or # Across bottom
                (board[7] == mark and board[4] == mark and board[1] == mark) or # Down left
                (board[8] == mark and board[5] == mark and board[2] == mark) or # Down middle
                (board[9] == mark and board[6] == mark and board[3] == mark) or # Down right
                (board[7] == mark and board[5] == mark and board[3] == mark) or # Diagonal
                (board[9] == mark and board[5] == mark and board[1] == mark)) # Diagonal

# Randomly decide which player goes first
def choose_first():

        if random.randint(0, 1) == 0:
                return 'Player 1'
        else:
                return 'Player 2'

# Check if a space on the board is available
def space_check(board, position):

        return board[position] == ' '

# Check if board is full
def full_board_check(board):

        for i in range(1, 10):
        	if space_check(board, i):
        		return False
        return True

# Get next position
def player_choice(board):

        position = ' '

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or not space_check(board, int(position)):
                position = raw_input('Choose your next position: (1 - 9) ')
        return int(position)

# Play Again
def replay():

        return raw_input('Play again? Enter Yes or No: ').lower().startswith('y')

print('Tic Tac Toe')

while True:

        gameBoard = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first!')

        game_on = True

        while game_on:

                if turn == 'Player 1':
                        display_board(gameBoard)
                        position = player_choice(gameBoard)
                        place_marker(gameBoard, player1_marker, position)

                        if win_check(gameBoard, player1_marker):
                                display_board(gameBoard)
                                print('Congratulations, Player 1 wins!')
                                game_on = False
                        else:
                                if full_board_check(gameBoard):
                                        display_board(gameBoard)
                                        print('Draw!')
                                        break
                                else:
                                        turn = 'Player 2'
                else:
                        display_board(gameBoard)
                        position = player_choice(gameBoard)
                        place_marker(gameBoard, player2_marker, position)

                        if win_check(gameBoard, player2_marker):
                                display_board(gameBoard)
                                print('Congratulations, Player 2 wins!')
                                game_on = False
                        else:
                                if full_board_check(gameBoard):
                                        display_board(gameBoard)
                                        print('Draw!')
                                        break
                                else:
                                        turn = 'Player 1'
        if not replay():
                break