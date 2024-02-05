

print("Let's do a quizz?")
confirm = input("(Y)es or (N)o? ")

if confirm.upper() == "Y":
    points = 0
    quest1 = input("Q1: Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?")
    resp1 = input("R: ")
    if resp1 == "Tem entre 4 a 6 litros. São retirados 450 mililitros": 
        print("Está correto!")
        points += 1
        print(points)
    else:
        print("Está incorreto ;(")
    quest2 = input("Q2: De quem é a famosa frase “Penso, logo existo”?")
    resp2 = input("R: ")
    if resp2 == "Descartes":
        print("Está correto!")
        points += 1
        print(points)
    else:
        print("Está incorreto ;(")
    quest3 = input("Q3: De onde é a invenção do chuveiro elétrico?")
    resp3 = input("R: ")
    if resp3 == "Brasil":
        print("Está correto!")
        points += 1
        print(points)
    else:
        print("Está incorreto ;(")
    if points == 3:
        print("YOU GOT MAX POINTS, CONGRATS!")
    elif points == 2:
        print("You almost got it, keep up the good work")
    elif points <= 1:
        print("Try again next time dont give up")

elif confirm.upper() == "N":
    print("See ya next time")
else:
    print("Ah?")
