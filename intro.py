# print() is a function and will output what you put in the brackets
# Note: Strings are text, need speech marks
print("Hello world")

# Numbers can be placed directly inside the brackets
print(123)
print(1.45)

# numbers like integers or floats don't brackets
# floats = floating point number

# A variable stores information
# Always give them meaningful names. In this case I am storing
# my name in a variable for the program to use later.
# Calling the variable name makes sense.
name = "Mr Adams"
# Now that the program has stored that information in a variable
# it can be used any time. Below, we print out the variable
print(name)

# Similarly, a variable can store an integer
number = 55
print(number)

# We will often ask the user to input something.
# We use the input() function for this.
# The program will forget what is entered unless we store it
# in a variable.

# Get user's name and store in a variable called user_name
user_name = input("Enter name: ")

# Get the user's age and store in a variable called age
# Notice that because age will be an integer, we need to add
# int() around the input statement.
age = int(input("How old are you?"))

# Use an f-string to print text and variables toegther
print(f"Your name is {user_name} and you are {age} years old")

