#*Ett bankkonto har en ränta på 1.2 % per år. Hur mycket har startkapitalet växt efter 5 år?

startkapital = float(input("Skriv in ditt startkapital: "))
tid = 1

for i in(1, 6):
    print("År", tid, startkapital * 0.012 + startkapital)
    tid = tid + 1

    
   



resultat = int(input("Ange ditt resultat: "))

if resultat >= 48:
    print("Ditt betyg är: A")
elif resultat >= 40:
    print("Ditt betyg är: B")
elif resultat >= 32:
    print("Ditt betyg är: C")
elif resultat >= 24:
    print("Ditt betyg är: D")
elif resultat >= 16:
    print("Ditt betyg är: E")
elif resultat >= 0:
    print("Ditt betyg är: F")
else:
    print("Resultatet är ogiltigt.")
