# Uppgift "funktioner del 1", av Malin Arkå

def print_max (a, b, c): 
    """En funktion som returnerar det största talet."""
    if a >= b and a >= c:
        print(f"Det största talet är {a}")
    elif c >= a and c >= b:
        print(f"Det största talet är {c}")
    elif b >= a and b >= c:
        print(f"Det största talet är {b}")

a = int(input("Skriv in tal 1: "))
b = int(input("Skriv in tal 2: "))
c = int(input("Skriv in tal 3: "))

print_max(a, b, c)


