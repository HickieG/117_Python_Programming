"""
This is Garrett Hickie's Capstone Project for Python Programming. 

Purpose: Design an interactive app that tracks a user's class schedule, takes inputs of bedtimes and waking times to calculate how long
they slept, and tells them if they got enough sleep or not for their classes!

Initially I wanted to allow users to input their own class schedules, but for simplicity,
I decided to predefine my own schedule to avoid heuristics.

Main Features:
? Prompt user to input time going to sleep and time waking up
? Calculate the difference between two times and present in hours & minutes format
? Give the user a message regarding how much sleep they got and whether it is sufficient for their classes

Inputs:
? (Estimated) Time of Slumber
? (Estimated) Time of Waking
? Day of Week

Outputs:
? Time Slept (Time of Waking - Time of Slumber)
? Classes on Given Day (Predetermined; listed info)
? Message about sleep quality based on Time Slept
"""

import json
from datetime import datetime
from pathlib import Path


def load_project_data():
	# Loads courses and user-facing messages from the JSON file.
	data_file = Path(__file__).with_name("capstone_list.json")
	with open(data_file, "r", encoding="utf-8") as file:
		return json.load(file)


def get_time_input(prompt, messages):
	# Asks for a time such as 10:30 PM and returns minutes after midnight.
	while True:
		time_text = input(prompt).strip()
        #using .strip to remove any leading or trailing whitespace from the input
		try:
			parsed_time = datetime.strptime(time_text, "%I:%M %p")
            #* AI assisted heavily with this functionality. Was unaware of the intricacies of parsing 12-hour time formats with AM/PM.
            #* strptime is used to parse the input string of time_text (%I for hours in 12-hour format, %M for minutes, %p for AM/PM)
			return parsed_time.hour * 60 + parsed_time.minute
		except ValueError:
			print(messages["invalid_time"])


def get_day_input(prompt, messages):
	# Asks for a weekday and returns its standard capitalized name.
	valid_days = [
		"Monday", "Tuesday", "Wednesday", "Thursday",
		"Friday", "Saturday", "Sunday",
	]
	while True:
		day_text = input(prompt).strip().capitalize()
		if day_text in valid_days:
			return day_text
		print(messages["invalid_day"])


def calculate_sleep_minutes(bedtime, wake_time):
	# Calculates sleep duration, accounting for a night that crosses midnight.
	if wake_time < bedtime:
		wake_time += 24 * 60
	return wake_time - bedtime


def find_courses_for_day(course_list, selected_day):
	# Finds courses for the given day from inside capstone_list.json
	courses_for_day = []
	for course in course_list:
		course_days = [day.strip().casefold() for day in course["days"].split(",")]
		if selected_day.casefold() in course_days:
			courses_for_day.append(course)
	return courses_for_day


def get_sleep_message(sleep_minutes, messages):
	# Chooses a feedback message based on the total sleep time. My favorite function, because it's so simple!
	if sleep_minutes < 6 * 60:
		return messages["short_sleep"]
	if sleep_minutes < 8 * 60:
		return messages["some_sleep"]
	return messages["rested_sleep"]


def display_results(sleep_minutes, selected_day, course_list, messages):
	# Prints sleep duration, sleep feedback, and classes for the chosen day.
	hours_slept = sleep_minutes // 60
	minutes_slept = sleep_minutes % 60
	print(messages["sleep_result"].format(hours=hours_slept, minutes=minutes_slept))
	print(get_sleep_message(sleep_minutes, messages))

	courses_for_day = find_courses_for_day(course_list, selected_day)
	print(messages["classes_heading"].format(day=selected_day))
	if courses_for_day:
		for course in courses_for_day:
			print(f"- {course['course_name']}: {course['course_time']}")
	else:
		print(messages["no_classes"])


def main():
	# Main function that runs the sleep tracker and class schedule display.
	project_data = load_project_data()
	messages = project_data["messages"]

	print(messages["welcome"])
	bedtime = get_time_input(messages["bedtime_prompt"], messages)
	wake_time = get_time_input(messages["wake_time_prompt"], messages)
	selected_day = get_day_input(messages["day_prompt"], messages)

	sleep_minutes = calculate_sleep_minutes(bedtime, wake_time)
	display_results(
		sleep_minutes,
		selected_day,
		project_data["course_list"],
		messages,
	)
