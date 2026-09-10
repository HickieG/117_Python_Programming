"""
Week 2, Assignment 3: Loops and Repetitions

My first loop will be an accumulator that sums up all the multiples of 10 from 0 to 100.
"""

total = 0
#Value to hold the sum of all multiples set at 0.

print("This program will add all the multiples of 10 up to 100, starting at 0.")
# Beginning message to give context to the output before the loop starts.

for number in range(0, 101, 10):
    total += number
    print("plus", number, "is", total)
# Learned through experimentation that the range() function can take a third argument that specifies the step size.
# In this case, I set the step size to 10 to only include multiples of 10 in the loop.

print("The sum of all multiples of 10 from 0 to 100 is:", total)
# Final message displaying the total to the user after the loop has completed.