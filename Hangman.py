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
       === ''', '''
    +---+   ]
   [o]  |
   /|\  |
   / \  |
       ===''']
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

def get_random_word(word_dict):
    word_key = random.choice(list(word_dict.keys()))
    word_index = random.randint(0, len(word_dict[word_key]) - 1)
    return [word_dict[word_key][word_index], word_key]

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '-' * len(secret_word) 

    for i in range(len(secret_word)):
         if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letters in blanks:
        print(letters, end=' ')

    print()
    
def get_guess(already_guessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed thet letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER')
        else:
            return guess

def play_again():
    print("Do you want to play again? (yes/no)")
    if input().lower().startswith('y'):
        return True
    else:
        return False

print("H A N G M A N")

difficulty = ''
while difficulty not in list('EHM'):
    print('Enter difficulty: E - Easy, m-medium, H-Hard')
    difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8:9]
if difficulty =='H':
    del HANGMAN_PICS[3:9]

missed_letters = ''
correct_letters = ''
secret_word, secret_set = get_random_word(words)
game_is_done = False

while True:
    print('The secret word is in the set: ' + secret_set)
    display_board(missed_letters, correct_letters, secret_word)

    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters += guess
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print('Yes! the secret word is "' + secret_word + '"! You have won!')
            game_is_done = True
    else:
        missed_letters = missed_letters + guess

        if len(missed_letters) == len(HANGMAN_PICS) -1:
            display_board(missed_letters, correct_letters, secret_word)                 
            print('You have run out of guesses!\nAfter ' +
                  str(len(missed_letters)) + ' missed guesses and ' +
                  str(len(correct_letters)) + ' correct guesses, the word was "' +
                  secret_word + '"')
            game_is_done = True 
    if game_is_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word, secret_set = get_random_word(words)
        else:
            break




