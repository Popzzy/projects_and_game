import random
from colorama import Fore
my_hangman_pics = ["""
    +----+
         |
         |
         |
        ===""", """
    +----+
    0    |
         |
         |
        ===""", """
    +----+
    0    |
    |    |
         |
        ===""", """
    +----+
    0    |
   /|    |
         |
        ===""","""
    +----+
    0    |
   /|\   |
         |
        ===""","""
    +----+
    0    |
   /|\   |
   /     |
        ===""","""
    +----+
    0    |
   /|\   |
   / \   |
        ===""","""
    +----+
   [0    |
   /|\   |
   / \   |
        ===""","""
    +----+
   [0]   |
   /|\   |
   / \   |
        ==="""]


words = {'animals': """ant baboon badger bat bear beaver camel cat clam cobra cougar coyote          
        crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama          
        mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram          
        rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad          
        trout turkey turtle weasel whale wolf wombat zebra""".split(),          
        'colors': 'red orange yellow green blue indigo violet white black brown'.split(),          
        'shapes': '''square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon          
        hexagon septagon octagon'''.split(),          
        'fruits': '''apple orange lemon lime pear watermelon grape grapefruit cherry banana          
        cantaloupe mango strawberry tomato'''.split(), }

def random_word(word_dict):
	word_key = random.choice(list(words.keys()))
	word_index = random.randint(0, len(words[word_key])-1)
	all_word = [words[word_key][word_index], word_key]
	return all_word

def display_board(missed_letters, correct_letters, secret_word):
	print(Fore.MAGENTA + my_hangman_pics[len(missed_letters)])	
	print(Fore.MAGENTA + "MISSED LETTERS: ", end = ' ')
	for i in range(len(missed_letters)):
		print(Fore.LIGHTYELLOW_EX + missed_letters[i], end=' ')
	print()

	pop = len(secret_word)
	blank = '-'*pop
	for i in range(pop):
		if secret_word[i] in correct_letters:
			blank = blank[:i] + secret_word[i] + blank[i + 1: ]

	for letter in blank:
		print(Fore.LIGHTRED_EX + letter, end=' ')
	print()

def get_guess(already_guess):
	guess = input(Fore.BLUE + "Guess a letter: ")
	if len(guess) <= 0:
		print(Fore.PINK + "Please enter a letter. ")
	elif guess in already_guess:
		print(Fore.RED + "Already guessed.")
	elif len(guess) > 1:
		print(Fore.RED + "Enter a single letter.")		
	elif guess not in 'abcdefghijklmnopqrstuvwxyz':
		print(Fore.RED + "Invalid character!")
	else:
		return guess

def play_again():
	player = input(Fore.CYAN + "Do you want to play again")
	if player.lower().startswith("y"):
		return True
	else:
		return False

print(Fore.RED + "H A N G M A N")
correct_letters = ' '
missed_letters = ' '
all_sets = random_word(words)
secret_word, current_set = all_sets

while True:
	display_board(missed_letters, correct_letters, secret_word)
	print(Fore.LIGHTRED_EX + "The secret word is in the set: {0}".format(current_set))
	guess = get_guess(correct_letters + missed_letters)
	game_over = True

	if guess:
		if guess in secret_word:
			correct_letters += guess
			for i in secret_word:
				if not i in correct_letters:
					game_over = False
			if game_over:
				print(Fore.GREEN + "You've Won! The word was: {winners}".format(winners = secret_word))

		else:
			missed_letters += guess

			if len(missed_letters) != len(my_hangman_pics) -1:
				game_over = False
			else:
				display_board(missed_letters, correct_letters, secret_word)
				print(Fore.CYAN + "You have run out of guesses!\nAfter " +
	              str(len(missed_letters)) + ' missed guesses and ' +
	              str(len(correct_letters)) + ' correct guesses, the word was "' +
	              secret_word + '"')
	else:
		game_over = False
    	
	if game_over:
		if play_again():
			correct_letters = ''
			missed_letters = ''
			secret_word, current_set = random_word(words)
		else:
			break			



		
	



