class Rectangle:

	def __init__(self, width: int, height: int):
		self.width = width
		self.height = height

	def __str__(self):
		return f"Rectangle(width={self.width}, height={self.height})"

	def set_width(self, width:int):
		self.width = width

	def set_height(self, height:int):
		self.height = height

	def get_area(self):
		area = self.width*self.height
		return area

	def get_perimeter(self):
		perimeter = 2*self.width + 2*self.height
		return perimeter

	def get_diagonal(self):
		diagonal = (self.width**2 + self.height **2)**(1/2)
		return diagonal

	def get_picture(self):
		'''Returns a string that represents the shape using lines of "*".
		Width or height must be smaller than 51.'''

		if self.width > 50 or self.height > 50:
			return "Too big for picture."
		else:
			picture = ""
			for i in range(self.height):
				picture += "*"*self.width + "\n"
			return picture

	def get_amount_inside(self, shape: object) -> int:
		'''Takes another shape (square or rectangle) as an argument.
		Returns the number of times the passed in shape could fit inside
		the shape (with no rotations), e.g., a rectangle with a width of 4
		and a height of 8 could fit in two squares with sides of 4.'''
		from math import floor

		# If you can fit in any, calculate that.
		if self.width >= shape.width and self.height >= shape.height:
			# How many you can fit, width-wise? 
			# Multiply that by the number you can fit height-wise.
			amount = floor(self.width / shape.width)*floor(self.height / shape.height)
		# If not, return 0.
		else:
			amount = 0

		return amount

class Square(Rectangle):

	def __init__(self, side:int):
		self.width = side
		self.height = side

	def __str__(self):
		return f"Square(side={self.width})"

	def set_side(self, side:int):
		self.width = side
		self.height = side