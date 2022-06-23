"""
Algoritmer: 
1: Förstå och beskriv uppgiften/problemet/kraven/behoven. Uppgiften består 
i att konstruera en miniräknare. 
Användaren ska ange operander samt operator. Sedan ska programmet
genomföra beräkningen och därefter fråga om man vill genomföra en
ny beräkning, ja eller nej. Vid nej avbryts programmet och vid ja
loopas första frågorna om inmatning. Om användaren skriver in felaktigt
räknesätt ska detta hanteras utan att programmet avslutas. Programmet
ska inte heller krascha eller avslutas vid division med 0. 
Krav: f-strängar ska användas för utskrifter. 

2: Gör en principiell lösning för problemet. Skriv pseudokod. 
Upprepa följande ett godtyckligt antal ggr: 
    Läs in operand 1
    Läs in operator och validera operator
        Endast de fyra räknesätten är godkända
    Läs in operand 2 och validera
        Om användaren skriver in något ogiltigt (division med 0) skrivs texten "ogiltigt"
        ut och användaren får börja om. 
    Svaret skrivs ut och användaren frågas om denne vill göra
    en ny beräkning. 
        Om "n" avslutas programmet
        om "j" körs programmet igen
        om ogiltigt får användaren felsvar och får försöka igen (j eller n)

3: Skriv kod som implemetrar lösningen. 
4: Testa och utvärdera din lösning. 
"""


användaren_vill_fortsätta = True
while användaren_vill_fortsätta:

    # Vilken beräkning vill användaren göra?
    # Inmatning av första operanden.
    operand_1 = float(input("Ange operand: "))
       
    # Loopa tills vi fått rätt räknesätt.
    inmatat_räknesätt = None
    while inmatat_räknesätt is None:
        räknesätt = input("Ange räknesätt (+, -, *, /): ")
        if räknesätt == "+" or räknesätt == "-" or räknesätt == "*" or räknesätt == "/":
            inmatat_räknesätt = True
        else:
            print("Ogiltig inmatning, ange en operand +, -, *, eller /.")
    
    # Inmatning av andra operanden.
    # Kontrollera att det ej sker division med noll.
    inmatning_2 = None
    while inmatning_2 is None:
        operand_2 = float(input("Ange operand: "))
        if räknesätt == "/" and operand_2 == 0:
            print("Ogiltig inmatning, ange inte en division med noll")
        else: 
            inmatning_2 = True

    # Nu gör vi själva beräkningen.
    if räknesätt == "+":
        resultat = operand_1 + operand_2
    elif räknesätt == "-":
        resultat = operand_1 - operand_2
    elif räknesätt == "*":
        resultat = operand_1 * operand_2
    elif räknesätt == "/":
        resultat = operand_1 * operand_2
    print(f"Svar: {operand_1} {räknesätt} {operand_2} = {resultat}")
        
    # vill användaren göra en ny beräkning?
    användaren_vill_fortsätta = None
    while användaren_vill_fortsätta is None:
        j_eller_n = input("Vill du fortsätta (j/n)? ")
        if j_eller_n == "j":
            användaren_vill_fortsätta = True
        elif j_eller_n == "n":
            användaren_vill_fortsätta = False
            print("Programmet avslutas!")
        else:
            print("Ogiltig inmatning. Var god och ange j eller n.")
