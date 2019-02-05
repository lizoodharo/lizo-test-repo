#RPS file
# Rock paper scissors game


#import the random library
import random




	
def rock_paper_scissors(games, usr_choice):
	#assign random number between 1 and 3 inclusive to represent rock, paper, and scissors respectively
	random_num = random.randint(1,3)


	# Rock = 1
	# Paper = 2
	# Scissors = 3
	


	#initialize counters to zero to tally up the wins, losses, and ties
	wins = 0
	loss = 0
	ties = 0
	#range must be games-1 because index starts at 0. So if user enters 5, range will iterate 0,1,2,3,4,5
	for i in range(games-1):
		
		if usr_choice == 'Rock' or usr_choice == 'rock' and random_num == 1:
			print('CPU chose Rock')
			print("It's a tie")
			ties += 1
		elif usr_choice == 'Rock' or usr_choice == 'rock' and random_num == 2:
			print('CPU chose paper')
			print("You lose")
			loss += 1
			
		elif usr_choice == 'Rock' or usr_choice == 'rock' and random_num == 3:
			print('CPU chose Scissors')
			print("You win!")
			wins += 1

		if usr_choice == 'Paper' or usr_choice == 'paper' and random_num == 1:
			print('CPU chose Rock')
			print("You Win")
			wins += 1
		elif usr_choice == 'Paper' or usr_choice == 'paper' and random_num == 2:
			print('CPU chose Paper')
			print("Its a tie")
			ties += 1
		elif usr_choice == 'Paper' or usr_choice == 'paper' and random_num == 3:
			print('CPU chose Scissors')
			print("You lose!")
			loss += 1

		if usr_choice == 'Scissors' or usr_choice == 'scissors' and random_num == 1:
			print('CPU chose Rock')
			print("You Lose")
			loss += 1
		elif usr_choice == 'Scissors' or usr_choice == 'scissors' and random_num == 2:
			print('CPU chose Paper')
			print("You Win")
			wins += 1
		elif usr_choice == 'Scissors' or usr_choice == 'scissors' and random_num == 3:
			print('CPU chose Scissors')
			print("Its a tie!")
			ties += 1
		usr_choice = str(input("Rock, Paper, or Scissors: "))
		random_num = random.randint(1,3)

	if wins > loss:
		print "You won the best of ", games
		print "Wins: " , wins
		print "Losses: ", loss
		print "Ties: ", ties
	elif wins < loss:
		print "You lost the best of", games
		print "Wins: " , wins
		print "Losses: ", loss
		print "Ties: ", ties
	else:
		print "You tied the best of ", games
		print "Wins: " , wins
		print "Losses: ", loss
		print "Ties: ", ties
		
#If this module is being run, execute the following block of code.
if __name__ == "__main__":
	#prompt user to input the number of games they like to play using the int() function to return an integer
	games = int(input("How many games would you like to play? "))
	#prompt user to input rock paper or scissors.
	usr_choice = str(input("Rock, Paper, or Scissors: "))
	rock_paper_scissors(games, usr_choice)