def arithmetic_arranger(problems, result=False):
	problems_original = problems

	if len(problems_original) > 5:
		return "Error: Too many problems."

	problems = []
	for problem in problems_original:
		problems.append(problem.split(" "))

	results = []
	for problem in problems:
		if problem[0].isdigit() and problem[2].isdigit():
			if (len(problem[0]) <= 4) and (len(problem[2]) <= 4):
				if problem[1] == "+":
					term_one = int(problem[0])
					term_two = int(problem[2])
					results.append(term_one + term_two)
				elif problem[1] == "-":
					term_one = int(problem[0])
					term_two = int(problem[2])
					results.append(term_one - term_two)
				else:
					return "Error: Operator must be '+' or '-'."
			else:
					return "Error: Numbers cannot be more than four digits."
		else:
			return "Error: Numbers must only contain digits."

	row_one = ""
	for index in range(len(problems)):
		if index < (len(problems) - 1):
			if len(problems[index][0]) > len(problems[index][2]):
				row_one += " " * 2 + problems[index][0] + "    "
			else:
				row_one += " " * (len(problems[index][2]) + 2 - (len(problems[index][0]))) + problems[index][0] + "    "
		else:
			if len(problems[index][0]) > len(problems[index][2]):
				row_one += " " * 2 + problems[index][0] + "\n"
			else:
				row_one += " " * (len(problems[index][2]) + 2 - (len(problems[index][0]))) + problems[index][0] + "\n"

	row_two = ""
	for index in range(len(problems)):
		if index < (len(problems) - 1):
			if len(problems[index][0]) > len(problems[index][2]):
				row_two += problems[index][1] + " " * (len(problems[index][0]) + 1 - (len(problems[index][2]))) + problems[index][2] + "    "
			else:
				row_two += problems[index][1] + " " + problems[index][2] + "    "
		else:
			if len(problems[index][0]) > len(problems[index][2]):
				row_two += problems[index][1] + " " * (len(problems[index][0]) + 1 - (len(problems[index][2]))) + problems[index][2] + "\n"
			else:
				row_two += problems[index][1] + " " + problems[index][2] + "\n"

	row_three = ""
	for index in range(len(problems)):
		if index < (len(problems) - 1):
			row_three += "-" * (max(len(problems[index][0]), len(problems[index][2])) + 2) + "    "
		else:
			if result == True:
				row_three += "-" * (max(len(problems[index][0]), len(problems[index][2])) + 2) + "\n"
			else:
				row_three += "-" * (max(len(problems[index][0]), len(problems[index][2])) + 2)

	row_four = ""
	if result == True:
		for index in range(len(problems)):
			if index < (len(problems) - 1):
				row_four += " " * (max(len(problems[index][0]), len(problems[index][2])) - len(str(results[index])) + 2) + str(results[index]) + "    "
			else:
				row_four += " " * (max(len(problems[index][0]), len(problems[index][2])) - len(str(results[index])) + 2) + str(results[index])

	arranged_problems = row_one + row_two + row_three + row_four

	return arranged_problems