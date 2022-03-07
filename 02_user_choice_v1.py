def choice_checker(question):

    error = "Please choose from rock / paper / scissors (or xxx to quit)"

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

        else:
            print(error)

# main routine


# loop for testing
user_choice = ""
while user_choice != "xxx":
    
    # asks
    xxx = "efefa"