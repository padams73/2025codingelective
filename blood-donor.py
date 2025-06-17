# Blood donor task
# Get the user's age and weight, then check to see if they are eligible to give blood

# Get age
age = int(input("Enter your age: "))

# Get weight
weight = int(input("Enter your weight: "))

# Check if age is at least 16 and weight at least 50kg
if age >= 16  and weight >= 50:
    print("You are eligible")
else:
    print("You are not eligible")


if age < 16 or weight < 50:
    print("You are not eligible")
else:
    print("You are eligible")
