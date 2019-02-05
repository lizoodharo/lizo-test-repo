#Guess the number game
import random

def guess_num(min, max):
	random_num = random.randint(min, max)
	
	tries = 1
	usr_guess = int(input("Guess the number: "))
	while usr_guess != random_num:
		if usr_guess < random_num:
			print("Too low! Try again")
		elif usr_guess > random_num:
			print("Too high! Try again")
		usr_guess = int(input("Guess the number: "))
		tries += 1
	print(random_num, " was the correct number! You guessed it in ", tries, " tries!")
	
if __name__ == "__main__":
	print("Guess a number between,")
	min = int(input("Lower bound: "))
	print("and")
	max = int(input("Upper bound: "))
	guess_num(min, max)