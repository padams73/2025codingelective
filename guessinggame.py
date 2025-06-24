# We import the random package so we can use a function
# to generate a random number from 1 to 10
import random
number = random.randint(1,100)

# Start a while loop that runs until the user guesses correctly
guess_number = True
while guess_number == True:
    # 1. Get input from the user

    get_guess = True
    while get_guess == True:
        try:
            guess = int(input("Guess a number: "))
            get_guess = False
        except ValueError:
            print("Please enter an integer")


    # 2. Check if their guess is correct, too high, or too low
    # (If correct, end the loop and print "That's right!"
    if guess == number:
        guess_number = False
    elif guess < number:
        print("Too low")
    else:
        print("Too high")
print("That's right")
