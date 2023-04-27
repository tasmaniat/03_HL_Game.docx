import random

# Initialize variables for game history
game_history = []
best_score = None
worst_score = None
total_score = 0

# Ask the user how many rounds they want to play
while True:
    num_rounds = input("Enter the number of rounds to play (or 'i' for infinite mode): ")
    if num_rounds == "i":
        num_rounds = None
        break
    try:
        num_rounds = int(num_rounds)
        if num_rounds > 0:
            break
        print("Error: Number of rounds must be a positive integer.")
    except ValueError:
        print("Error: Please enter a valid number of rounds or 'i' for infinite mode.")

# Ask the user for the range of numbers to guess from
while True:
    low = int(input("Enter the lowest number to use: "))
    high = int(input("Enter the highest number to use: "))
    if low < high:
        break
    print("Error: Lowest number must be less than highest number.")

# Calculate the number of guesses allowed
if low == 1 and high == 100:
    num_guesses = 9
else:
    num_guesses = int((high - low + 1) ** 0.5) + 1

# Play the rounds
round_num = 1
while num_rounds is None or round_num <= num_rounds:
    # Generate a random secret number
    secret_number = random.randint(low, high)

    # Initialize variables for this round
    guesses = set()
    num_tries = 0

    # Ask the user to guess the number
    while True:
        guess = int(input(f"Round {round_num}, Guess the secret number between {low} and {high}: "))
        if guess < low or guess > high:
            print(f"Error: Guess must be between {low} and {high}.")
        elif guess in guesses:
            print("Error: You already guessed that number.")
        else:
            guesses.add(guess)
            num_tries += 1
            if guess == secret_number:
                print(f"Congratulations! You guessed the secret number in {num_tries} tries.")
                game_history.append(num_tries)
                total_score += num_tries
                if best_score is None or num_tries < best_score:
                    best_score = num_tries
                if worst_score is None or num_tries > worst_score:
                    worst_score = num_tries
                break
            elif guess < secret_number:
                print("Sorry, your guess is too low.")
            else:
                print("Sorry, your guess is too high.")
        if num_tries >= num_guesses:
            print(f"Sorry, you ran out of guesses. The secret number was {secret_number}.")
            game_history.append(None)
            break

    # Ask the user if they want to play another round
    if num_rounds is None:
        play_again = input("Do you want to play another round (y/n)? ")
        if play_again.lower() != "y":
            break
    else:
        round_num += 1





