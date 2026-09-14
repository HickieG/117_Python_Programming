"""
Simple program that writes a grocery list and saves it to a file
"""

from pathlib import Path


file_path = Path(__file__).with_name("grocery_list.txt")

grocery_list = ["M&Ms", "tea", "sausage", "chicken tenders", "avocados", "limes"] #added limes after list was made to see if file changed


with file_path.open("w", encoding="utf-8") as file:
    for item in grocery_list:
        file.write(item + "\n")

    print("Grocery list saved to", file_path.name)