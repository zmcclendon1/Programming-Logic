"""
This program calculates prices for custom house signs.

A variable for the cost of the sign assigned to 0.00 (charge).
A variable for the number of characters assigned to 8 (numChars).
A variable for the color of the characters assigned to "gold" (color).
A variable for the wood type assigned to "oak" (woodType).




"""

# Declare and initialize variables here.
charge = 0.00
numChars = 8
color = "gold"
woodType = "oak"

# Charge for this sign.
charge = 35.00

# Write assignment and if statements here as appropriate.

if numChars > 5:
    charge += (numChars - 5) * 4


if color == "gold":
    charge += 15.00


if woodType == "oak":
    charge += 20.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))