"""
I am taking my previous week's fraction-to-percentage code, slightly editing its structure, removing its previous comments, and giving it a couple bugs to practice debugging.
"""

def fraction_input():
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    return numerator, denominator #! initial bugged change: instead of "numerator, denominator", now says "numerator + denominator", adding two values instead of storing them separately.)


def fraction_to_percentage(numerator, denominator):
    if denominator == 0: #! initial bugged change: should be "==" for comparison, but instead writing "=" causes a syntax error.
        return "Denominator cannot be zero."
    return (numerator / denominator) * 100
# terminal error message:
# File "d:\AAISE-2026-27\Python_Programming\Week_4\debugging_first_functions.py", line 11
    # if denominator = 0: 
    #    ^^^^^^^^^^^^^^^
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

result = fraction_input()
print("Debug:", result)
numerator, denominator = result
#* Debugging shenanigans: I did not at first realize this, but when I bugged the return statement in fraction_input to add the numerator and denominator instead of returning them separately,
#* I had to adjust how I unpack the result here, otherwise I would get the following error message: 

# Traceback (most recent call last):
#   File "d:\AAISE-2026-27\Python_Programming\Week_4\debugging_first_functions.py", line 9, in <module>
#     print("Debug:", numerator + denominator)
#                     ^^^^^^^^^
# NameError: name 'numerator' is not defined. Did you mean: 'enumerate'?

#* This makes my code break if I try to unpack the result as two separate values, so I have to provide a default for the denominator as 1, making line 23 initially read as:
#* "numerator, denominator = result, 1"
#* I am essentially admitting that my code is broken before I even go to debug it, because it won't work AT ALL otherwise.
# I definitely learned a lot from this process, but not sure if it will come across properly for the assignment.
print(fraction_to_percentage(numerator, denominator), "%")

