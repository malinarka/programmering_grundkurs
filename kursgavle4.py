fortsätt = True

while fortsätt: 
    tabell = int(input("Ange tabell: "))
    startintervall = int(input("Ange startintervall: "))
    stoppintervall = int(input("Ange stoppintervall: "))

    print("--------------------")
    print(f"{tabell}:ans tabell")
    print("--------------------")

    for i in range(startintervall, stoppintervall + 1):
        produkt = tabell * i
        print(f"{i:2} * {tabell} = {produkt:3}")

    fortsätt = None
    while fortsätt == None:
        avsluta = input("Vill du avsluta j/n? ")
        if avsluta == "j" or avsluta == "J":
            fortsätt = False
        elif avsluta == "n" or avsluta == "N":
            fortsätt = True
        else: 
            print("felaktigt svar")



