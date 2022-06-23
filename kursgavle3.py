

summa = 0
tal = int(input("Ange ett positivt heltal: "))

while tal != 0:
    summa += tal
    tal = int(input("Ange ett positivt heltal: "))
print("Summan av de inmatade heltalen är:", summa)

igen = input("Vill du beräkna en summa till (j/n)? ")
summa = 0
tal = int(input("Ange ett positivt heltal: "))

while igen == j:
    while tal != 0:
        summa += tal
        tal = int(input("Ange ett positivt heltal: "))
else: 
    print("Du vill inte göra fler beräkningar.")
print("Summan av de inmatade heltalen är:", summa)