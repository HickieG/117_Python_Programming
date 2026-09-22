"""
This code contains functions to simulate fetching data from an API using a local json file for its data source.
The main goal is to avoid printing raw JSON data directly and instead provide a structured way to access specific values.
I am going to use data from my request response flow, but have it formatted into a json first to highlight a difference.
"""

# Bringing in json data to this script.
import json
from pathlib import Path

# Delineating what input file to draw from.
input_file = Path(__file__).with_name("student_grades.json")

# This section makes the most and least sense to me. As I understand it, we open, read, and give a charset to the json file.
# Then, we assign its contents to the variable `student_data` for easier access within the rest of the script.
with input_file.open("r", encoding="utf-8") as file:
    student_data = json.load(file)

# Printing multiple students' information using the defined function. At first, I was writing this out twice manually, violating DRY!
def print_student_info(student_index):
    print("Student:", student_data["students"][student_index]["name"])
    print("GPA:", student_data["students"][student_index]["gpa"])
    print("Course:", student_data["courses"][student_index]["name"])
    print("Credits:", student_data["courses"][student_index]["credits"])
    print("Passing:", student_data["courses"][student_index]["passing"])

# One flaw here is that this function assumes the student and course indices are the same, which may not always be the case.
# However, this works fine for the current dataset where the student and course indices align. :P
print_student_info(0)
print()
print_student_info(1)




