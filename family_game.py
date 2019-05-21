from sys import stdout, exit
from colorama import init, AnsiToWin32, Fore

init(wrap=False)
stream=AnsiToWin32(stdout).stream

print(Fore.MAGENTA, file=stream)
print("There are three families.")
print("Family_1.")
print("Family_2.")
print("Family_3.")
print("Good luck!")

def family_1():
    print("The family is very rich.")
    print("it's said to own a very big factory in America.")
    print("The family is entitled to be very mean people in the city.")
    print("It's a home to very beautiful girls.")
    print("It's a home to many legendary leaders.")
    print("Do you:\n\tTake the big factory.\n\tMarry the beautiful girls.\n\tTake the factory leadership.\n\tstop them from being mean.")


    choice_1 = input("==>")

    if choice_1=="Take the big factory":
        over("The family does not agree and seed an assassin to kill you.")
        exit()

    elif choice_1=="Marry the beautiful girls.":
    	print()
    	family_2()

    elif choice_1 =="Take the factory leadership.":
    	print()
    	over("Sorry the factory is under very good leadership.")
    	exit()
    elif choice_1 == "stop them from being mean.":
    	print()
    	family_3()

    else:
    	print("GAME OVER ! Hey, you can always try next time.")


def family_2():
	print("The family is known for having great people.")
	print("People say that the family is an immigrant.")
	print("The family has very bright people in terms of business.")
	print("Fortunitly the family has only one girl.")
	print("Do you:\n\tAsk them for the big plane.\n\tAsk if they are immigrant.\n\tAsk for business ideas.\n\tmarry the only girl in the family.")


	choice_2=input("=>>")

	if choice_2 == "marry the only girl in the family.":
		print()
		print("Are you ready to die for her.(Yes/no).")
		ans = input("=>")
		if ans == "Yes":
			print()
			print("To marry her you must choose :\n\tPropose to her.\n\tTake her to the places she enjoys must.\n\tForce her to marriage.\n\tAsk the family for a hand in marriage.")
			choice_3 = input("=+>")

			if choice_3 == "Propose to her.":
				print()
				over("She rejects the proposal.")
				exit()
			elif choice_3 == "Take her to the places she enjoys must.":
				print()
				print("She enjoys doing two things (1~2)")
				print(" choose between 1 or 2 ")
			
				quiz = ["Provided by nature but destroyed by evolution",
						"It's a picking game with no roles but just your ability."]
				num = input("=>")
				
				if num == "1":
					print(quiz[0])
					print("hint: visible everywhere.")
					ans = input("==>")
					print()
					if ans == "nature work" or num == "nature":
						print("She falls in love with youand agree to marry you.")
					elif ans != "nature work " or num == "nature":
						print("That is not correct you can think and try later.")
						exit()
					else:
						print()
						over("GAME OVER!!! YOU CAN TRY AGAIN.")

				if num == "2":
					print()
					print(quiz[1])
					ans = input("==>")

					if ans == "shopping":
						print("she gives you all he heart and love you so much.")
					elif ans != "shopping":
						print("That is a good gess but not correct ")
					else:
						over("GAME OVER!!")
						exit() 		


			elif choice_3 == "Force her to marriage":
				print()
				family_3()

			elif choice_3 == " Ask the family for a hand in marriage.":
				over("The family does not take part in love decissions.")
				exit()
			else:
				print("GAME OVER!!!!")

		elif ans == "no":
			print("You have to love her first.")
			print()
			family_3()
		else:
			print()
			print("GAME OVER !! Follow the rule of the game.")
			exit()

	elif choice_2 == "Ask for the big plan.":
		print()
		over("The family does not tell you their plane it's a secret.")
		exit()

	elif choice_2 == "Ask if they are immigrant.":
		print()
		family_1()
	elif choice_2 == "Ask for business ideas.":
		print()
		over("The family does not give any business ideas")
		exit()
	else:
		print("GAME OVER!! Hey you can always try next time.")
		exit()

def family_3():
	print("The family is a street Family.")					
	print("The family is known to produce many street children.")
	print("same of the children are adopted.")
	print("Most of the beggers in the city are from this family.")
	print("Not much is known about the family.")
	print("They all keep on looking for temporry jobs in the city.")
	print("Do you:\n\tSearch for the family street children.\n\tAdopt same of the children.\n\tFeed the beggers of the family.\n\tGive the family a job.")

	choice_4 = input("=>>")

	if choice_4 == "Search for the family street children.":
		print()
		print("it's long since the family saw same of it's children where do you think their children are.")
		ans = input("=>>")

		if ans == "street":
			print()
			print("That is a good idea, but when we went to look for them we did not find them please give another idae.")
			another = input("+>>")
			if another =="adopted home":
				print()
				family_2()
			else:
				over("GAME OVER!!")
				exit()
		elif ans =="adopted home":
			print()
			family_2()

		elif ans != "street":
			print()
			print("Good try but not correct.")
			over("GAME OVER!! That is not correct")
			exit()

		else:
			over("You can always try next time.")
			exit()

	elif choice_4 == "adopt Adopt same of the children.":
		print()
		family_1()

	elif choice_4 == "Feed the beggers of the family.":
		print("The family gives two quesions before feeding them.")
		print("Choose either question 1 or 2 .")

		question = ["What can you hold in your right hand but can't hold in your left hand.",
					"It's so cloudy, i am pointing with my finger up in the sky, what am i pointing."]

		choice_5 = input("\t==>")

		if choice_5 == "1":
			print(question[0])
			print()
			print("Hint: it's always with you.")
			answ = input("=>")

			if  answ == "right hand":
				print()
				print("Has anyone ever told you that you are the most intellegent person this planet has ever seen.")
				exit()
		
			elif answ != "right hand":
				print()
				over("Wrong answer thing and try again later.")
				exit()
			
			else:
				over("GAME OVER!!")
				exit()

		elif choice_5 == "2":
			print(question[1])
			print()
			print("Hint: That is a very easy question, it does not need a hint.")
			answer = input("==>")
			print()

			if answer == "finger":
				print()
				print("You became the most intelligent person the world has ever seen.")
				exit()

			elif answer != "finger":
				print()
				print("Wrong answer, think and try again.")
				exit()
			else:
				over("GAME OVER!!")
				exit()
				
		else:
			print()
			over("Game over!!.")
			exit()

	elif choice_4 == "Give the family a job.":
		print()
		family_1()

	else:
		print()
		over("GAME OVER!!!")
		exit()
def over(reason):
	print(reason, "hope you enjoyed")		

def families():
	print()
	print("You were asked to investigate the lifestyle of families.")
	print("You were told to choose amang three families \n\t1, \n\t2, \n\t3.")

	choice = input("=>>")

	if choice == "1":
		family_1()

	elif choice == "2":
		family_2()

	elif choice == "3":
		family_3()

families()

			

								

