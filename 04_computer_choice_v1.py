import random

# main routine
rps_list = ["rock\n", "paper\n", "scissors\n", "xxx\n"]

# testing loop to generate 20 
for item in range(0,20):
    comp_choice = random.choice(rps_list[:-1])
    print(comp_choice, end='')