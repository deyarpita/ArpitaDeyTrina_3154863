# For generating random numbers
import random
# For adding sound
import winsound

# For generating a random number between 1 and 100
random_number = random.randint(1, 100)

# Initialize the guess count as 0
guess_count = 0

# A while loop to receive the user input
while True:
    print("Press 0 to quit the Guessing_Game")
    # For the user input value
    guess = int(input("Welcome to the Guessing game! Guess a number between 1 and 100: "))
    # For increasing the guess count by 1
    guess_count += 1

    # For quiting the game at any moment
    if guess == 0:
        print("Thanks for Playing The Guessing Game!")
        break

    # To check if the guessed number by the user is correct or not
    if guess == random_number:
        # To create sound for right guessing
        winsound.Beep(1000, 1200)
        print("You Guessed The Correct Number! You Guessed it in {} attempts".format(guess_count))
        # Initialize the guess count to 0 again
        guess_count = 0

    # To check if the guessed number is too high
    elif guess > random_number:
        print("The Guessed Number is Too High!")
        # To create sound for guessing higher number
        winsound.Beep(800, 1000)

    # To check if the guessed number is too low
    elif guess < random_number:
        print("The Guessed Number is Too Low!")
        # To create sound for guessing lower number
        winsound.Beep(1000, 1000)
