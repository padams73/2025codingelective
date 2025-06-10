# Write a program that asks the user for their name, then greets them by name.

# get input and store in a variable
name = input("What is your name?")

# print hello
print(f"Hello {name}")

# Ask them to guess a number
# Using int() to make the input an integer
number = int(input("Guess a number from 1 to 10"))

# Check if the number is greater than 5
if number > 5:
    print("Too high")
# If not check if it is less than 5
elif number < 5:
    print("Too low")
# If it failed both of those tests it must have been 5
else:
    print("That's right!")

