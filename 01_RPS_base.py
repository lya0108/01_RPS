import random

# functions
def check_rounds():
    while True:

        response = input("Rounds: ")

        round_error = "Please type either <enter> for Endless mode\n or an integer that is more than 0"
        # check rounds is an integer more than 0 for finite mode
        if response != "":
            try:
                response = int(response)

                # if response less than 1 go back to start of loop
                if response < 1:
                    print(round_error)
                    print()
                    continue
            
            # if response is not an integer go back to start of loop
            except ValueError:
                print(round_error)
                print()
                continue

        return response

def choice_checker(question, valid_list ,error):

    valid = False
    while not valid:
        
        # asks user for choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item
        
        print(error)
        print()

def decorator(text, decoration, lines):

    ends = decoration * 5
    statement = "{} {} {}".format(ends, text, ends)
    text_length = len(statement)

    if lines == "3":
        print(decoration * text_length)
        print(statement)
        print(decoration * text_length)
        return ""

    elif lines == "1":
        print(statement)
        return ""
    else:
        return ""

# main routine

decorator("Please pick how many rounds you want\nor press <enter> for endless mode", "=", "1") 

# lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# asks user if thay have played before
# if 'no' show instructions


# asks user for # of rounds then loop...
rounds_played = 0

# ask user for # number of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # rounds heading
    print()
    if rounds == "":
        heading = "Endless Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose_instructions = "Please choose rock (r), paper (p), scissors (s)\nor 'xxx' to exit\n"
    choose_error = "Please choose from rock / paper / scissors (or 'xxx to exit)"

    # asks user for choice and check if valid
    choose = choice_checker(choose_instructions, rps_list, choose_error)


    if choose == "xxx":
        break

    # rest of loop
    print("You chose {}".format(choose))

    rounds_played += 1

    # end game if # of rounds requested have been played
    if rounds_played == rounds:
        break


# ask user if they want to see their game history
# if 'yes' show game history

# end
print("Thank you for playing")