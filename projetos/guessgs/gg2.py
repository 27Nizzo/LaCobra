# interface 

# 1ºtentativa

# loop finito para as tentativas 

# Venceu ou ficou sem tentativas 


print("Let's guess a word?")
confirm = input("(Y)es or (N)o? ")

if confirm.upper() == "Y":
    print("Try to guess this: _ _ _ _ _ _ _")
    tent1 = input("Try: ") 
    if tent1.upper() == "CONTROL" and len(tent1) == 7:
        print("You won!")
    else:
        i = 0 
        while i < 3:
            tentl = input("Try again: ")
            i += 1
            if i == 3:
                print("Oh no you lost ;(")
elif confirm.upper() == "N":
    print("Aight see ya next time :D")
else:
    if confirm != "N" or confirm != "Y":
        print("Ah?") 
