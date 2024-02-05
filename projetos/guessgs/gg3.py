print("Let's play a guessing game?")
confirm = input("R: ")
if confirm == "Yes":
    print("Aight! Your word is: the men's best friend: _ _ _")
    tnt = input("Try to guess: ")
    if tnt.upper() == "D":
        print("D _ _")
    tnt2 = input("Try again: ")
    if tnt2.upper() == "O":
        print("D O _")
    tnt3 = input("Try again: ")
    if tnt3.upper() == "G":
        print("YOU ARE CORRECT THE WORD IS DOG!")
    else:
        i = 0
        while i < 6:
            tnt4 = input("Try again: ")
            i += 1 
            if i == 3:
                print("Oh no, you lost ;(")
elif confirm == "No":
    print("Aight, see ya next time")     
else: 
    print("Ah?")      
    