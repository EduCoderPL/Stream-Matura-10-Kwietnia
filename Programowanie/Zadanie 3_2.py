# nazwaPliku = "dane/pi_przyklad.txt"
nazwaPliku = "dane/pi.txt"

plik = open(nazwaPliku, "r", encoding="utf-8")

linie = plik.readlines()

licznik = 0

licznikFragmentow = {}

for i in range(len(linie) - 1):
    poprzednik = linie[i][:-1]
    nastepnik = linie[i + 1][:-1]

    fragment = poprzednik + nastepnik

    if fragment in licznikFragmentow:
        licznikFragmentow[fragment] += 1
    else:
        licznikFragmentow[fragment] = 1

fragmentMin = '00'
fragmentMax = '00'

for fragment, liczba in licznikFragmentow.items():
    if liczba < licznikFragmentow[fragmentMin]:
        fragmentMin = fragment

    if liczba > licznikFragmentow[fragmentMax]:
        fragmentMax = fragment

print(fragmentMin, licznikFragmentow[fragmentMin])
print(fragmentMax, licznikFragmentow[fragmentMax])




plik.close()

