################################
# Program name: weights.py

#  Author: Gabrielle Viray
#  Course: Python Essentials
#  Date: 1/30/2022
#  Assignment: Module 2 - Assignment #2
#  Purpose: Python script that prompts the user for their name and weight. The program greets the user by their name
#           then calculates and displays the user's weight on other planets. Each item is disppplayed on a line by itself.
########################################

# Prompt the user for their name and weight.
userName = input("Please enter your name.\n")
userWeight = float(input("Please enter your weight in pounds.\n"))

# Greet the user by their name.
print("\nHello " + userName + "!" + " Your weight on the following planets are:\n")


# Create a dictionary to store Planets' multiple of Earth's gravity
planet_dictionary = {
					"Sun": 27.01,
					"Mercury": 0.38,
					"Venus": 0.91,
					"Earth": 1,
					"Moon": 0.166,
					"Mars": 0.38,
					"Jupiter": 2.34,
					"Saturn": 1.06,
					"Uranus": 0.92,
					"Neptune": 1.19,
					"Pluto": 0.06
					}

# Create empty dictionary to store user's weights on each planet after calculation.
userWeights_dictionary = {}

# Loop through planet dictionary and multiply the value of each key to the user's weights
for key in planet_dictionary:

	# Weight Calculation
	planetWeight = userWeight * planet_dictionary[key]

	# Storing user's weight in new dictioary
	userWeights_dictionary[key] = planetWeight

# Loop through the dictionary and print each value
for key in userWeights_dictionary:
	print("			" + key + ": " + str("{:.2f}".format(userWeights_dictionary[key])) + " lbs.")


