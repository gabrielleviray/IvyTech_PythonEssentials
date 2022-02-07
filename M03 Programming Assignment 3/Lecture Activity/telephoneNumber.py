################################
# Program name: ampersandTriangle.py

#  Author: Gabrielle Viray
#  Course: Python Essentials
#  Date: 2/6/2022
#  Assignment: M03 Lecture Lab Activity - Display a pattern of ampersands
#  Purpose: This program prompts the user for a number and uses the number to display
#			a triangle with the height of the specified number. The triangle is filled
# 			in using ampersands. 
########################################

userInput = str(input("Enter a telphone number containing letters or numbers:"))

mapping = {
	'A' :	'2',
	'B'	:	'2',
	'C'	:	'2',
	'D'	:	'3',
	'E'	:	'3',
	'F'	:	'3',
	'G'	:	'4',
	'H'	:	'4',
	'I'	:	'4',
	'J'	:	'5',
	'K'	:	'5',
	'L'	:	'5',
	'M'	:	'6',
	'N'	:	'6',
	'O'	:	'6',
	'P'	:	'7',
	'Q'	:	'7',
	'R'	:	'7',
	'S'	:	'7',
	'T'	:	'8',
	'U'	:	'8',
	'V'	:	'8',
	'W'	:	'9',
	'X'	:	'9',
	'Y'	:	'9',
	'Z'	:	'9'
}

for char in userInput:
	print(char)
	if char.isnumeric():
		print(str(char), end='')

	elif char in mapping:
		print(mapping[char], end='')

		# repeatingLetter = str.charAt(char) + 1
		# if char == repeatingCharacter:
		# 	char = char+2
print('\n')


