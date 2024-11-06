import random

def guess_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")
    
    while True:
        try:
            # Ask the player for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct, too high, or too low
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    guess_number()
