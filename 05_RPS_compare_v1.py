# RPS component 3 - compare user and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[user_index]
        user_index += 1

        # compare options
        valid = False
        while not valid:
            outcome = 0
            
            # user
            if user_choice == "rock":
                outcome += 3

            elif user_choice == "scissors":
                outcome += 2

            elif user_choice == "paper":
                outcome += 1
            
            else:
                print("Please pick rock, paper, or scissors")
                continue

            # computer
            if comp_choice == "rock":
                outcome -= 3

            elif comp_choice == "paper":
                outcome -= 2

            else:
                outcome -= 1
            
            if outcome == 0:
                print("You got a tie")
        
        enter = input("You chose {}".format(user_choice))
        if enter == "":
            print("The computer got {}".format(comp_choice))
            print("")