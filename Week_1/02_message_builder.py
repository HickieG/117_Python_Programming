"""
This code is meant to allow users to build an interactive message using a couple input functions.
"""

weather = input("What is the weather like today? ")
dinner = input("What will you be having for dinner? ")
#asking user basic questions to obtain a text string value

print("The weather outside is " + weather + ".")
print("I will be having " + dinner + " for dinner.")
#printing out a sentence based on the previous inputs.
#* I initially tried to break up the sentence between the inputs with commas, but I was running into a syntax error, so I decided to use the "+" instead.
