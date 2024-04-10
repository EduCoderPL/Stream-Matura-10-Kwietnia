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

licznik = 0

for i in range(len(linie) - 5):
    szostka = linie[i: i+6]

    if czy_ciag_rosnaco_malejacy(szostka):
        print(szostka, czy_ciag_rosnaco_malejacy(szostka))
        licznik += 1

print(licznik)

plik.close()

