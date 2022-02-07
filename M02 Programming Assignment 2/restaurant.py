################################
# Program name: restaurant.py

#  Author: Gabrielle Viray
#  Course: Python Essentials
#  Date: 1/25/2022
#  Assignment: Module 2 - Assignment #1
#  Purpose: Python script to infrom a user of their total meal charges.
########################################


# Prompt the user for the amount of the meal (e.g. $32.95).
mealAmount = float(input("\nPlease enter the amount of the meal: "))
formattedMealAmount = "{:.2f}".format(mealAmount)

# Compute the tax on the restaurant bill. The tax should be 6.75 percent of the meal cost.
tax = mealAmount*0.0675
formattedTaxAmount = "{:.2f}".format(tax)

# Prompt the user for the tip amount (Suggesting a value equal to 18 percent of the total).
suggestedTip = "{:.2f}".format(mealAmount*0.18)
print("\nSuggested Tip(18%) = $", suggestedTip)
tipAmount = float(input("Please enter the tip amount: "))
formattedTipAmount = "{:.2f}".format(tipAmount)

# Display the meal cost, tax amount, tip amount, and total bill on the screen.
totalBill = mealAmount + tax + tipAmount
formattedBill = "{:.2f}".format(totalBill)


print(	"\nYour meal cost is $" + str() + formattedMealAmount + "." +
	  	"\nYour total tax amount is $" + str(formattedTaxAmount) + "." + 
	  	"\nYour total tip is $" + str(formattedTipAmount) + "."
	  	"\nYour total bill is $" + str(formattedBill) + ".")



