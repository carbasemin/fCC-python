import numpy as np

def calculate(list_of_9:list) -> dict:
	'''Gets a list containing 9 digits and converts it to 3x3 Numpy array. 
	Then it returns a dictionary containing the mean, variance, std deviation, 
	max, min, and sum along both axes and for the flattened matrix.'''

	if len(list_of_9) == 9:
		pass
	else:
		raise ValueError("List must contain nine numbers.")

	# Making an array out of a list.
	array = np.array(list_of_9)
	# Reshaping it into a 3x3 matrix.
	matrix = array.reshape(3, 3)

	# Calculations in the form [axis=1, axis=2, flattened].
	mean = [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), array.mean()]
	variance = [list(matrix.var(axis=0)), list(matrix.var(axis=1)), array.var()]
	std = [list(matrix.std(axis=0)), list(matrix.std(axis=1)), array.std()]
	max_ = [list(matrix.max(axis=0)), list(matrix.max(axis=1)), array.max()]
	min_ = [list(matrix.min(axis=0)), list(matrix.min(axis=1)), array.min()]
	sum_ = [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), array.sum()]

	return {'mean': mean,
			'variance': variance,
			'standard deviation': std,
			'max': max_,
			'min': min_,
			'sum': sum_
			}