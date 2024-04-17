# nazwaPliku = "dane/pi_przyklad.txt"
nazwaPliku = "dane/pi.txt"

plik = open(nazwaPliku, "r", encoding="utf-8")

linie = plik.readlines()

licznik = 0

for i in range(len(linie) - 1):
    poprzednik = linie[i][:-1]
    nastepnik = linie[i + 1][:-1]

    fragment = int(poprzednik + nastepnik)

    if fragment > 90:
        licznik += 1
print(licznik)

plik.close()

