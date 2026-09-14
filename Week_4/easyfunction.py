"""
This program calculates the average of three scores and prints a message based on the average. It is a little repetitive and is meant to highlight what it could be a class.
"""
def average_three_scores(score1, score2, score3):
	# Add the three scores and divide by three to find the average.
	total = score1 + score2 + score3
	return total / 3


print(average_three_scores(80, 90, 100))

def score_message(score1, score2, score3):
	average = average_three_scores(score1, score2, score3)
	if average >= 90:
		print("Excellent!")
	elif average >= 75:
		print("Good job!")
	else:
		print("Keep trying!")

score_message(80, 90, 100)
