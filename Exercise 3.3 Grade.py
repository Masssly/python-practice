#Exercise 3.3
'''Exercise 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade >= 0.9 A >= 0.8 B >= 0.7 C >= 0.6 D < 0.6 F
Enter score: 0.95 A
Enter score: perfect Bad score
Enter score: 10.0 Bad score
Enter score: 0.75 C
Enter score: 0.5 F
Run the program repeatedly as shown above to test the various different values for input.'''

#Prompt entry
score = float(input("Enter a score between 0.0 and 0.1\n"))#\n for new line
if (score < 0.0) or (score > 1.0):
	print ("Error message:Out of range")
elif (score>=0.9):
	print ("A")
elif (score>=0.8):
	print ("B")
elif (score>=0.7):
	print ("C")
elif (score>=0.6):
	print ("D")
elif (score<0.6):
	print ("F")
#else print("Bad score does not work")

#Exercise 4.6 
'''Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
Score Grade > 0.9 A > 0.8 B > 0.7 C > 0.6 D <= 0.6 F
Program Execution:
Enter score: 0.95
A
Enter score: perfect Bad score
Enter score: 10.0 Bad score
Enter score: 0.75 C
Enter score: 0.5 F
Run the program repeatedly to test the various different values for input.'''

#function to compute grade
def computegrade(score):
	if (score < 0.0) or (score > 1.0):
		print ('Number entered is valid but out of the specified range.!\n')
		test()
	elif (score>=0.9):
		print ("\nThe corresponding grade is: A")
	elif (score>=0.8):
		print ("\nThe corresponding grade is: B")
	elif (score>=0.7):
		print ("\nThe corresponding grade is: C")
	elif (score>=0.6):
		print ("\nThe corresponding grade is: D")
	else:
		print ("\nThe corresponding grade is: F")

#function to accept and test input
def test ():
	userInput = 0
	while True:
		try:
			score = float(input("Enter a number between 0.0 and 1.0:\n"))
		except ValueError:
			print("Value you entered is invalid! Try gain.")
			continue
		else:
			computegrade (score)
			break
test()
