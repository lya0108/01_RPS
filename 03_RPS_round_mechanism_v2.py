from email import header


def check_rounds():
    while True:

        response = input("how many rounds: ")

        round_error = "please type either <enter> or an integer that is more than 0"
        
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


# main routine

rounds_played = 0
choose_instructions = "please choose rock (r), paper (p), scissors (s)"

# ask user for # number of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # rounds heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played)
        print(heading)
        choose = input(choose_instructions)
        if rounds_played == rounds -1:
            