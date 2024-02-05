# "import random" -> é um modulo aleatorio

import random 

userWins = 0
computerWins = 0

options = ["rock", "paper", "scissors"]

while True:
    userInput = input("To play type Rock/Paper/Scissors or Q to quit the game: ").lower()
    if userInput == "q":
        break # ou podemos usar "quit()", mas ao utilizar o quit não vai resultar no ultimo print pois vai sair do programa

    if userInput not in options:
        print("Not valid option!")
        continue
    randomNumber = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2 pelos index's da lista options
    computerPick = options [randomNumber]
    print("Computer Picked: ", computerPick + ".")

    if userInput == "rock" and computerPick == "scissors":
        userWins += 1
        print("User won!")
        print("User: ", userWins)
        print("Computer: ", computerWins)
    
    elif userInput == "scissors" and computerPick == "paper":
        userWins += 1 
        print("User won!")
        print("User: ", userWins)
        print("Computer: ", computerWins)

    elif userInput == "paper" and computerPick == "rock":
        userWins += 1 
        print("User won!")
        print("User: ", userWins)
        print("Computer: ", computerWins)
    
    else: 
        print("Computer Wins!")
        computerWins += 1 
        print("User: ", userWins)
        print("Computer: ", computerWins)

        # if computerPick == "rock" and userInput == "scissors":
        # computerWins += 1
        # print("Computer won!")
        # print("User: ", userWins)
        # print("Computer: ", computerWins)
    
    # elif computerPick == "scissors" and userInput == "paper":
       # computerWins += 1 
       # print("Computer won!")
       # print("User: ", userWins)
       # print("Computer: ", computerWins)

    # elif computerPick == "paper" and userInput == "rock":
        # computerWins += 1 
        # print("Computer won!")
        # print("User: ", userWins)
        # print("Computer: ", computerWins)


print("Bye Bye!")



