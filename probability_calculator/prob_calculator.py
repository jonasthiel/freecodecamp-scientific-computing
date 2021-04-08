import copy
import random
# Consider using the modules imported above.

class Hat():

	def __init__(self, **kwargs):
		self.contents = []
		for color, number in kwargs.items():
			for i in range(number):
				self.contents.append(color)

	def draw(self, no_draws):
		if no_draws >= len(self.contents):
			return self.contents
		else:
			draws = []
			for i in range(no_draws):
				draw = self.contents[random.randint(0, len(self.contents) - 1)]
				draws.append(draw)
				self.contents.remove(draw)
			return draws


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	M = 0
	for i in range(num_experiments):
		copy_hat = copy.deepcopy(hat)
		experiment = copy_hat.draw(num_balls_drawn)
		checker = 0
		for color, number in expected_balls.items():
			if experiment.count(color) >= number:
				checker += 1
		if checker == len(expected_balls):
			M += 1
	return M / num_experiments