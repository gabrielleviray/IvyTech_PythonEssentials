################################
# Program name: guessing_game.py

#  Author: Gabrielle Viray
#  Course: Python Essentials
#  Date: 2/6/2022
#  Assignment: M03 Lecture Lab Activity #2 - Guessing Game
#  Purpose: The program is to write a number guessing game program. If the user
# 			fails to guess the number after 6 attempts, the script terminates. 
########################################

from random import randint

correctValue = randint(1,100)
print("For testing purposes, the correct number is: "+str(correctValue))
usersValue = int(input("\nEnter in a number to guess the correct value between 1 and 100: "))
guessCount = 1

while (guessCount <= 6):
	if usersValue == correctValue:
		print("Your guessed value of " + str(usersValue) + " is correct. You win the game!")
		break
	if usersValue != correctValue and guessCount > 6:
		print("You've ran out of attempts!")
		break
	if usersValue < correctValue:
		usersValue = int(input("Incorrect value. Your number is lower than the correct value. Please try again: " ))
		guessCount+=1
	elif usersValue > correctValue:
		usersValue = int(input("Incorrect value. Your number is higher than the correct value. Please try again: " ))
		guessCount+=1

print("\n--------------------------Game over.--------------------------")
