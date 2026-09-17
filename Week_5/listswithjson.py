"""
This program is my first attempt at reading from a list using JSON.
"""

import json
from pathlib import Path

input_file = Path(__file__).with_name("gameslist.json")

with open(input_file, "r") as file:
    games_list = json.load(file)

print("Games list:", input_file.name, "\n")

for game in games_list:
    print("Game: ", game["name"], "    Genre: ",game["genre"], "\n")