# V3 - checks that response is in a given list

# functions
def choice_checker(question, valid_list ,error):

    valid = False
    while not valid:
        
        # asks user for choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return response
        
        print(error)
        print()

# main routine
rps_list = ["rock", "paper", "scissors", "xxx"]

# loop for testing
user_choice = ""
while user_choice != "xxx":
    
    # asks user for choice and check if valid
    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ", rps_list,"please choose from rock / paper / scissors (or xxx to quit")

    # print out choice for comparison purposes
    print("you chose {}".format(user_choice))