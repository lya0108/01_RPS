# less repeated code / more efficient
# exit 'xxx' is available for both modes

def check_rounds():
    while True:

        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer more than 0"
        
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    print()
                    continue

            except ValueError:
                print(round_error)
                print()
                continue

        return response


# main routine

rounds_played = 0
choose_instructions = "Please choose rock (r), paper (p), scissors (s)"

# ask user for # number of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # rounds heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose = input("{} or 'xxx' to end: ".format(choose_instructions))

    if choose == "xxx":
        break
    
    elif choose == "r":
        choose = "rock"

    elif choose == "p":
        choose = "paper"

    elif choose == "s":
        choose = "scissors"
    
    # rest of loop
    print("You chose {}".format(choose))

    rounds_played += 1

    # end game if # of rounds requested have been played
    if rounds_played == rounds:
        break

print("Thank you for playing")