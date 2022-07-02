def ange_räknesätt():
    """Användaren uppmanas att ange ett önskat räknesätt."""  
    while True:
        räknesätt = input("Ange räknesätt (+, -, *, /): ")
        if räknesätt == "+" or räknesätt == "-" or räknesätt == "*" or räknesätt == "/":
            return räknesätt
        else:
            print("Ogiltig inmatning, ange en operand +, -, *, eller /.")


def ange_operand_2(räknesätt):
    """Användaren uppmanas att ange den andra operanden i en beräkning. Det sker även en kontroll för att division med noll ej sker."""
    while True:
        operand_2 = float(input("Ange operand: "))
        if räknesätt == "/" and operand_2 == 0:
            print("Ogiltig inmatning, ange inte en division med noll")
        else: 
            return operand_2

        
def utför_beräkning(räknesätt, operand_1, operand_2):
    if räknesätt == "+":
        return operand_1 + operand_2
    elif räknesätt == "-":
        return operand_1 - operand_2
    elif räknesätt == "*":
        return operand_1 * operand_2
    elif räknesätt == "/":
        return operand_1 / operand_2


def ange_fortsättning():
    """Användaren anger om den vill genomföra en ny beräkning eller om programmet ska avslutas."""
    while True:
        j_eller_n = input("Vill du fortsätta (j/n)? ")
        if j_eller_n == "j":
            return True
        elif j_eller_n == "n":
            return False
        else:
            print("Ogiltig inmatning. Var god och ange j eller n.")


användaren_vill_fortsätta = True
while användaren_vill_fortsätta:
    # Användaren skriver in det första talet.
    operand_1 = float(input("Ange operand: "))
    räknesätt = ange_räknesätt()
    operand_2 = ange_operand_2(räknesätt)
    resultat = utför_beräkning(räknesätt, operand_1, operand_2)
    print(f"Svar: {operand_1} {räknesätt} {operand_2} = {resultat}")
    användaren_vill_fortsätta = ange_fortsättning()
print("Programmet avslutas!")