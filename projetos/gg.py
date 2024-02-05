#Building an Interactive Game — In this guided
#project, you’ll use basic Python concepts to create a functional and interactive word-guessing game.

print("Let's guess a word?")
confirm = input("(Y)es or (No)?")

if confirm.upper() == "Y": 
    print("_ _ _ _ _ _ _")
    tentativa = input("Try: ")
    if tentativa == "Control" or "CONTROL" or "control":
        print("You WON!!")
    else: 
        tentativa != "Control" or "Control" or "control"
        tentativa2 = input("Try again: ")
else: 
    print("See ya next time bud :D")