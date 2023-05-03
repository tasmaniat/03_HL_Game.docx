# HL component 11 - Maximum Guesses Calculator
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


import math

for item in range(0, 4):  # loop component for easy testing...

    low = int(input("Low: "))  # use int check in due course
    high = int(input("High: "))  # use int check in due course

    range = high - low + 1
    max_raw = math.log2(range)  # finds maximum # of guesses used
    max_upped = math.ceil(max_raw)  # rounds up (ceil --> ceiling
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))

    print()
