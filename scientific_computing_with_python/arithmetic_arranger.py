def __above_printer__(above: list, below: list) -> str:
	'''Prints the numbers above.'''

	# Above.
	A = str()

	for i in range(len(above)):

		if i < len(above) - 1:

			if len(above[i]) >= len(below[i]):
			# A space for the operator, a space for the space between the op. and the number,
			# the number, then four spaces.
				A += "  " + above[i] + "    "
			else:
			# A space for the operator, a space for the space between the op. and the below number,
			# enough spaces to make the numbers right aligned in harmony, then four spaces.
				A += "  " + " "*(len(below[i]) - len(above[i])) + above[i] + "    "
		
		# The last problem.
		else:
			if len(above[i]) >= len(below[i]):
			# A space for the operator and a space for the space between the op. and the number
			# and then the number then four spaces. 
				A += "  " + above[i]
			else:
			# A space for the operator, a space for the space between the op. and the below number.
			# Then spaces enough to make the numbers right aligned in harmony, then four spaces.
				A+= "  " + " "*(len(below[i]) - len(above[i])) + above[i]

	return A

def __below_printer__(above: list, below: list, operators: list) -> str:
	'''Prints below.'''

	# Below.
	B = str()

	for i in range(len(below)):

		if i < len(below) - 1:
			
			if len(above[i]) > len(below[i]):
			# Operator, a space, enough spaces to make above and below right align in sync, the number and then four spaces.
				B += operators[i] + " " + " "*(len(above[i]) - len(below[i])) + below[i] + "    "
			else:
			# The op., then a space, then the number, then four spaces.
				B += operators[i] + " " + below[i] + "    "

		# The last problem.
		else:

			if len(above[i]) > len(below[i]):
			# Operator, a space, enough spaces to make above and below right align in sync,then the number.
				B += operators[i] + " " + " "*(len(above[i]) - len(below[i])) + below[i]
			else:
			# The op. then a space, then the number, then four spaces.
				B += operators[i] + " " + below[i]

	return B

def __line_printer__(above:list, below:list) -> str:
	'''Prints the lines.'''

	# Lines.
	L = str()

	for i in range(len(below)):

		if i < len(below) - 1:

			if len(above[i]) > len(below[i]):
				# Two spaces for the operator and the space between
				# the operator and the larger number.
				L += "--" + "-"*len(above[i]) + "    "
			else:
				L += "--" + "-"*len(below[i]) + "    "
		
		# The last problem.
		else:
			if len(above[i]) >= len(below[i]):
				##
				L += "--" + "-"*len(above[i])
			else:
				L += "--" + "-"*len(below[i])

	return L

def __result__(above: list, below: list, operators: list) -> str:
	'''Prints the results'''

	# Result.
	R = str()

	for i in range(len(above)):

		if operators[i] == "+":

			op_result = int(above[i]) + int(below[i])

			n = len(str(op_result))

			if len(above[i]) > len(below[i]):
				##
				spaces = len(above[i]) + 2 - n
			else:
				spaces = len(below[i]) + 2 - n
				##
			if i < len(above) - 1:
				##
				R += " "*spaces + str(op_result) + "    "
			else:
				R += " "*spaces + str(op_result)
		else:
			op_result = int(above[i]) - int(below[i])

			n = len(str(op_result))

			if len(above[i]) > len(below[i]):
				##
				spaces = len(above[i]) + 2 - n
			else:
				spaces = len(below[i]) + 2 - n
				##
			if i < len(above) - 1:
				##
				R += " "*spaces + str(op_result) + "    "
			else:
				R += " "*spaces + str(op_result)

	return R

def arithmetic_arranger(problems: list, result=False) -> str:
	'''Middle school style addition and division.

	result: Will show the result of the operation if True; default is False.'''

	################# Looks for errors first. #################
	
	# The operation limit is five.
	if len(problems) > 5:
		return "Error: Too many problems."

	for problem in problems:

		# Get the operands and the operator into a list.
		# oo is for "operands and the operator".
		oo = problem.split()

		# The operator must be either "+"" or "-". 
		if oo[1] == '+' or oo[1] == '-':
			pass
		else:
			return "Error: Operator must be '+' or '-'."

		# Let's put our operands in lists.
		first_opd = oo[0]
		# .split() doesn't works for integers. So, let's use a list comprehension.
		first_opd = [i for i in first_opd]
		second_opd = oo[2]
		second_opd = [i for i in second_opd]
		opds = first_opd + second_opd

		# Each operand should only contain digits.
		for what in opds:
			# This is a weird way of doing things, I accept that.
			# what is a string containing the "digits". Try to convert it into integer. 
			# If it converts, then its an integer, 
			try:
				int(what)
			# if not, than raise an error and exit.
			except:
				return "Error: Numbers must only contain digits."

		# Each operand has a max of four digits in width. 
		if len(first_opd) > 4 or len(second_opd) > 4:
			return "Error: Numbers cannot be more than four digits."
		else:
			pass

	################# PRINTING #################

	# We'll seperate the operands and the operator.
	numbers = list()
	operators = list()

	# problems contain a few arithmetic operations, we'll iterate over it.
	for problem in problems:

		oo = problem.split()

		for o in oo:
			# If it's an integer, add it to numbers,
			try:
				int(o)
				numbers.append(o)
			# if not, add it to operators.
			except:
				operators.append(o)
	# Now we have the all the numbers in the list numbers and all the operators in the list operators. Good.
	
	# The even indexed numbers (which are the first numbers, e.g., 14 and 16 in ['14 + 15', '16 - 17'])
	# will be written on top and the odd numbered ones will come at the bottom.
	# So let's seperate above from the bottom.

	above = list()
	below = list()

	for i in range(len(numbers)):

		if i % 2 == 0:
			above.append(numbers[i])
		else:
			below.append(numbers[i])

	# Actual stuff that is printed on the screen:

	if result == True:
		return __above_printer__(above, below) + "\n" + __below_printer__(above, below, operators) + "\n" + __line_printer__(above, below) + "\n" + __result__(above, below, operators)

	else:
		return __above_printer__(above, below) + "\n" + __below_printer__(above, below, operators) + "\n" + __line_printer__(above, below)