"""
The purpose of this code is to take numerical string inputs from a user, convert them to a float value, perform a calculation, and present the result to the user.
More specifically, it assumes an oncoming rainstorm, takes the amount of days raining, the amount of people living together, and multiplies those two values.
Maybe not the most helpful program but it is a bit silly.
"""

days_raining_txt = input("How many days will it be raining? ")
people_cohabitating_txt = input("How many people are in your household? ")
#taking inputs and designating them as text strings

days_raining = float(days_raining_txt)
people_cohabitating = float(people_cohabitating_txt)
#transforming the text strings into float values

soup = days_raining * people_cohabitating
#performing the SOUP calculation! very important!

print("You should make", soup, "bowls of soup while you're rained in. Or maybe 1 more :)")
#can never have too much soup