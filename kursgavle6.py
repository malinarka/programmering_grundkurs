# Uppgift 6 av Malin Arkå
inmatade_heltal = input("Ange heltal: ")
lista_inmatade_heltal = inmatade_heltal.split()
lista_inmatade_heltal = [int(s) for s in lista_inmatade_heltal]
print(f"Inmatade tal som lista: {lista_inmatade_heltal}")
lista_inmatade_heltal.reverse()
print(f"Listan i omvänd ordning: {lista_inmatade_heltal}")
print(f"Sorterad lista: {sorted(lista_inmatade_heltal)}")
print(f"Listan har {len(lista_inmatade_heltal)} element")
print(f"Minsta talet i lista är {min(lista_inmatade_heltal)} och största talet är {max(lista_inmatade_heltal)}")
