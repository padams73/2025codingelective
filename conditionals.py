# Demonstration of conditional statements
# Get user to enter an integer
number = int(input("Enter a number"))

# We check a condition using if/else
# If the condition is true (in this case the variable called
# number is greater than 10), we run the indented code below
# the if statement.
# If the condition is not true, we bypass those indented lines
# and go down to the indented code below the else statement
if number > 10:
    print("Higher")
    print("Run this line if higher than 10")
else:
    print("Lower")
print("All done")
