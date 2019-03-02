import random
HANGMAN_PICS =['''
	+---+
	    |
	    |
	    |
	   === ''', '''
	+---+
	o   |
	    |
	    |
	   === ''', '''
	+---+
	o   |
	|   |
	    |
	   === ''', '''
	+---+
	o   |
   /|   |
	    |
	   === ''', '''	
	+---+
	o   |
   /|\  |
	    |
	   === ''', '''
	+---+
	o   |
   /|\  |
   /    |
	   === ''', '''
	+---+
	o   |
   /|\  |
   / \  |
	   === ''']

words = {'animals': """ant baboon badger bat bear beaver camel cat clam cobra cougar
		coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
		lion lizard llama mole monkey moose mouse mule newt otter olw panda
		parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
		skunk sloth snake spider stork swan tiger toad trout turky turtle
		weasel whale wolf wombat zebra""".split(),
		'colors': 'red orange yellow green blue indigo violet white black brown'.split(),
		'shapes': """square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon
		hexagon septagon octagon""".split(),
		'fruits': '''apple orange lemon lime pear watermelon grape grapefruit cherry banana
		cantaloupe mango strawberry tomato'''.split(),} 

def getRandomWord(word_dict):
	# this function returns a random string from the passed lst of
	word_key = random.choice(list(word_dict.keys()))
	#second, randomly select a word from the key's list in the dictionary:

	word_index = random.randint(0, len(word_dict[word_key]) -1)
	return [word_dict[word_key][wordindex], word_key]

def displayBoard(missedletters, correctletters, secretword):
	print(HANGMAN_PICS[len(missedletters)])
	print()
	
	print('missed letters:', end=' ')
	for letter in missedletters:
		print(letter, end=' ')
	print()
	
	blanks = '-'* len(secretword)

	for i in range(len(secretword)): #Replace blank with correctly
	  
		if secretword[i] in correctletters:
			blank = blanks[:i] +  secretword[i] + blank[i+1:]
	for letter in blanks:#show the secret word with spaces in between
	   
		print(letter, end=' ')
	print()

def getGuess(alreadyGuessed):
	"""Returns the letter the player entered. This function makes sure the
	  player entered a single letter and not something else."""
	while True:
		print('Guess a letter.')
		guess = input()
		guess = guess.lower()
		if len(guess) !=1:
			print('please enter a single letter.')
		elif guess in alreadyGuessed:
			print('You have already guessed that letter. Choose again.')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('please enter a LETTER.')
		else:
			return guess

def playAgain():
	'''this function returns True if the player wants to play again;
	  outherwise, it returns False'''
	print('Do you want to play again? (yes/no)')
	if input().lower().startswith('y'):
		return True
	else:
		return False	

print('H A N G M A N')

difficulty = ''
while difficulty not in list('EHM'):
	print('Enter difficulty : E -Easy, M - Medium, H-Hard')
	difficulty = input().upper()

if difficulty == 'M':
	del HANGMAN_PICS[8:9]
if difficulty == 'H':
	del HANGMAN_PICS[3:9]

missedletters = ''
correctletters = ''
secret_set = getRandomWord(words)
gameIsDone = False

while True:
	print('The secret word is in the set:' + secret_set)
	displayBoard(missedletters, correctletters, secretword)

	# let the player enter a letter.
	guess = getGuess(missedletters + correctletters)

	if guess in secretword:
		correctletters += guess

		#check if the player entered a letter.
		foundALLletters = True
		for i in range(len(secretword)):
			if secretword[i] not in correctletters:
				foundALLletters = False
				break
		if foundALLletters:
			print('Yes! the secret word is "' + secretword + '"! You have won!')
			gameIsDone = True
	else:
		missedletters = missedletters + guess

		# Check if the player has guessed too many times and lost.
		if len(missedletters) == len(HANGMAN_PICS) - 1:
			displayBoard(missedletters, correctletters, secretword)
			print('you have run out of guesses!|\nAfter ' +
				str(len(missedletters)) + ' missed guesses and ' +
				str(len( correctletters)) + ' correct guesses, the word was "' +  
				secretword  + '"')
			gameIsDone = True
	#Ask the player if they want to play aoter round
	if gameIsDone:
	 	if playAgain():
	 		missedletter = ''
	 		correctletters = ''
	 		gameIsDone = False
	 		secretword, secret_set = getRandomWord(words)
	 	else:
	 		break




