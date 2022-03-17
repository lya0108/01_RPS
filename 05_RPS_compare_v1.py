# RPS component 3 - compare user and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # 
        print("{} vs {}".format(user_choice, comp_choice))
        if user_choice == comp_choice:
            print("You got a tie")

        elif user_choice == "rock" and comp_choice == "scissors":
            print("You won")

        elif user_choice == "paper" and comp_choice == "rock":
            print("You won")

        elif user_choice == "scissors" and comp_choice == "paper":
            print("You won")

        else:
            print("Lost to bot")
            
        
        # enter = input("You chose {}".format(user_choice))
        # if enter == "":
        #     print("The computer got {}".format(comp_choice))
        #     print("")



            # \x1b[0m