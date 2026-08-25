"""
    This is a beginner program that demonstrates decision logic and repetition through boolean expressions, comparisons, and if & elif statements.
    I will be drawing concepts from week 1's programs such as requesting user input, using variables, and printing output to the console.
    This will be another weather-message type program that will ask the user for the current temperature and then provide a message based on the temperature range.
"""

weather_temp_input = input("What is the current temperature in Fahrenheit? ")
# Initial ask from user for the current temperature in Fahrenheit. The input will be stored as a string in the variable weather_temp_input.

weather_temp = int(weather_temp_input)
# The input from the user is converted to an integer using the int() function and stored in the variable weather_temp. This allows for numerical comparisons in the subsequent if-elif statements

if weather_temp < 32:
    print("It's below freezing! Bundle up!")
elif weather_temp < 55:
    print("It's quite chilly. A jacket isn't a bad idea.")
elif weather_temp < 75:
    print("The weather is mild. Perfect for a walk!")
else:
    print("It's warm outside! Stay hydrated!")
# Important reminder: Write a colon after the numerical comparison in the if, elif, and else statements.
