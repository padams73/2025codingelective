# Calculate the grades based on a score from 1-100

# Get the score from the user
score = int(input("Enter your score: "))

if score >= 90:
    print("You got E")
elif score >= 70:
    print("You got M")
elif score >= 50:
    print("You got A")
else:
    print("You got N")
