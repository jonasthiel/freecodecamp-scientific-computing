class Rectangle():

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.shape = "Rectangle"

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

	def get_area(self):
		area = self.width * self.height
		return area

	def get_perimeter(self):
		perimeter = 2 * self.width + 2 * self.height
		return perimeter

	def get_diagonal(self):
		diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
		return diagonal

	def get_picture(self):
		if self.width > 50 or self.height > 50:
			return "Too big for picture."
		else:
			picture = ""
			for i in range(self.height):
				picture += "*" * self.width + "\n"
			return picture

	def get_amount_inside(self, shape_inside):
		shape_outside_area = self.get_area()
		shape_inside_area = shape_inside.get_area()
		return shape_outside_area // shape_inside_area

	def __str__(self):
		return self.shape + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"


class Square(Rectangle):

	def __init__(self, length):
		self.width = length
		self.height = length
		self.shape = "Square"

	def set_side(self, side):
		self.width = side
		self.height = side

	def set_width(self, width):
		self.width = width
		self.height = width

	def set_height(self, height):
		self.width = height
		self.height = height

	def __str__(self):
		return self.shape + "(side=" + str(self.width) + ")"