from zajecia02 import *

# Kod z zadania 14
imiona = ['Anna', 'Jan', 'Ewa']
oceny = [5, 4, 3]

pary_imiona_oceny = zip(imiona, oceny)

for imie, ocena in pary_imiona_oceny:
    print(imie, "ma ocenę:", ocena)

# Kod z zadania 15
def kwadrat(x):
    return x ** 2

liczby = [1, 2, 3, 4, 5]

kwadraty_liczb = list(map(kwadrat, liczby))

print(kwadraty_liczb)

# Kod z zadania 17
zamowienia = []

zamowienia.append(zamowienie_produktu("Mleko", cena=2, ilosc=3))
zamowienia.append(zamowienie_produktu("Chleb", cena=3))
zamowienia.append(zamowienie_produktu("Masło", cena=5, ilosc=2))

for zamowienie in zamowienia:
    print(zamowienie[1])

suma_zamowien = oblicz_sumaryczna_wartosc(zamowienia)
print("Sumaryczna wartość zamówień:", suma_zamowien)
