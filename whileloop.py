# While loops enable us to repeat code as long as
# a condition is true

# Set a boolean to true
get_password = True

# While loop runs as long as get_password is true
while get_password == True:
    guess = input("Guess the password: ")
    if guess == "hello":
        # if they guess correctly, set get_password to false
        # so we can leave the loop
        get_password = False
    else:
        print("Wrong! Guess again")
