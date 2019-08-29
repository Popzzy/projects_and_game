#!/usr/bin/ env python
#old_draft.py  -- old draft game 
import random

def draw(board):
	#the out put of the game

	print(board[7] + ' -------------'+ board[8] + ' -------------' + board[9])
	print('|  \           |           /  |')
	print("|   \          |          /   |")
	print("|    \         |         /    |")
	print("|     \        |        /     |")
	print("|      \       |       /      |")
	print("|       \      |      /       |")
	print("|        \     |     /        |")
	print("|         \    |    /         |")
	print("|          \   |   /          |")
	print("|           \  |  /           |")
	print("|            \ | /            |")
	print("|             \|/             |")
	print(board[4] + ' -------------' + board[5] + '-------------' + board[6])
	print("|            /| \             |")
	print("|           / |  \            |")
	print("|          /  |   \           |")
	print("|         /   |    \          |")
	print("|        /    |     \         |")
	print("|       /     |      \        |")
	print("|      /      |       \       |")
	print("|     /       |        \      |")
	print("|    /        |         \     |")
	print("|   /         |          \    |")
	print("|  /          |           \   |")
	print("| /           |            \  |")
	print(board[1] + ' ------------'+ board[2] + '------------- ' + board[1])

def input_letters():
	#we use 'x' and 'o'
	#one will select what to use
	letter = ''
	while not(letter== 'X' or letter == 'O'):
		print('Would you like to be "x" or "o"?')
		letter = input().upper()
		"""change into upper case"""
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', "X"]

def who_play_first():
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'

def make_move(board, letters, move):
	#making a move on the board = display the letter
	board[letters] = move

def winning(board, letter):
	#check the board and letters
	
	return ((board[7] == letter and board[8] == letter and board[9] == letter) or
		(board[4] == letter and board[5] == letter and board[6] == letter) or
		(board[1] == letter and board[2] == letter and board[3] == letter) or
		(board[7] == letter and board[4] == letter and board[1] == letter) or
		(board[8] == letter and board[5] == letter and board[2] == letter) or
		(board[9] == letter and board[6] == letter and board[3] == letter) or
		(board[1] == letter and board[5] == letter and board[9] == letter) or
		(board[7] == letter and board[5] == letter and board[3] == letter))

def copy_ofthe_board(board):
	#make a copy of the board list and return it.
	boardCopy = []
	for i in board:
		boardCopy.append(i)
	return boardCopy

def is_space_free(board, move):
	"""return True if space is free"""
	return board[move] == ''

def Get_players_move(board):
	move = ''
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
		print("what is your next move? (1-9)")
		move = input()
	return int(move)
	
def chooseRandomMove(board, moveList):
	anyMove = []
	for i in moveList:
		if is_space_free(board, i):
			anyMove.append(i)

	if len(anyMove) != 0:
		return random.choice(anyMove)
	else:
		return None

def computer_move(board, computerLetter):
	if computerLetter == 'X':
		playerLetter == 'O'
	else:
		playerLetter == 'X'
	#the IQ of our game
	
	for i in range(1, 10):
		boardCopy = copy_ofthe_board(board)
		if is_space_free(boardCopy, i):
			make_move(boardCopy, computerLetter, i)
			if is_winner(boardCopy, computerLetter):
				return i
	for i in range(1, 10):
		boardCopy = copy_ofthe_board(board)
		if is_space_free(boardCopy, i):
			make_move(boardCopy, playerLetter, i)
			if is_winner(boardCopy, playerLetter):
				return i


	move = chooseRandomMove(board, [1, 3, 7, 9])
	if move != None:
		return move

	if is_space_free(board, 5):
		return 5

	return chooseRandomMove(board, [2, 4, 6, 8])

def is_board_full(board):
	for i in range (1, 10):
		if is_space_free(board, i):
			return False
	return True	

print("WELCOME TO OLD DRAFT")

while True:
	#reset the board 						
	board_draw = [' ']*10
	playerLetter, computerLetter = input_letters() 
	turn = who_play_first()
	print("The " + turn + " will go first.")
	gameisplaying = True

	while True:
		if turn == "player":
			draw(board_draw)
			move = Get_players_move(board_draw)
			make_move(board_draw, playerLetter, move)

			if winning(board_draw, playerLetter):
				draw(board_draw)	 
				print("Hooray! you won ")
				gameisplaying = False
				exit()
			else:
				if is_board_full(board_draw):
					draw(board_draw)

					print("The game is a tie!")
					break
				else:
					turn = 'computer'

		else:
			
			move = computer_move(board_draw, computerLetter)
			make_move(board_draw, computerLetter, move)

			if winning(board_draw, computerLetter):
				draw(board_draw)
				print("The computer has beaten you! You lose.")
				gameIsPlaying = False
				

			else:
				if is_Board_Full(board_draw):
					draw(board_draw)
					print("The game is a tie!")
					break
				else:
					turn = "player"

	print("Do you want to play again? (yes/no)")
	if not input().lower().startswith("y"):
		break									












	
