game_summary = []

rounds_played = 5
best_score = float('inf')
worst_score = float('-inf')
average_guesses = 0
rounds_won = 0
rounds_lost = 0
total_guesses = 0

for item in range(1, rounds_played + 1):
    result = input("Choose result for round {}: ".format(item))

    outcome = "Round {}: {}".format(item, result)

    if result == "lost":
        rounds_lost += 1
    elif result == "win":
        rounds_won += 1

    guesses = int(input("Enter the number of guesses for round {}: ".format(item)))
    total_guesses += guesses

    if guesses < best_score:
        best_score = guesses

    if guesses > worst_score:
        worst_score = guesses

    game_summary.append((result, guesses))

# ***** Calculate Game Stats *****
average_guesses = total_guesses / rounds_played if rounds_played != 0 else 0

if rounds_played == 0:
    percent_win = 0
else:
    percent_win = rounds_won / rounds_played * 100

percent_lose = rounds_lost / rounds_played * 100 if rounds_played != 0 else 0

print()
print("----------------------")
print("won: {}\t|\t Lost: {} ".format(rounds_won, rounds_lost, ))
print("----------------------")
print()

print()
print("******* Game Scores *******")
print("Rounds\t| Result\t| Guesses")
print()
for item, (result, guesses) in enumerate(game_summary, 1):
    print("{}\t\t| {}\t\t| {}".format(item, result, guesses))

print("\n******** Summary Statistics ********")
print(" Best Score: {}\n Worst Score: {}\n Average Guesses: {:.2f}"
      .format(best_score, worst_score, average_guesses))

