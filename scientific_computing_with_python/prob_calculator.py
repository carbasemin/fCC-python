import copy
import random
from collections import Counter

class Hat:

	def __init__(self, **kwargs):
		self.items = list(kwargs.items())
		self.contents = [item[0] for item in self.items
									for _ in range(item[1])]

	def draw(self, number:int) -> list:
		'''Accepts an argument indicating the number of balls to draw from the hat. 
		Removes balls at random from contents and returns those balls as a list of strings.
		The balls don't go back into the hat during the draw. 
		If the number of balls to draw exceeds the available quantity,
		it returns all the balls. '''
		
		# Calculating the lenght of contents twice for different jobs.
		# This one will be used for not indexing out of range.
		# This lenght doesn't change.
		n = len(self.contents)
		drawed_balls = list()

		for i in range(number):
			if i < n:
				# And this len(self.contents) is used for generating
				# a random integer for indexing. This lenght, due to taking
				# items out of it, changes; get's less and less with every loop.
				r_int = random.randint(0, len(self.contents) - 1)
				# Take an item from the hat.
				drawed_balls.append(self.contents.pop(r_int))
			else:
				# If the number of balls wanted is greater than the number of balls
				# in the hat, after taking all the balls, break the loop.
				break

		return drawed_balls



def experiment(hat: object, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
	'''Returns the probability of the experiment you define.
	
	hat: A hat object containing balls that should be copied inside the function.
    expected_balls: An object indicating the exact group of balls to attempt to draw
    from the hat for the experiment, e.g., to determine the probability of drawing
    2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
    num_balls_drawn: The number of balls to draw out of the hat in each experiment.
    num_experiments: The number of experiments to perform.
    (The more experiments performed, the more accurate the approximate probability will be.)'''

	# Number of succesfull experiments.
	M = 0
	# Number of total experiments.
	N = num_experiments
	# Do the experiment. ######### It shouldn't be done once, it should be done num_experiment times.
	for _  in range(N):

		# Lists are, as you know, assigned by reference. That means that when you modify a list, the
		# original thing gets modified, not the variable you defined. So, we use a deepcopy method
		# to copy the thing to be able to play with the lists in it without changing the originals. 
		hat_copy = copy.deepcopy(hat)
		# That's the experiment, done once.
		items_list = hat_copy.draw(num_balls_drawn)
		# That's a counter, turns our list of string into a dictionary where the frequency of items
		# are noted. 
		items = dict(Counter(items_list))
		#That's the expected experiment result.
		expected = list(expected_balls.items())
		# Boolean value of an empty list is False. We'll use that.
		shit = list()
		# How many colours are there in the expected putcome?
		for i in range(len(expected)):
			# The keys are the colours in the excepted outcome.
			key = expected[i][0]
			# If the expected ball of particular colour is drawn at least once
			try:
				# and if the number of balls drawn in that colour is equal or more 
				# to the expected value, do nothing.
				if items[key] >= expected[i][1]:
					pass
				# If it's less than expected, fill the list up. That will
				# change it's boolean value.
				else:
					shit.append("!")
			# Again, if there isn't even one ball drawn of that colour, fill the list.
			except:
				shit.append("!")
		
		# If shit is modified, then the experiment failed, don't touch M.
		if shit:
			pass
		# If shit is unmodified, then we have a successful experiment. Yeyy!
		else:
			M += 1

	return M/N