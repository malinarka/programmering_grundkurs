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
        return operand_1 / operand_2


while True:
    inmatad_beräkning = input("Ange beräkning: ")
    lista_inmatad_beräkning = inmatad_beräkning.split()
    operand_1 = float(lista_inmatad_beräkning[0])
    räknesätt = lista_inmatad_beräkning[1]
    if räknesätt != "+" and räknesätt != "-" and räknesätt != "*" and räknesätt != "/":
        print("Error: Felaktig operator!")
        print()
        continue
    operand_2 = float(lista_inmatad_beräkning[2])
    if operand_2 == 0 and räknesätt == "/":
        print("Error: Division med 0")
        print()
        continue
    resultat = utför_beräkning(operand_1, räknesätt, operand_2)
    print(f"{operand_1} {räknesätt} {operand_2} = {resultat}")
    print()