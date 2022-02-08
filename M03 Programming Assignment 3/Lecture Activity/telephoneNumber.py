################################
# Program name: telephoneNumber.py

#  Author: Gabrielle Viray
#  Course: Python Essentials
#  Date: 2/7/2022
#  Assignment: M03 Lecture Lab Activity #4 - Convert telephone entry into numbers
#  Purpose: This program prompts the user for a telephone number(containing both letters and numbers such as "CALL HOME")
#			and outputs the corresponding numbers to be inputted in a telphone.
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
	'Z'	:	'9',
	'a' :	'2',
	'b'	:	'2',
	'c'	:	'2',
	'd'	:	'3',
	'e'	:	'3',
	'f'	:	'3',
	'g'	:	'4',
	'h'	:	'4',
	'i'	:	'4',
	'j'	:	'5',
	'k'	:	'5',
	'l'	:	'5',
	'm'	:	'6',
	'n'	:	'6',
	'o'	:	'6',
	'p'	:	'7',
	'q'	:	'7',
	'r'	:	'7',
	's'	:	'7',
	't'	:	'8',
	'u'	:	'8',
	'v'	:	'8',
	'w'	:	'9',
	'x'	:	'9',
	'y'	:	'9',
	'z'	:	'9'
}

# initalize a variable called 'count' to keep track of numbers/letters in the input
count = 0


print("\nTelephone number: ")
# Loop through each character in the string
for char in range(0, len(userInput)):

	# If 7 characters/integers are reached, break out of the for-loop
	if count == 7:
		print("\n")
		break

	# If character is an empty space, do nothing and continue to the beginning of for-loop
	if userInput[char] == ' ':
		continue

	# if the third character/number is reached print out a dash(-) for number format	
	if count == 3:
		print('-', end='')

	# Handles integer numbers, and automatically prints out the integer
	if userInput[char].isnumeric():
		print(userInput[char], end='')
		count+=1

	# Handles alphabetical letters, and looks up the letter(key) in the dictionary to find the corresponding number(value) of that key
	elif userInput[char] in mapping:
		print(mapping[userInput[char]], end='')
		count+=1

