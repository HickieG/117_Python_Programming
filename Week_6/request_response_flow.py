"""
This code is meant to show how functions operate when drawing from a simulated API, but doesn't pull from any other files.
"""

# Function to build a request dictionary for a given student name. 
def build_request(student_name):
    return {
        "endpoint": "/grades",
        "query": {"student": student_name},
    }


# Function to choose which values to display from the response data.
def choose_display_values(response_data):
    student = response_data["student"]
    return {
        "grade": student["grade"],
        "gpa": student["gpa"],
    }

# Simulate making a request and receiving a response. Will this look different for an API call? If so, how?
request_details = build_request("Jack Smith")
simulated_response = {
    "student": {
        "name": "Jack Smith",
        "grade": "A",
        "gpa": 3.8,
    }
}

# Putting together the selected values from the simulated response via the second function.
selected_values = choose_display_values(simulated_response)

# Print the request and the selected values from the response. 
print("Request endpoint:", request_details["endpoint"])
print("Query student:", request_details["query"]["student"])
print("Selected values:", selected_values)
