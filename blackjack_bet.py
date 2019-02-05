import blackjack_function

usr_bank = 1000.00
print "Current bank: $1000.00"

cash_out = 1

while cash_out >= 1:
	bet_amount = float(input("Place your bet. (Minimum bet amount is $0.01): $"))

	while bet_amount > usr_bank or bet_amount < 0.01:
		bet_amount = float(input("Invalid amount. Please re-enter your bet: $"))

	usr_bank -= bet_amount

	game_result = blackjack_function.blackjack()

	if game_result == 0:
		print "Current bank: $", "%.2f" % usr_bank
	elif game_result == 1:
		usr_bank += bet_amount*2
		print "Current bank: $", "%.2f" % usr_bank
	elif game_result == 2:
		usr_bank += bet_amount
		print "Current bank: $", "%.2f" % usr_bank
	
	if usr_bank < 0.01:
		print "Sorry! You have no money left!"
		exit()
	cash_out = float(input("Enter any number to continue, or 0 to cash out:"))

		
	
	

print "Your winnings: $", "%.2f" % usr_bank