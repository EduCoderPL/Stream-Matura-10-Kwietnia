# nazwaPliku = "dane/bin_przyklad.txt"
nazwaPliku = "dane/bin.txt"

plik = open(nazwaPliku, "r", encoding="utf-8")
plikWynik = open("wyniki2_5.txt", "w", encoding="utf-8")


for linia in plik.readlines():
    liczba1 = int(linia[:-1], 2)
    liczba2 = liczba1 // 2
    wynik = str(bin(liczba1 ^ liczba2))[2:]
    plikWynik.write(wynik + "\n")

plik.close()

