
import random


def blackjack():
	black_jack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
	card_type = ['of spades', ' of diamonds', ' of hearts', ' of clubs']
	specialTen_cards = ["Jack", "King", "Queen"]
	House_favor = [1,2,3,3,4,5,6,7,8,9,10]
	User_favor = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
	#bet = bet_ammount#<------- if statement where difficulty changes if bet is greater than 1000
	#Draw CPU 1st card. Don't show
	CPU_1stCard = random.choice(black_jack)
	CPU_1stCard_type = random.choice(card_type)


	print "| Dealer: Face down card"

	#Draw CPU 2nd card & show
	CPU_2ndCard = random.choice(black_jack)
	CPU_2ndCard_type = random.choice(card_type)

	if CPU_2ndCard == 10:
		Rand_TenCard = random.choice(specialTen_cards)
		print "| Dealer Draws: ", Rand_TenCard, CPU_2ndCard_type
	elif CPU_2ndCard == 1:
		print "| Dealer Draws: Ace", CPU_2ndCard_type
	else:
		print "| Dealer Draws: ", CPU_2ndCard, CPU_2ndCard_type
	
	print "-------------------------------"	




	#Draw user first card and show

	USR_1stCard = random.choice(black_jack)
	USR_1stCard_type = random.choice(card_type)


	if USR_1stCard == 1:
		print "Your 1st card: Ace", USR_1stCard_type
	elif USR_1stCard == 10:
		Rand_TenCard = random.choice(specialTen_cards)
		print "Your 1st Card: ", Rand_TenCard, USR_1stCard_type
	elif USR_1stCard == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
		print "Your 1st Card: ", USR_1stCard, USR_1stCard_type





	#Draw user 2nd card & show
	USR_2ndCard = random.choice(black_jack)
	USR_2ndCard_type = random.choice(card_type)

	if USR_2ndCard == 1:
		print "Your 2nd card: Ace", USR_2ndCard_type
	elif USR_2ndCard == 10:
		Rand_TenCard = random.choice(specialTen_cards)
		print "Your 2nd Card: ", Rand_TenCard, USR_2ndCard_type
	elif USR_2ndCard == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
		print "Your 2nd Card: ", USR_2ndCard, USR_2ndCard_type



	CPU_totalCard_value = CPU_1stCard + CPU_2ndCard
	USR_totalCard_value = USR_1stCard + USR_2ndCard
	Ace_Total = USR_totalCard_value + 10
	

	
	if USR_1stCard == 1 or USR_2ndCard == 1:
		if Ace_Total == 21:
			print "Blackjack! You Win!!!"
			return 1
		print USR_totalCard_value, "or", Ace_Total
	else:
		print USR_totalCard_value



	#Give user the choice to Hit or Stay. Code block draws new card from deck and adds value to total
	while USR_totalCard_value < 21:
		usr_choice1 = int(input("Enter 1 to Hit or 2 Stand: "))
		
	#If user chooses to stand, display final card value and break out of loop.
		if usr_choice1 == 2 and Ace_Total < 21 and (USR_1stCard == 1 or USR_2ndCard == 1):
			USR_finalCard_value = Ace_Total
			break
		elif usr_choice1 == 2 and Ace_Total > 21 and (USR_1stCard == 1 or USR_2ndCard == 1):
			USR_finalCard_value = USR_totalCard_value
			break
		elif usr_choice1 == 2:
			USR_finalCard_value = USR_totalCard_value
			break
	#If user chooses to hit, assign a 3rd card, and add it's value to the total card value.
		if usr_choice1 == 1 and USR_totalCard_value < 17:
			USR_3rdCard = random.choice(black_jack)
			USR_3rdCard_type = random.choice(card_type)
			
			if USR_3rdCard == 1:
				print "Your card: Ace", USR_3rdCard_type
				USR_totalCard_value += USR_3rdCard
				Ace_Total += USR_3rdCard
				if Ace_Total == 21 and USR_1stCard == 1 or USR_2ndCard == 1:
					print "You win!!!!"
					return 1
				elif Ace_Total < 21 and USR_1stCard == 1 or USR_2ndCard == 1:
					print USR_totalCard_value, "or", Ace_Total	
				else:
					print "Total card value: ", USR_totalCard_value
			elif USR_3rdCard == 10:
				Rand_TenCard = random.choice(specialTen_cards)
				print "Your Card: ", Rand_TenCard, USR_3rdCard_type
				USR_totalCard_value += USR_3rdCard
				print USR_totalCard_value
			else:
				print "Your Card: ", USR_3rdCard, USR_3rdCard_type
				USR_totalCard_value += USR_3rdCard
				Ace_Total += USR_3rdCard
				if Ace_Total == 21 and USR_1stCard == 1 or USR_2ndCard == 1:
					print "You win!!!!"
					return 1
				elif Ace_Total < 21 and USR_1stCard == 1 or USR_2ndCard == 1:
					print USR_totalCard_value, "or", Ace_Total	
				else:
					print "Total card value: ", USR_totalCard_value				
			if USR_totalCard_value > 21:
				print "You Bust!"
				print "Your card total: ", USR_totalCard_value
				print "Dealer's card total: ", CPU_totalCard_value
				print "----------------------------------------------------------"
				return 0
			elif USR_totalCard_value == 21:
				print "You win!!!!"
				print "Your card total: ", USR_totalCard_value
				print "Dealer's card total: ", CPU_totalCard_value
				print "----------------------------------------------------------"
				return 1
	#Below elif statement makes game a little easier for user by decreasing odds of drawing a 10. Remove or comment to increase difficulty.
	#Programmer can also adjust difficulty by manipulating values in the User_favor list
		elif usr_choice1 == 1 and USR_totalCard_value >= 17:
			USR_3rdCard = random.choice(User_favor)
			USR_3rdCard_type = random.choice(card_type)
			if USR_3rdCard == 1:
				print "Your card: Ace", USR_3rdCard_type
				USR_totalCard_value += USR_3rdCard
				print "Total card value: ", USR_totalCard_value
			elif USR_3rdCard == 10:
				Rand_TenCard = random.choice(specialTen_cards)
				print "Your Card: ", Rand_TenCard, USR_3rdCard_type
				USR_totalCard_value += USR_3rdCard
				print USR_totalCard_value
			else:
				print "Your Card: ", USR_3rdCard, USR_3rdCard_type
				USR_totalCard_value += USR_3rdCard
				print USR_totalCard_value
	#Test to see if user busts, or draws 21
			if USR_totalCard_value > 21:
				print "You Bust!"
				print "Your card total: ", USR_totalCard_value
				print "Dealer's card total: ", CPU_totalCard_value
				print "----------------------------------------------------------"
				return 0
			elif USR_totalCard_value == 21:
				print "You win!!!!"
				print "Your card total: ", USR_totalCard_value
				print "Dealer's card total: ", CPU_totalCard_value
				print "----------------------------------------------------------"
				return 1
		
	print "----------------------------------------------------------"
	
	

#CPU auto play

	#CPU decision to hit or stay
	
	if CPU_1stCard == 10:
		Rand_TenCard = random.choice(specialTen_cards)
		print "Dealer's face down card: ", Rand_TenCard, CPU_1stCard_type
	else:
		print "Dealer's face down card: ", CPU_1stCard, CPU_1stCard_type
	
	if CPU_totalCard_value == 21:
		print "----------------------------------------------------------"
		print "Blackjack for Dealer! You lose!"
		print "Your card total: ", USR_finalCard_value
		print "Dealer's card total: ", CPU_totalCard_value
		print "----------------------------------------------------------"		
	while CPU_totalCard_value < 21:
		#CPU checks user total and chooses to stay if it's total card value is greater than the user's final card value at any point in the game.
		if CPU_totalCard_value > USR_finalCard_value:
			print "Dealer chooses to stay"
			CPU_finalCard_value = CPU_totalCard_value
			break
		elif CPU_totalCard_value >= 18:
			print "Dealer chooses to stay"
			CPU_finalCard_value = CPU_totalCard_value
			break
		#Additional elif statement to increase House's chance of winning
		#Line 112 will be changed to if CPU_totvalue >= 18:
		#Additional elif condition will be if CPU_totvalue >= 15 and CPU_totvalue < 18:
		#New list will be created containing these values House_favor = [1,2,2,3,3,4,5,6,7,8,9,10]
		#print "Dealer hits!"
			# CPU_3rdCard = random.choice(House_favor)
			# CPU_3rdCard_type = random.choice(card_type)
		elif CPU_totalCard_value >= 15 and CPU_totalCard_value < 18:
			print "Dealer hits!"
			CPU_3rdCard = random.choice(House_favor)
			CPU_3rdCard_type = random.choice(card_type)
			if CPU_3rdCard == 10:
				Rand_TenCard = random.choice(specialTen_cards)
				print "Dealer draws: ", Rand_TenCard, CPU_3rdCard_type
				CPU_totalCard_value += CPU_3rdCard
			elif CPU_3rdCard == 1:
				print "Dealer draws: Ace", CPU_3rdCard_type
				CPU_totalCard_value += CPU_3rdCard
			else:
				print "Dealer draws: ", CPU_3rdCard, CPU_3rdCard_type
				CPU_totalCard_value += CPU_3rdCard
			if CPU_totalCard_value > 21:
				
				print "----------------------------------------------------------"
				print "Dealer busts! You win"
				if Ace_Total > USR_totalCard_value and Ace_Total < 21:
					print "Your card total: ", Ace_Total
				else:
					print "Your card total: ", USR_finalCard_value
				print "Dealer's card total: ", CPU_totalCard_value
				print "----------------------------------------------------------"
				
				return 1
			elif CPU_totalCard_value == 21:
				
				print "----------------------------------------------------------"
				print "You lose!"
				if Ace_Total > USR_totalCard_value and Ace_Total < 21:
					print "Your card total: ", Ace_Total
				else:
					print "Your card total: ", USR_finalCard_value
				print "Dealer's card total: ", CPU_totalCard_value
				print "----------------------------------------------------------"
				return 0
#Above elif condition causes a harder version of the game. If lines 124 to 156 are commented or removed, game will be easier
#Programmer can also adjust difficulty by manipulating values in the House_favor list
		elif CPU_totalCard_value < 17:
			print "Dealer hits!"
			CPU_3rdCard = random.choice(black_jack)
			CPU_3rdCard_type = random.choice(card_type)
			CPU_totalCard_value += CPU_3rdCard
			if CPU_3rdCard == 10:
				Rand_TenCard = random.choice(specialTen_cards)
				print "Dealer draws: ", Rand_TenCard, CPU_3rdCard_type
				
			elif CPU_3rdCard == 1:
				print "Dealer draws: Ace", CPU_3rdCard_type
				
			else:
				print "Dealer draws: ", CPU_3rdCard, CPU_3rdCard_type
				
			if CPU_totalCard_value > 21:
				print "----------------------------------------------------------"
				print "Dealer busts! You win"
				print "Your card total: ", USR_totalCard_value
				print "Dealer's card total: ", CPU_totalCard_value
				print "----------------------------------------------------------"
				return 1
			elif CPU_totalCard_value == 21:
				print "----------------------------------------------------------"
				print "You lose!"
				print "Your card total: ", USR_totalCard_value
				print "Dealer's card total: ", CPU_totalCard_value
				print "----------------------------------------------------------"
				return 0
				
	
	
	if USR_finalCard_value == CPU_totalCard_value:
		print "----------------------------------------------------------"
		print "It's a tie"
		print "Your card total: ", USR_finalCard_value
		print "Dealer's card total: ", CPU_totalCard_value
		print "----------------------------------------------------------"
		return 2
	elif USR_finalCard_value > CPU_totalCard_value:
		print "----------------------------------------------------------"
		print "You win!"
		print "Your card total: ", USR_finalCard_value
		print "Dealer's card total: ", CPU_totalCard_value
		print "----------------------------------------------------------"		
		return 1
	elif USR_finalCard_value < CPU_totalCard_value:
		print "----------------------------------------------------------"
		print "You lose!"
		print "Your card total: ", USR_finalCard_value
		print "Dealer's card total: ", CPU_totalCard_value
		print "----------------------------------------------------------"		
		return 0
	
	

if __name__ == "__main__":

	blackjack()
















