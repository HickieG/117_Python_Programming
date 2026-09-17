"""
    This code is meant to show how the same piece of data can be represented through different methods. I intend to use CSV, dictionary, and object styles.
"""

class ObjectStyling:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

csv_style = "x, y, z"

dictionary_style = {"x": 1, "y": 2, "z": 3}

object_style = ObjectStyling(1, 2, 3)

print("CSV style:", csv_style)

print("Dictionary style:", dictionary_style["x"], dictionary_style["y"], dictionary_style["z"])

print("Object style:", object_style.x, object_style.y, object_style.z)