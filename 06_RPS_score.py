# rounds won will be calculated (total - draw - lost)
import re


rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# results for testing
testing = ["won", "won", "loss", "loss", "tie"]

# play game
for item in testing:
    rounds_played += 1

    # generate computer choice

    result = item

    if result == "tie":
        result = "It's a tie"
        rounds_drawn += 1
    elif result == "loss":
        rounds_lost += 1

# quick calculations
rounds_won = rounds_played - rounds_lost - rounds_drawn

# end of game
print()
print("***** End Game Summary *****")
print("Won: {} | Lost: {} | Draw: {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("I hope u enjoyed")
print()