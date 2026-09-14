"""
This is basically the same thing as my easyfunction.py program, but shown as a class.
"""
class ScoreCalculator:
	# Store the three scores in the object.
	def __init__(self, score1, score2, score3):
		self.score1 = score1
		self.score2 = score2
		self.score3 = score3

	# Add the scores and divide by three to find the average.
	def average(self):
		total = self.score1 + self.score2 + self.score3
		return total / 3

	# Print a message based on the average score.
	def score_message(self):
		average = self.average()
		if average >= 90:
			print("Excellent!")
		elif average >= 75:
			print("Good job!")
		else:
			print("Keep trying!")


scores = ScoreCalculator(80, 90, 100)
print(scores.average())
scores.score_message()
