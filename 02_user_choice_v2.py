# V2 - error message included when calling funtion

# functions
def choice_checker(question, error):

    valid = False
    while not valid:

        rock = ["rock", "r"]
        paper = ["paper", "p"]
        scissors = ["scissors", "s"]

        # asks user for choice
        response = input(question).lower()

        if response in rock:
            response = "rock"
            return response

        elif response in paper:
            response = "paper"
            return response

        elif response in scissors:
            response = "scissors"
            return response
        
        elif response == "xxx":
            return response
        
        else:
            print(error)

# main routine


# loop for testing
user_choice = ""
while user_choice != "xxx":
    
    # asks user for choice and check if valid
    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ", "please choose from rock / paper / scissors (or xxx to quit")

    # print out choice for comparison purposes
    print("you chose {}".format(user_choice))