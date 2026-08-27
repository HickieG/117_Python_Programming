"""
This program is meant to highlight the use of loops that have a conditional break from a user input. 
The program will continue to ask the user for input until they enter a specific value that will break the loop.
More specifically, the program will ask the user to enter an integer and will calculate the square of that integer.
"""
integer_ask = 1
#integer_ask = int(input("Please enter an integer (enter 0 to stop): "))
#square = integer_ask ** 2
#print ("\nYou entered:", integer_ask)
#print ("\nThe square of", integer_ask, "is", square)
#I have been trying to get this program to not be so redundantly written, but I haven't pieced together how to start the loop without having to repeat the first input and calculation outside of the loop.

#*Thank you for the assistance during lab! Happy to not be violating the DRY principle anymore. The above commented out code was my first attempt alone, but the feedback I received helped me stop repeating the same lines of code outside of the loop.
#I am happy to have learned how to take a user input directly as an integer, as well as the use of the ** operator to calculate the square of a number.

while integer_ask != 0:
    integer_ask = int(input("\n\nPlease enter an integer (enter 0 to stop): "))
    square = integer_ask ** 2
    print ("\nYou entered:", integer_ask)
    print ("\nThe square of", integer_ask, "is", square)
    
    if integer_ask == 0:
        print ("\nYou entered 0, the loop will now stop.")