
import time
def czy_ciag_rosnaco_malejacy(ciag):
    stan = "START"
    poprzednik = ciag[0]

    for znak in ciag[1:]:
        if stan == "START":
            if znak <= poprzednik:
                return False
            stan = "ROSNACY"

        elif stan == "ROSNACY":
            if znak == poprzednik and poprzednik == ciag[-1]:
                return False
            elif znak <= poprzednik:
                stan = "MALEJACY"

        elif stan == "MALEJACY":
            if znak >= poprzednik:
                return False

        poprzednik = znak
    return True

# nazwaPliku = "dane/pi_przyklad.txt"
nazwaPliku = "dane/pi.txt"

plik = open(nazwaPliku, "r", encoding="utf-8")

linie = [linia[:-1] for linia in plik.readlines()]

pozycja = 0
maxCiag = []

for i in range(len(linie) - 3):

    for dlugosc in range(4, 21):
        if czy_ciag_rosnaco_malejacy(linie[i: i+dlugosc]) and i + dlugosc < len(linie):
            if dlugosc > len(maxCiag):
                maxCiag = linie[i: i+dlugosc]
                pozycja = i + 1

wynik = ""
for znak in maxCiag:
    wynik += znak

print(pozycja, wynik)

plik.close()

