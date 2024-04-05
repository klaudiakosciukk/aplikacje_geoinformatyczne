def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    wartosc_zamowienia = cena * ilosc
    tekst_podsumowanie = f"Produkt: {nazwa_produktu}, Cena: {cena}, Ilość: {ilosc}, Łączna cena: {wartosc_zamowienia}"
    return tekst_podsumowanie, wartosc_zamowienia

def oblicz_sumaryczna_wartosc(zamowienia):
    return sum(zamowienie[1] for zamowienie in zamowienia)
