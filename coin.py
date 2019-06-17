import random
import time
from colorama import Fore

def displayThis():
	print(Fore.LIGHTRED_EX + """  you are in a Casino with your friends playing Toss the Coin.
		you are all enjoying playing and now it is your turn. \n\n\n""")

def chooseside():
	ans = ''
	while ans != 'head' and ans != 'tail' :
		print(Fore.MAGENTA + "In a coin their is only a head and a tail. After the coin is tossed, which side do you think it will land (head or tail)")
		ans  = input(Fore.RED + '=>> ')

	return ans

def TossCoin(anyside):
	print(Fore.LIGHTGREEN_EX + 'The coin has just been tossed and is moving up rotating at a very high speed......')
	time.sleep(3)
	print(Fore.GREEN+ '\nThe coin now moving down and is reducing its rotating speed,,,,,,,,')
	time.sleep(4)
	print(Fore.RED + "\nThe coin is now rotating on the table at a low speed,,,,,,")
	time.sleep(4)

	CoinHead = str(random.randint(1, 2))

	if anyside == CoinHead:
		print(Fore.BLUE + '\n\tIt\'s your lucky day ! You got it correct!')
	else:
		print(Fore.BLUE + '\n\tyou are not lucky this time. please try again')

PlayAgain = 'yes'
while PlayAgain == 'yes' or PlayAgain == 'y':
	displayThis()
	head_and_tail = chooseside()
	TossCoin(head_and_tail)

	print(Fore.RED + "do you want to play again? (yes or no)")
	PlayAgain = input('->> ')						


