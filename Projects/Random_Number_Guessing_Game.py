# Python Random Number Guessing Game
import random

def play_game():
    lowest_num = 1
    highest_num = 100
    round_number = 1

    while True:
        print(f"\n--- Round {round_number} ---")
        print(f"Guess a number between {lowest_num} and {highest_num}")
        
        answer = random.randint(lowest_num, highest_num)
        max_attempts = 7
        attempts = 0

        while attempts < max_attempts:
            guess = input("Enter your guess: ")

            # Handle invalid input (no attempt lost)
            if not guess.isdigit():
                print("Invalid input. Please enter a number.\n")
                continue

            guess = int(guess)

            # Check range
            if guess < lowest_num or guess > highest_num:
                print(f"Out of range! Enter between {lowest_num} and {highest_num}.\n")
                continue

            attempts += 1

            if guess < answer:
                print("Too low!\n")
            elif guess > answer:
                print("Too high!\n")
            else:
                print(f"Correct! The number was {answer}")
                print(f"You guessed it in {attempts} attempt(s).")
                break

        # Lose condition
        if attempts == max_attempts and guess != answer:
            print(f"Game Over! The correct number was {answer}.")

        # Ask player to continue
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()

        if play_again == "yes":
            # Increase difficulty (expand range)
            highest_num += 50   # you can tune this (e.g., +100 for faster difficulty)
            round_number += 1
        else:
            print("Thanks for playing!")
            break


# Start the game
play_game()