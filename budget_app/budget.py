class Category():

	def __init__(self, category):
		self.category = category
		self.ledger = []

	def deposit(self, amount, description=""):
		self.ledger.append({"amount": amount, "description": description})

	def withdraw(self, amount, description=""):
		if self.check_funds(amount) == False:
			return False
		else:
			self.ledger.append({"amount": -1 * amount, "description": description})
			return True

	def get_balance(self):
		balance = 0
		for i in self.ledger:
			balance += i["amount"]
		return balance

	def transfer(self, amount, category):
		if self.check_funds(amount) == True:
			source = self.category
			destination = category.category
			self.withdraw(amount, "Transfer to " + destination)
			category.deposit(amount, "Transfer from " + source)
			return True
		else:
			return False

	def check_funds(self, amount):
		if amount > self.get_balance():
			return False
		else:
			return True

	def __str__(self):
		headline = "*" * int(((30 - len(self.category)) / 2)) + self.category + "*" * int(((30 - len(self.category)) / 2)) + "\n"
		items = ""
		total = 0
		for item in self.ledger:
			if len(item["description"]) <= 23:
				items += item["description"] + " " * (24 - len(item["description"])) + "{:.2f}".format(float(item["amount"])) + "\n"
			else:
				items += item["description"][0:23] + " " + "{:.2f}".format(float(item["amount"])) + "\n"
			total += item["amount"]
		return headline + items + "Total: " + "{:.2f}".format(float(total))


def create_spend_chart(categories):
	headline = "Percentage spent by category\n"

	withdrawals = {}
	for category in categories:
		withdrawals[category.category] = 0
	total = 0
	for category in categories:
		for item in category.ledger:
			if float(item["amount"]) < 0:
				withdrawals[category.category] += float(item["amount"])
				total += float(item["amount"])

	percentages = {}
	for category in categories:
		percentages[category.category] = (withdrawals[category.category] / total * 100) // 10 * 10

	bar_chart = ""
	for label in range(100, -10, -10):
		row = str(label).rjust(3, " ") + "|" + " "
		i = 0
		for category in categories:
			if percentages[category.category] >= label and (i < len(categories)):
				row += "o" + "  "
				i += 1
			elif percentages[category.category] >= label:
				row += "o"
				i += 1
			else:
				row += "   "
				i += 1
		row += "\n"
		bar_chart += row

	line = "    " + "---" * len(categories) + "-\n"

	xlabels = ""
	category_names = []
	for category in categories:
		category_names.append(category.category + " " * (max([len(str(category.category)) for category in categories]) - len(category.category)))
	for i in range(max([len(str(category.category)) for category in categories])):
		row = "    "
		j = 0
		for category_name in category_names:
			j += 0
			if j < len(category_names):
				row += " " + category_name[i] + " "
			else:
				row += " " + category_name[i]

		if i < (max([len(str(category.category)) for category in categories]) - 1):
			row += " \n"
		else:
			row += " "
		xlabels += row

	return headline + bar_chart + line + xlabels