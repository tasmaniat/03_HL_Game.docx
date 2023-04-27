# Checks user enters an integer between a low and high number
def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

while True:
    low = int(input("Low Number: "))
    high = int(input("High NUmber: "))
    if low < high:
        break
    print("Enter an integer equal or more then 2")

    # Calculate the number of guesses allowed
if low == 1 and high == 100:
    num_guesses = 9
else:
    num_guesses = int((high - low + 1) ** 0.5) + 1



