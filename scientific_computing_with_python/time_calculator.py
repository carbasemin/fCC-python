def __date_calculator__(days: int, day: str) -> str:

	if day:
		# Make it case-insensitive.
		day = day.lower()
		# Make it useful for printing.
		for i in range(len(day)):
			if i == 0:
				new_day = day[i].upper()
			else:
				new_day += day[i]

		# Assigning the days an index to do algebra on them.
		dates = {'Monday': 1,
				'Tuesday': 2,
				'Wednesday': 3,
				'Thursday': 4,
				'Friday': 5,
				'Saturday': 6,
				'Sunday': 7}
		
		dates_reversed = {1: 'Monday',
						2: 'Tuesday',
						3: 'Wednesday',
						4: 'Thursday',
						5: 'Friday',
						6: 'Saturday',
						7: 'Sunday'}

		# If we get to a new day, when adding the duration to the start time;
		if days > 0:
	
			which_day = (dates[new_day] + days) % 7
			# If dates[new_day] + days is 7, which_day becomes 0, 
			# we don't want that.
			if which_day == 0:
				date = dates_reversed[7]
			else:	
				date = dates_reversed[which_day]
		# else, do nothing.
		else:
			date = new_day
	else: pass

	return date

def __time_converter__(format: str, start_time: list=None, AM_or_PM: str=None, hours: int=None) -> list or str:
	'''Converts time.
	format: "24" converts the start_time into 24-hour and "12" converts the hours into 12-hour format.'''

	# Convert to 24-hour format.
	if format == "24":
		if AM_or_PM == 'PM' and start_time[0] != 12:
			start_time[0] += 12
		elif AM_or_PM == 'AM' and start_time[0] == 12:
			start_time[0] = 0
		else: pass
		
		return start_time
	# Convert to 12-hour format.
	elif format == "12":
		if hours == 0:
			hours_str = ["12", "AM"]
		elif hours == 12:
			hours_str = ["12", "PM"]
		elif int(hours) > 12:
			hours_str = [str(hours - 12), "PM"]
		else:
			hours_str = [str(hours), "AM"]

		return hours_str
	else: pass

def __time_printer__(day: str, hours_str: str, minutes_str: str, days: int) -> str:
	'''Prints the time in the format specified in the README.md'''

	if day:

		date = __date_calculator__(days, day)

		if days == 0:
			new_time = hours_str[0] + ':' + minutes_str + " " + hours_str[1] + f", {date}"
		##
		elif days == 1:
			new_time = hours_str[0] + ':' + minutes_str + " " + hours_str[1] + f", {date}" + " " + "(next day)"
		##
		else:
			new_time = hours_str[0] + ':' + minutes_str + " " + hours_str[1] + f", {date}" + " " + f"({days} days later)"
	else:
		if days == 0:
			new_time = hours_str[0] + ':' + minutes_str + " " + hours_str[1]
		##
		elif days == 1:
			new_time = hours_str[0] + ':' + minutes_str + " " + hours_str[1] + " " + "(next day)"
		##
		else:
			new_time = hours_str[0] + ':' + minutes_str + " " + hours_str[1] + " " + f"({days} days later)"

	return new_time

def add_time(start: str, duration: str, day: str=None) -> str:
	'''Adds the time and sometimes days.

	start: Starting time.
	duration: How much time you\'d like to pass?
	day: Which day is it? default is None.'''


	start = start.split()
	# Is it AM or PM?
	AM_or_PM = start[1]
	# First element of the list is the hour and the second is the minutes.
	start_time = start[0].split(':')
	start_time = [int(time) for time in start_time]

	# Again, first element of the list is the hour and the second is the minutes.
	duration_time = duration.split(':')
	duration_time = [int(time) for time in duration_time]

	start_time = __time_converter__("24", start_time, AM_or_PM)

	# Add the starting time and the duration. 
	minutes = start_time[1] + duration_time[1]
	hours = start_time[0] + duration_time[0]

	# How many hours live in the summed minutes?
	hours_in_minutes = divmod(minutes, 60)

	# Convert minutes into hours.
	if hours_in_minutes[0] >= 1:
		hours += 1
		minutes = hours_in_minutes[1]
	else: pass


	# How many dats live in the summed hours?
	days_in_hours = divmod(hours, 24)

	# Convert hours into days.
	if days_in_hours[0] >= 1:
		days = days_in_hours[0]
		hours = days_in_hours[1]
	else:
		days = 0

	hours_str = __time_converter__("12", hours=hours)

	# Minute formatting.
	if len(str(minutes)) < 2:
		minutes_str = "0" + str(minutes)
	else:
		minutes_str = str(minutes)

	new_time = __time_printer__(day, hours_str, minutes_str, days)

	return new_time