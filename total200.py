# While loop task

# Set a variable to store the running total
total = 0

# Set boolean to true and start loop
get_number = True
while get_number == True:
    # Get number input from user
    number = int(input("Enter number: "))
    # Check if it is in the range 50-100
    # If not, print an error message
    if number < 50 or number > 100:
        print("Enter a number between 50 and 100")
    else:
        # Valid number entered
        # Add to total and print new total
        total = total + number
        print(f"Your new total is {total}")
        # Check if total exceeds 200. If so, stop loop
        if total > 200:
            get_number = False

print(f"All done, the total is {total}")
