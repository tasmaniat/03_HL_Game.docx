# HL component 1 - Get (and Check) user input

# To Do
# Check lowest is an integer (any integer)
# Check that highest is more than lowest (lower bound only)
# Check that rounds is more than 1 (upper bound only)
# Check that guess is between lowest and highest (
# lower and upper bound)


# Number checking function goes here
def int_check(question, low=None, high=None ):

    situation = ""

    # Check if both low and high values are given
    if low is not None and high is not None:
        situation = "both"  # If both values are given, set the situation to "both"
    # Check if only low value is given
    elif low is not None and high is None:
        situation = "low only"  # If only low value is given, set the situation to "low only"

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
                    print("Please enter a number that is more"
                          "than (or equal to) {}".format(low))
                    continue

            return response
        # check input is a integer
        except ValueError:
            print("please enter an integer")
            continue




# Main routine

lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)
guess = int_check("Guess: ", lowest, highest)
