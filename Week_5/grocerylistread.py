"""
Simple program that reads a grocery list from a written file and prints it
"""

from pathlib import Path

file_path = Path(__file__).with_name("grocery_list.txt")

with file_path.open("r", encoding="utf-8") as file:
    list = file.read()

print("Grocery list from file", file_path.name)
for item in list.splitlines():
    print("-", item)