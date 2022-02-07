################################
# Program name: distance_traveled.py

#  Author: Gabrielle Viray
#  Course: Python Essentials
#  Date: 2/5/2022
#  Assignment: Module 3 - Distance Traveled
#  Purpose: Calculate the distance traveled and hours a vehicle has traveled for each hour.
########################################

speed = int(input("\nWhat is the speed of the vehicle in mph? "))
while(speed < 0):
	speed = int(input("ERROR: Speed cannot be negative. Please re-enter a postive number for the speed in mph: "))
	if speed > 0:
		break;

hours = int(input("\nHow many hours has it traveled? "))
while (hours < 1):
	hours = int(int(input("ERROR: Hours traveled cannot be less than one. Please try again: ")))
	if hours >= 1:
		break;

print("\nHour             Distance Traveled")
print("----------------------------------\n")
for j in range(1, hours+1):
	print(str(j) + "                      " + str(speed*j))