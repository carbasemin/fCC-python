class Category:
	
	def __init__(self, name: str):
		self.name = name
		self.ledger = list()

	def __str__(self):
		len_name = len(self.name)

		if len_name % 2 == 0:
			title = "*"*round((30-len_name)/2) + self.name + "*"*round((30-len_name)/2)
		else:
			# It can't be centered if it's a title that contains odd number of characters...
			title = "*"*round((30-len_name)/2) + self.name + "*"*round((30-len_name)/2 + 1)

		transactions_ = ""

		for transactions in self.ledger:
			# First 23 characters of the description.
			desc = transactions['description'][0:23]
			# Formatting the amount. Two decimals and 7 characters in total.
			amnt_float = float(transactions['amount'])
			formatted_amnt_float = "{:.2f}".format(amnt_float)
			amnt = str(formatted_amnt_float)[0:7]
			
			transactions_ += desc + " "*(30-len(desc)-len(amnt))  + amnt + "\n"

		# Balance
		values = [transactions['amount'] 
					for transactions in self.ledger]
	
		balance = sum(values)
		ttl = float(balance)
		formatted_ttl = "{:.2f}".format(ttl)
		total = str(formatted_ttl)
		transactions_ += f"Total: {total}"

		return title + "\n" + transactions_

	def get_balance(self):
		'''Returns the current balance of the budget category
		based on the deposits and withdrawals that have occurred.'''

		# Collects the values of all the transactions that had happen.
		values = [transactions['amount'] 
					for transactions in self.ledger]
		
		balance = sum(values)
		
		return balance

	# Might cause problems.
	def check_funds(self, amount: int) -> bool:
		'''It returns False if the amount is greater than the 
		balance of the budget category and returns True otherwise.'''

		if amount > self.get_balance():
			return False
		else:
			return True

	def deposit(self, amount: int, description: str="") -> None:
		'''This method accepts an amount and description.
		If no description is given, it defaults to an empty string. 
		The method appends an object to the ledger list in the form of:
		{"amount": amount, "description": description}.'''

		self.ledger.append({"amount": amount, "description": description})

	def withdraw(self, amount: int, description: str="") -> bool:
		'''The amount passed in is stored in the ledger as a negative number.
		If there are not enough funds, nothing is added to the ledger.
		This method returns True if the withdrawal took place, and False otherwise.'''

		if self.check_funds(amount):
			self.ledger.append({"amount": -amount, "description": description})
			return True
		else:
			return False


	def transfer(self, amount: int, category: object) -> bool:
		'''The method adds a withdrawal with the amount and the description 
		"Transfer to [Destination Budget Category]" to the ledger. 
		It then adds a deposit to the other budget category with the amount and 
		the description "Transfer from [Source Budget Category]".
		If there are not enough funds, nothing is added to either ledgers.
		This method returns True if the transfer took place, and False otherwise.'''

		if self.check_funds(amount):
			self.withdraw(amount, f"Transfer to {category.name}")
			category.deposit(amount, f"Transfer from {self.name}")	
			return True
		else:
			return False

def __withdrawals__(category: object) -> int:
	'''Returns the sum of withdrawals in a certain category as a list.'''

	# Gets the amount that is transacted in a list.
	values = [transactions['amount'] 
						for transactions in category.ledger]
	
	# Gets only the withdrawals.
	withdrawals = [amount for amount in values
							if amount < 0]

	return -sum(withdrawals)

def __withdrawal_percentages__(list_of_categories: list) -> list:
	'''Returns the percentage of withdrawals.'''

	from math import floor

	## Getting all the withdrawals.
	withdrawals_percentage = list()
	total_withdrawals = 0

	for category in list_of_categories:
		total_withdrawals += __withdrawals__(category)
	##

	# Percentages are rounded **down** to the nearest ten.
	for category in list_of_categories:
		percentage = floor((__withdrawals__(category)/total_withdrawals)*10)*10
		withdrawals_percentage.append((category.name, percentage))

	return withdrawals_percentage

def create_spend_chart(list_of_categories: list) -> str:
	'''This is just horrible. I won't even try to explain...'''

	percentage = "Percentage spent by category"

	percentages = __withdrawal_percentages__(list_of_categories)

	percentages_values = [category[1] for category in percentages]
	percentages_names = [category[0] for category in percentages]

	### Will be working on every line seperately. Ugly, ugly, ugly code.
	hundred_line = "100| "; ninty_line = " 90| "; eighty_line = " 80| "
	seventy_line = " 70| "; sixty_line = " 60| "; fifty_line = " 50| "
	fourty_line = " 40| "; thirty_line = " 30| "; twenty_line = " 20| "
	ten_line = " 10| "; zero_line = "  0| "

	for i in range(len(percentages)):
		
		if percentages_values[i] == 100:
			hundred_line += "o  "
			ninty_line += "o  "
			eighty_line += "o  "
			seventy_line += "o  "
			sixty_line += "o  "
			fifty_line += "o  "
			fourty_line += "o  "
			thirty_line += "o  "
			twenty_line += "o  "
			ten_line += "o  "
			zero_line += "o  "
		else:
			hundred_line += "   "
			if percentages_values[i] == 90:
				ninty_line += "o  "
				eighty_line += "o  "
				seventy_line += "o  "
				sixty_line += "o  "
				fifty_line += "o  "
				fourty_line += "o  "
				thirty_line += "o  "
				twenty_line += "o  "
				ten_line += "o  "
				zero_line += "o  "
			else:
				ninty_line += "   "
				if percentages_values[i] == 80:
					eighty_line += "o  "
					seventy_line += "o  "
					sixty_line += "o  "
					fifty_line += "o  "
					fourty_line += "o  "
					thirty_line += "o  "
					twenty_line += "o  "
					ten_line += "o  "
					zero_line += "o  "
				else:
					eighty_line += "   "
					if percentages_values[i] == 70:
						seventy_line += "o  "
						sixty_line += "o  "
						fifty_line += "o  "
						fourty_line += "o  "
						thirty_line += "o  "
						twenty_line += "o  "
						ten_line += "o  "
						zero_line += "o  "
					else:
						seventy_line += "   "
						if percentages_values[i] == 60:
							sixty_line += "o  "
							fifty_line += "o  "
							fourty_line += "o  "
							thirty_line += "o  "
							twenty_line += "o  "
							ten_line += "o  "
							zero_line += "o  "
						else:
							sixty_line += "   "
							if percentages_values[i] == 50:
								fifty_line += "o  "
								fourty_line += "o  "
								thirty_line += "o  "
								twenty_line += "o  "
								ten_line += "o  "
								zero_line += "o  "
							else:
								fifty_line += "   "
								if percentages_values[i] == 40:
									fourty_line += "o  "
									thirty_line += "o  "
									twenty_line += "o  "
									ten_line += "o  "
									zero_line += "o  "
								else:
									fourty_line += "   "
									if percentages_values[i] == 30:
										thirty_line += "o  "
										twenty_line += "o  "
										ten_line += "o  "
										zero_line += "o  "
									else:
										thirty_line += "   "
										if percentages_values[i] == 20:
											twenty_line += "o  "
											ten_line += "o  "
											zero_line += "o  "
										else:
											twenty_line += "   "
											if percentages_values[i] == 10:
												ten_line += "o  "
												zero_line += "o  "
											else:
												ten_line += "   "
												if percentages_values[i] == 0:
													zero_line += "o  "
												else:			
													zero_line += "   "
	###

	# Above the horizontal line. 
	lines = percentage + "\n" + hundred_line + "\n" + ninty_line + "\n" + eighty_line + "\n" + seventy_line + "\n" + sixty_line + "\n" + fifty_line + "\n" + fourty_line + "\n" + thirty_line + "\n" + twenty_line + "\n" + ten_line + "\n" + zero_line + "\n" + " "*4 + "-"*(len(list_of_categories)*3 + 1)

	## Below the horizontal line:
	lenghts_of_names = [len(name) for name in percentages_names]
	longest_name = max(lenghts_of_names)

	names_holder = "     ."*(longest_name)
	names_list = names_holder.split(".")


	for j in range(longest_name):

		for i in range(len(list_of_categories)):		

			try:
				names_list[j] += percentages_names[i][j] + " "*2
			except:
				names_list[j] += " "*3

	names = "\n"

	for i in range(len(names_list)):

		if i < len(names_list) - 2:
			names += names_list[i] + "\n"
		elif i == len(names_list) - 2:
			names += names_list[i]
		else: pass
	##

	# Printing them altogether.
	return lines + names