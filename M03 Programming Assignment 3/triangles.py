################################
# Program name: triangles.py

#  Author: Gabrielle Viray
#  Course: Python Essentials
#  Date: 02/05/2022
#  Assignment: Module 3 - Triangles
#  Purpose: Prompt the user for the length of three sides and determine whether the lengths form a triangle and what type of triangle
# 			such as right triangle, isosceles, and equilateral triangle.
########################################


# Sort list of sides from least to greatest (in-place)
def bubbleSort(lst):
	for i in range(len(lst)):
		for j in range(len(lst) - i - 1):
			if lst[j] > lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]


def isTriangle(sideOne,sideTwo,sideThree):

	# Sort lengths from least to greatest 
	lengthOfSides = [sideOne,sideTwo,sideThree]
	bubbleSort(lengthOfSides)

	if (sideOne + sideTwo > sideThree) or (sideThree + sideOne > sideTwo) or (sideThree + sideTwo > sideOne):
		print("\nThe lengths of the sides form a triangle.")

		#  Right triangle: square of the length of longest side is equal to the sum of the lengths of the other two sides
		if( (lengthOfSides[2])**2 == (lengthOfSides[0])**2 + lengthOfSides[1] **2):
			print("The triangle is a right triangle.")

		# Isosceles : length of any two sides must be equal
		elif( (sideOne == sideTwo != sideThree) or (sideTwo == sideThree != sideOne) or (sideOne == sideThree != sideTwo)):
			print("The triangle is an isosceles  triangle.")

		# Equilateral: length of all three sides must be equal
		elif(sideOne == sideTwo == sideThree):
			print("The triangle is an equilateral triangle.")
		else:
			print("The triangle is not a right triangle, an isosceles triangle, or an equilateral triangle.")

	else:
		print("\nThe lengths of the sides do not from a triangle.")


# Prompt for user input and perform input validation
sideOne =  int(input("Please enter the length of side one:"))
while(sideOne <= 0):
	sideOne = int(input("Error: Please re-enter a length greater than zero for side one:"))

	if sideOne > 0:
		break;

sideTwo =  int(input("\nPlease enter the length of side two:"))
while(sideTwo <= 0):
	sideTwo = int(input("Error: Please re-enter a length greater than zero for side two:"))

	if sideTwo > 0:
		break;

sideThree =  int(input("\nPlease enter the length of side three:"))
while(sideThree <= 0):
	sideThree = int(input("Error: Please re-enter a length greater than zero for side three:"))

	if sideThree > 0:
		break;


isTriangle(sideOne,sideTwo,sideThree)



