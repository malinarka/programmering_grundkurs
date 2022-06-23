
kvar_uttag = input("Hur mkt pengar vill du ta ut? ")
kvar_uttag = int(kvar_uttag)

femhundra = kvar_uttag // 500
kvar_uttag = kvar_uttag % 500
tvåhundra =  kvar_uttag // 200
kvar_uttag = kvar_uttag % 200
etthundra =  kvar_uttag // 100
kvar_uttag = kvar_uttag % 100

print("Antal 500-lappar:", femhundra, "antal 200-lappar:", tvåhundra, "antal 100-lappar:", etthundra)