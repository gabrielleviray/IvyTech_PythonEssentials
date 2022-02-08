################################
# Program name: distance_traveled.py

#  Author: Gabrielle Viray
#  Course: Python Essentials
#  Date: 2/6/2022
#  Assignment: M03 Lecture Lab Activity #1 - Palindrome
#  Purpose: The program compares the letters from the beginning and end of a word to validate
#			if the word is a palindrome. The program takes in numbers and letters.
########################################


letters = str(input("Enter a word to check if it is a palindrome: "))

# Convert str object into a list of characters
lettersList = [list(i) for i in letters]

# Left index
i = 0

# set right index to be the end of the list
j = len(lettersList)-1

# while loop
while i <= j:
	if lettersList[i] != lettersList[j]:
		print(letters +" is not a palindrome.")
		break
	if (lettersList[i] == lettersList[j]) and (i == j):
		print(letters + " is a palindrome.")
		break

	i+=1
	j-=1






