"""
This program will be my first attempt at creating lists in Python. The idea for this program is to write down a list of games I have been playing with friends recently,
then update the list with newer games later on by appending them to the end of the list. I will also be creating a for loop to print out the list in a more readable format.
"""

games = ["Deadlock", "Slay the Spire 2", "How to Fish", "HELLDIVERS 2"]

print("Here are some games I have been playing with friends recently:")

for game in games:
    print("-", game)

games.extend(["PEAK", "Portal 2", "Counter-Strike"])
#Because I added multiple games to the list at once, my AI system recommended I use the extend() command instead of append().
#Append can only add one item at a time, while extend() can add multiple items at once. This is a good example of how AI can help me learn new things about programming.

print("\nThis is an update to the list:")

for game in games:
    print("-", game)