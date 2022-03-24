import random

# functions
def check_rounds():
    while True:
        
        print()
        print("Odd Number of Rounds Recommended")
        response = input("\nRounds: ")

        round_error = "Please Type Either [enter] for Endless Mode\n or an Integer That is More Than 0"
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

    elif lines == "2":
        print("|",statement,"|")

    elif lines == "1":
        print(statement)
        return ""

    else:
        return ""

# main routine
print("\x1b[96m")

decorator("Please pick how many rounds you want", "=", "2")
decorator(" or press <enter> for endless mode  ", "=", "2") 

# lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# asks user if thay have played before
# if 'no' show instructions


# asks user for # of rounds then loop...
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

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

    user_choice = choose 

    if user_choice == "xxx":
        break

    print("You Chose", user_choice)

    # End game if exit code is typed
    if choose == "xxx":
        break

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Computer Chose", comp_choice)

    # Compare choices
    
    # \x1b[0m (code for color)
    if user_choice == comp_choice:
        print("\x1b[93mStop Copying Me!\x1b[96m")
        rounds_drawn += 1

    elif user_choice == "rock" and comp_choice == "scissors":
        result = 1

    elif user_choice == "paper" and comp_choice == "rock":
        result = 1

    elif user_choice == "scissors" and comp_choice == "paper":
        result = 1

    else:
        for item in range (0, 1):
            number = random.randint(1, 3)
            if number == 1:
                print("\x1b[91mLost To Bot :OMEGALUL:\x1b[96m")

            elif number == 2:
                print("\x1b[91mEZ Clap\x1b[96m")

            else:
                print("\x1b[91mWooooooooooW\x1b[96m")

        rounds_lost += 1
    
    if result == 1:
        for item in range (0, 1):
            number = random.randint(1, 3)
            if number == 1:
                print("\x1b[92mYou Won (Your still Lonely)\x1b[96m")
            
            elif number == 2:
                print("\x1b[92mY U Bully Me? Everyone Asking..\x1b[96m")
            
            else:
                print("\x1b[92mTry Harder\x1b[96m")
    # rest of loop

    rounds_played += 1

    # end game if # of rounds requested have been played
    if rounds_played == rounds:
        break


# ask user if they want to see their game history
# if 'yes' show game history

# show game stats
# quick calculations
rounds_won = rounds_played - rounds_lost - rounds_drawn

# end of game statements
print()
print("***** End Game Summary *****")
print("Won: {} | Lost: {} | Draw: {}".format(rounds_won, rounds_lost, rounds_drawn))
if rounds_lost > rounds_won:
    for item in range (0, 1):
            number = random.randint(1, 2)
            if number == 1:
                print("GGEZ")
            
            else:
                print("SO BAD")
if rounds_won > rounds_lost:
    print("I'm Set To Easy Mode Calm Down")
print()
print("Playing Rock Paper Scissors By Yourself? \nSo Lonely...")
print()