def add_time(start, duration, weekday=None):
	import re

	weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	weekdays_lower = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

	start_parts = re.split(":| ", start)
	start_hours = int(start_parts[0])
	start_minutes = int(start_parts[1])
	start_clock = start_parts[2]

	duration_parts = duration.split(":")
	duration_hours = int(duration_parts[0])
	duration_minutes = int(duration_parts[1])

	new_hours = start_hours + duration_hours
	new_minutes = start_minutes + duration_minutes

	if new_minutes > 60:
		new_hours += new_minutes // 60
		new_minutes = new_minutes % 60

	if new_hours >= 12:
		clock_turner = new_hours // 12
		new_hours = new_hours % 12
		if new_hours == 0:
			new_hours = 12
	else:
		clock_turner = 0

	if clock_turner % 2 == 0:
		new_clock = start_clock
	else:
		if start_clock == "AM":
			new_clock = "PM"
		else:
			new_clock = "AM"

	if (clock_turner / 2 == 0.5) and (start_clock == "PM"):
		days_later = 1
	else:
		days_later = round(clock_turner / 2)
	if days_later == 1:
		new_days_later = "(next day)"
	elif days_later > 1:
		new_days_later = "(" + str(days_later) + " days later)"
	else:
		new_days_later = ""

	if weekday != None:
		weekday_index = weekdays_lower.index(weekday.lower())
		weekday_index += days_later
		if weekday_index > 7:
			weekday_index = weekday_index % 7

	if (new_days_later == "") and (weekday == None):
		new_time = str(new_hours) + ":" + "{:02d}".format(new_minutes) + " " + new_clock
	elif (new_days_later == "") and (weekday != None):
		new_time = str(new_hours) + ":" + "{:02d}".format(new_minutes) + " " + new_clock + ", " + weekdays[weekday_index]
	elif (new_days_later != "") and (weekday != None):
		new_time = str(new_hours) + ":" + "{:02d}".format(new_minutes) + " " + new_clock + ", " + weekdays[weekday_index] + " " + new_days_later
	else:
		new_time = str(new_hours) + ":" + "{:02d}".format(new_minutes) + " " + new_clock + " " + new_days_later

	return new_time