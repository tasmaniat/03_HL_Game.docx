
# Function go here...
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


# Main Routine goes here...
played_before = yes_no("Have you played the "
                       "game before?  ")

if played_before == "no":
    instructions()
print()
print("Please press <enter> to begin...")
