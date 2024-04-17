nazwaPliku = "dane/bin_przyklad.txt"
# nazwaPliku = "dane/bin.txt"

plik = open(nazwaPliku, "r", encoding="utf-8")

tymczasoweMax = -1

for linia in plik.readlines():
    liczba = int(linia[:-1])

    if liczba > tymczasoweMax:
        tymczasoweMax = liczba

print(tymczasoweMax)

plik.close()

