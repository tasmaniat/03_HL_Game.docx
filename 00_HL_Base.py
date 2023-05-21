import math
import random


# check user answers yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


# Displays instructions, returns ""
def instructions():
    print()
    print("****** Welcome to the Higher Lower Game ******")
    print()
    print("- Enter a 'low' and 'high' number")
    print("- A 'secret' number will be generated")
    print()
    print("- Your goal is to figure out the \n"
          "  secret number inside the range. ")
    print()
    print("Good Luck!")

    return ""


# checks user enters an integer between a low and high number
def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    elif low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            if situation == "any integer":
                return response
            elif situation == "both":
                if low <= response <= high:
                    return response
            elif situation == "low only":
                if response >= low:
                    return response

            print(error)

        except ValueError:
            print(error)


# Main routine goes here

# Game settings
low_number = 1
high_number = 10
mode = "regular"

# Game Statistics
rounds_played = 0
rounds_won = 0
rounds_lost = 0
total_guesses = 0
best_score = float('inf')
worst_score = float('-inf')
game_summary = []


print()
# Ask the user if they have played before
# Display instructions if they have not
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

# ask the user how many rounds they want to play with...
print()
rounds = int_check("How many rounds: ", low=1)

# asks user for a low and high number
low_number = int_check("Low Number: ")
high_number = int_check("High Number: ", low=low_number + 1)

guess_range = high_number - low_number + 1
max_raw = math.log2(guess_range)  # finds maximum # of guesses used
max_upped = math.ceil(max_raw)  # rounds up (ceil --> ceiling)
max_guesses = max_upped
print("Max Guesses: {}".format(max_guesses))

if rounds == "":
    mode = "infinite"
    rounds = 5

# Rounds loop
end_game = False
while rounds_played < rounds:

    print()

    if mode == "infinite":
        heading = f"Round {rounds_played + 1} (infinite mode)"
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    num_won = 0

    # Start Round!!
    secret = random.randint(low_number, high_number)
    guesses_left = max_guesses
    already_guessed = []
    result = ""

    while True:
        guess = int_check("Guess (or 'xxx' to exit): ", low_number,
                          high_number, "xxx")
        print("You guessed", guess)
        print()

        if guess == "xxx":
            end_game = "yes"
            break

        if guess in already_guessed:
            print("You already guessed that number! \nPlease try again."
                  " You *still* have {} guesses left".format(guesses_left))
            continue

        already_guessed.append(guess)

        if guess == secret:
            print("Congratulations! You guessed the secret number.")
            rounds_won += 1
            result = "win"
            break
        elif guesses_left > 1:
            guesses_left -= 1
            if guess < secret:
                print("Too low! Try again.")
            if guess > secret:
                print("Too high! Try again.")
        else:
            print("Out of guesses! The secret number was", secret)
            rounds_lost += 1
            result = "lost"
            break

    rounds_played += 1
    total_guesses += max_guesses - guesses_left

    if max_guesses - guesses_left < best_score:
        best_score = max_guesses - guesses_left

    if max_guesses - guesses_left > worst_score:
        worst_score = max_guesses - guesses_left

    outcome = (result, max_guesses - guesses_left)
    game_summary.append(outcome)

    if mode != "infinite" and rounds_lost >= rounds:
        break

# ***** Calculate Game Stats *****
rounds_won = rounds_played - rounds_lost
average_guesses = total_guesses / rounds_played if rounds_played != 0 else 0

# End of game Statements
print()
print("----------------------")
print("won: {}\t|\t Lost: {} ".format(rounds_won, rounds_lost, ))
print("----------------------")
print()

# Ask the user if they want to see the game statistics
show_statistics = yes_no("Do you want to see the game Statistics?")
if show_statistics == "yes":
    # Displays the game scores
    # Shows the results of the rounds in the game and
    # guesses used to find secret number
    print()
    print("******* Game Scores *******")
    print("Rounds\t| Result\t| Guesses")
    for item, (result, guesses) in enumerate(game_summary, 1):
        print("{}\t\t| {}\t\t| {}".format(item, result, guesses))

    # Show game statistics
    # Displays the best , worst and average scores of the game
    print("\n******** Summary Statistics ********")
    print("Best : {}\nWorst : {}\nAverage : "
          "{:.2f}".format(best_score, worst_score, average_guesses))
else:
    print()
    print("Thank you for playing")

    # Ask the user if they want to play again or quit
    print()
    play_again = input("Press <Enter> to play again or any "
                       "other key to quit: ").lower()
    if play_again != "":
        print()
        print("Thank you for playing")
