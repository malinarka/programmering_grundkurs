import math


# Här ska du skapa en klass Andragradsekvation med metoderna __init__, __str__ och lösningar
class Andragradsekvation:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    
    def __str__(self):
        return f"x² + {self.p}x + {self.q} = 0"


    def lösningar(self):
        diskriminanten = (self.p/2) ** 2 - q
        if diskriminanten > 0:
            x1 = -p/2 + math.sqrt(diskriminanten)
            x2 = -p/2 - math.sqrt(diskriminanten)
            return [round(x1, 2), round(x2, 2)]
        elif diskriminanten == 0:
            x1 = -p/2
            return [round(x1, 2)]
        else:
            return []

          
# Fråga användaren om p och q i en andragradekvation x*x + px + q = 0
str = input('Ange heltalen p och q i en andragradsekvation (x\u00b2 + px + q = 0): ')
lista = str.split()

# Loopa genom alla element i listan och omvandla datatypen till decimaltal
for index in range(0, len(lista)):
    lista[index] = int(lista[index])

# Hämta ut p och q från listan
p = lista[0]
q = lista[1]

ekvation = Andragradsekvation(p, q)     # Skapa objektet
print(ekvation)

lösningar = ekvation.lösningar()        # Anropa metoden lösningar på objektet, som returnerar en lista
if len(lösningar) == 0:
    print('Ekvationen har inga reella lösningar')
elif len(lösningar) == 1:
    print(f'Ekvationen har en lösning: {lösningar[0]}')
else:
    print(f'Ekvationen har två lösningar: {lösningar[0]} och {lösningar[1]}')


str = input("Ange heltalen p och q i en andragradsekvation (x\u00b2 + px + q = 0): ")
lista = str.split()


for index in range(0, len(lista)):
    lista[index] = int(lista[index])

p = lista[0]
q = lista[1]

ekvation = Andragradsekvation(p, q)
print(ekvation)


lösningar = ekvation.lösningar()
if len(lösningar) == 0:
    print('Ekvationen har inga reella lösningar')
elif len(lösningar) == 1:
    print(f'Ekvationen har en lösning: {lösningar[0]}')
else:
    print(f'Ekvationen har två lösningar: {lösningar[0]} och {lösningar[1]}')