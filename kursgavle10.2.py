def utför_beräkning(operand_1, räknesätt, operand_2):
    """
    Beräkna och validera argumenten (för att undvika division med noll och
    verifiera räknesättens giltighet).
    """
    if räknesätt == "+":
        return operand_1 + operand_2
    elif räknesätt == "-":
        return operand_1 - operand_2
    elif räknesätt == "*":
        return operand_1 * operand_2
    elif räknesätt == "/":
        if operand_2 == 0:
            print("Error: Division med 0")
            return None
        return operand_1 / operand_2
    else:
        print("Error: Felaktig operator!")
        return None


while True:
    inmatad_beräkning = input("Ange beräkning: ")
    lista_inmatad_beräkning = inmatad_beräkning.split()
    operand_1 = float(lista_inmatad_beräkning[0])
    räknesätt = lista_inmatad_beräkning[1]
    operand_2 = float(lista_inmatad_beräkning[2])
    resultat = utför_beräkning(operand_1, räknesätt, operand_2)
    if resultat is not None:
        print(f"{operand_1} {räknesätt} {operand_2} = {resultat}")
    print()
