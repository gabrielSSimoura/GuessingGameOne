# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
import time
import random


def endGame(guesses):
    playAgain = "y"
    print("You got " + str(guesses) + " guesses")
    playAgain = input("Do you wanna play again? (y/n): ")
    if (playAgain.lower() == "y"):
        return 1
    else:
        print("Shutting The Game Down...")
        time.sleep(2)
        exit()


def main():
    while True:

        guesses = 0
        number = random.randint(1, 9)

        while True:
            userInput = int(input(
                "Guess the number between 1 and 9 (or type (0) to quit the game: "))
            if(userInput == 0):
                if(endGame(guesses)):
                    break

            elif userInput < number:
                print("Too Low, try again")
                guesses += 1
                continue

            elif userInput > number:
                print("Too High, try again")
                guesses += 1
                continue

            elif number == userInput:
                print("That's right!")
                guesses += 1
                if(endGame(guesses)):
                    break


main()
