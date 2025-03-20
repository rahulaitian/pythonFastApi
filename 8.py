# Implement a number guessing game.
import random
def number_guessing_game():
    number_computer = random.randint(1,101)
    attempts = 0
    print("welcome to the number guessing game")
    print("guess any number from 1 to 100")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1 

            if guess > number_computer:
                print("guess the smaller number")
            elif guess < number_computer:
                print("guess the bigger number")
            else:
                     print(f"Congratulations! You guessed the number {number_computer} in {attempts} attempts.")
                     break
        except ValueError:
            print("Invalid input! Please enter a valid number.")    
number_guessing_game()            