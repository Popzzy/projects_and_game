# Tic_tac_toe

import random

def drow_board(board):
	#This fanction prints out the board that it was passed.
	#'board' is a list of 10 strings representing the board(ignore index 0).
	
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[1] + '|' + board[2] + '|' + board[3])

def input_player_letter():
	#lets the player type which letter they want to enter
	#Return a list with the player's letter as the first item and the computer's letter as the second.
	letter = ''
	while not(letter == 'X' or letter == 'O'):
		print('Do you want to be x or o ?')
		letter = input().upper()

	# The first element in the list is the player's letter; the second is the computer's letter.
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def Who_Goes_first():
	#Rondomly choose which player goes first.
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'

def make_move(board, letter, move):
	board[move] = letter

def is_winner(bo, le):
	#Given a board and a player's letter, this function returns True if that player has won.
	#we use 'bo' instead of 'board' and 'le' instead of 'letter' so we don't type so much 
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or #Across the middle top
	(bo[4] == le and bo[5] == le and bo[4] == le) or # Across the middle
	(bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
	(bo[7] == le and bo[4] == le and bo[1] == le) or #down the left side
	(bo[8] == le and bo[5] == le and bo[2] == le) or #down the middle
	(bo[9] == le and bo[6] == le and bo[3] == le) or #down the right side
	(bo[9] == le and bo[5] == le and bo[1] == le) or #Diagonal
	(bo[7] == le and bo[5] == le and bo[3] == le))#Diagonal

def get_Board_copy(board):
	#make a copy of the board list and return it.
	boardCopy = []
	for i in board:
		boardCopy.append(i)
	return boardCopy

def is_Space_Free(board, move):
	#return True if the possed move is free on the passed board.
	return board[move] == ' '

def Get_Player_move(board, move):
	#let the player enter their move
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_Space_Free(board, int(move)):
		print("What is your next move? (1-9)")
		move = input()
	return int(move)
	
def ChooseRandomMoveFromList(board, moveList):
	#Return a valid move from the passed list on passed board.
	#Return None if there is no valid move.
	possssibleMoves = []
	for i in moveList:
		if is_Space_Free(board, i):
			possssibleMoves.append(i)

	if len(possssibleMoves) != 0:
		return random.choise(possssibleMoves)
	else:
		return None

def get_computer_move(board, computerLetter):
	#Give a board and the computer's letter, determine where to move and return the move.
	if computerLetter == 'X':											 				 				
 		playerletter = 'O'
	else:
 		playerletter = 'X'
 			
	#Here is the algorithim for our tic-tac-toe IQ:
 	#first, check if we can win in the next move.
	for i in range(1,10):
 		boardCopy = get_Board_copy(board)
 		if is_Space_Free(boardCopy, i):
 			make_move(boardCopy, computerLetter, i)
 			if is_winner(boardCopy, computerLetter):
 				return i

 	#check if the player could win on their next move and block them.
	for i in range(1, 10):
		boardCopy = get_Board_copy(board)
		if is_Space_Free(boardCopy, i):
			make_move(boardCopy, playerletter, i)
			if is_winner(boardCopy, playerletter):
				return i

	# Try to take one of the corners, if they are free.
	move = ChooseRandomMoveFromList(board, [1, 3, 7, 9])
	if move != None:
		return move

	#Try to take the center, if it is free.
	if is_Space_Free(board, 5):
		return 5

	# Move on one of the sides.
	return ChooseRandomMoveFromList(board, [2, 4, 6, 8])

def is_Board_Full(board):
	#Return True if every space on the board has been taken . Otherwise, return False
	for i in range(1, 10):
		if is_Space_Free(board, i):
			return False
	return True


print("Welcome to Tic-Tac-Toe!")

while True:
	# Reset the board.
	theBoard = [' ']* 10
	playerletter, computerLetter = input_player_letter()
	turn = Who_Goes_first()
	print("The " + turn + ' will go first.')
	gameIsPlaying = True

	while gameIsPlaying:
		if turn == 'player':
			# player's turn
			drow_board(theBoard)
			move = Get_Player_move(theBoard)
			make_move(theBoard, playerletter, move)

			if is_winner(theBoard, playerletter):
				drow_board(theBoard)
				print("Hooray! You have won the game!")
				gameIsPlaying = False
			else:
				if is_Board_Full(theBoard):
					drow_board(theBoard)
					print("The game is a tie!")
					break
				else:
					turn = 'computer'

		else:
			# Computer's turn
			move = get_computer_move(theBoard, computerLetter)
			make_move(theBoard, computerLetter, move)

			if is_winner(theBoard, computerLetter):
				drow_board(theBoard)
				print("The computer has beaten you! You lose.")
				gameIsPlaying = False
			else:
				if is_Board_Full(theBoard):
					drow_board(theBoard)
					print("The game is a tie!")
					break
				else:
					turn = "player"

	print("Do you want to play again? (yes/no)")
	if not input().lower().startswith("y"):
		break									

 
			 					
 			
