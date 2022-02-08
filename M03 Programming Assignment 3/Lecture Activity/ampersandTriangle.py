################################
# Program name: ampersandTriangle.py

#  Author: Gabrielle Viray
#  Course: Python Essentials
#  Date: 2/6/2022
#  Assignment: M03 Lecture Lab Activity #4 - Display a pattern of ampersands
#  Purpose: This program prompts the user for a number and uses the number to display
#			a triangle with the height of the specified number. The triangle is filled
# 			in using ampersands. 
########################################

numOflines = int(input("Enter a number to display the height of a triangle: "))

for i in range(numOflines):
	i = i + 1
	for j in range(i):
		j = j+1
		print('&', end ='')
	print('')

