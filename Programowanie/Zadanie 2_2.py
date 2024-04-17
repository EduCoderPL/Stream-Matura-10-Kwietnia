
def policz_liczbe_blokow(liczba):

    b = 0
    poprzednik = -1

    for bit in liczba:
        if bit != poprzednik:
            b += 1
        poprzednik = bit

    return b



# nazwaPliku = "dane/bin_przyklad.txt"
nazwaPliku = "dane/bin.txt"

plik = open(nazwaPliku, "r", encoding="utf-8")
licznik = 0

for linia in plik.readlines():
    liczba = linia[:-1]
    liczbaBlokow = policz_liczbe_blokow(liczba)

    if liczbaBlokow <= 2:
        licznik += 1


print(licznik)
plik.close()