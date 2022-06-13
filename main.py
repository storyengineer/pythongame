import random

while True:

    thislist = ["R", "P", "S"]
    cpu = random.choice(thislist)
    data = input(" R - Rock, P - Paper, S - Scissors\nPick an Option: ")

    if data in thislist:

        if data == "R":
            if cpu == "P":
                print("Player: ", data)
                print("cpu: ", cpu)
                print("Player Loses")
            if cpu == "S":
                print("Player: ", data)
                print("cpu: ", cpu)
                print("Player Wins")
        elif data == "P":
            if cpu == "R":
                print("Player: ", data)
                print("cpu: ", cpu)
                print("Player Wins")
            if cpu == "S":
                print("Player: ", data)
                print("cpu: ", cpu)
                print("Player Loses")
        elif data == "S":
            if cpu == "R":
                print("Player: ", data)
                print("cpu: ", cpu)
                print("Player Loses")
            if cpu == "P":
                print("Player: ", data)
                print("cpu: ", cpu)
                print("Player Wins")
        elif data == cpu:
            print("Player: ", data)
            print("cpu: ", cpu)
            print("Draw")
    else:
        print("You have entered an Invalid Response.")