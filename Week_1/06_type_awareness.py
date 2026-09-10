"""
This code is meant to highlight the differences in type between strings, numbers (both integers and floats), and booleans.
"""

class_name = "Python Programming"
#defining text string
hours_per_week = 6
#integer; number without decimals
hours_spent_coding = 1.5
#float; number with decimals
having_fun = True
#boolean; true/false value

print("Class:", class_name)
print("Hours of Class per Week:", hours_per_week)
print("Hours Spent Coding:", hours_spent_coding)
print("Is it fun?:", having_fun)

print("Type of class_name:", type(class_name))
print("Type of hours_per_week:", type(hours_per_week))
print("Type of hours_spent_coding:", type(hours_spent_coding))
print("Type of having_fun:", type(having_fun))
#I'm not entirely sure why I'm printing the exact name of the value that I defined at the top
#It seems as though I assume whoever is reading the output is also reading the code itself. That is the only logical explanation to me. It is true in this case!
