
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


# Display instructions, returns ""
def instructions():
    print()
    print("**** Welcome to the Higher Lower Game ****")
    print()
    print("For each game you will be asked to...\n"
          "- Enter a 'low' and 'high' number.  ")
    print()
    print("The computer will randomly generate a 'secret' number \n"
          "between your two chosen numbers.")
    print()
    print("It will use these numbers for all\n"
          "the rounds given in a game.")
    print("- The computer will calculate how many guesses you are allowed")
    print("- enter the number of rounds you want to play")
    print("- guess the secret number")
    print()
    print("Good Luck!")
    print()
    return ""

# checks if user is using an integer between low and high number
def int_check(question, low=None, high=None):
    situation = ""

    # Check if low and high values are given
    # If both values are given, set the situation to "both"
    # If only low value is given, set the situation to "low only"
    if low is not None and high is not None:
        situation = "both"
    # Check if only low value is given
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # checks input is not too high or too low
            # if a both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between"
                          "{} and {}".format(low, high))
                    continue

            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more "
                          "than (or equal to) {}".format(low))
                    continue

            return response
        # check input is a integer
        except ValueError:
            print("please enter an integer")
            continue


def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    if low is not None and high is not None:
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

            # check that integer is valid (ie: not too low / too hig etc)
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


# main routine goes here

rounds_played = 0
rounds_won = 0

low_number = 1
high_number = 10

mode = "regular"

# Ask the user if they have played before
# Display instructions if they have not
played_before = yes_no("Have you played the "
                       "game before?  ")

if played_before == "no":
    instructions()
print()
print("Please press <enter> to begin...")
print()

rounds = int_check("How many rounds", 1, exit_code="")

if rounds == "":
    mode = "infinite"
    rounds = 5

# rounds loop
end_game = "no"
while end_game == "no":

    if mode == "infinite":
        heading = f"Round {rounds_played + 1} (infinite mode)"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1

    # Start Round!!
    while True:

        secret = 7

        guess = int_check("Guess (or 'xxx' to exit): ", low_number, high_number, "xxx")
        print("you guessed", guess)

        if guess == "xxx":
            end_game = "yes"
            break

            # compare guess to secret number
        print("Pretend we've compared")

        if guess == secret:
            rounds_won += 1
            break

    # check if we are out of rounds
    if rounds_played >= rounds:
        break
