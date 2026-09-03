"""
This week starts off with creating functions. I will be attempting to write from scratch here, not refactoring existing code.
This program intends to use functions to convert input fractions into percentages.
"""

def fraction_input():
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    return numerator, denominator
#While I was first writing my program, I had this section entirely in the main body of the code, without using functions. Then I realized it was a process that could be called!

def fraction_to_percentage(numerator, denominator):
    if denominator == 0:
        return "Denominator cannot be zero."
    return (numerator / denominator) * 100
#This function is pretty self-explanatory, but it also includes a check to prevent division by zero. 
#The AI suggestions tried to make the failed check return a ValueError, but I went with what I knew how to do.
#The two functions above work in tandem by first taking a user input as a float and then converting it into a percentage.

numerator, denominator = fraction_input()
print(fraction_to_percentage(numerator, denominator), "%")
#The phrasing here is still a bit confusing to me to be honest. Why is it supposed to be written this way?
#I assume listing the numerator and denominator values outside of the function is necessary for it to be called; without these two lines above, the code does not work.
#Still though, I feel uncertain as to how this makes everything operate when looking at it. Hopefully that clears up after working with functions more down the road.