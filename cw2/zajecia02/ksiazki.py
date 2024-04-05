ksiazki = [
    {'tytul': 'Wiedźmin', 'autor': 'Andrzej Sapkowski', 'rok_wydania': 1993},
    {'tytul': 'Harry Potter i Kamień Filozoficzny', 'autor': 'J.K. Rowling', 'rok_wydania': 1997},
    {'tytul': 'Mistrz i Małgorzata', 'autor': 'Michaił Bułhakow', 'rok_wydania': 1966},
    {'tytul': 'Zbrodnia i Kara', 'autor': 'Fiodor Dostojewski', 'rok_wydania': 1866},
    {'tytul': 'Czysty kod', 'autor': 'Robert C. Martin', 'rok_wydania': 2008}
]

def sortuj_ksiazki_po_roku():
    return sorted(ksiazki, key=lambda x: x['rok_wydania'])

def filtruj_ksiazki_po_roku(rok):
    return list(filter(lambda x: x['rok_wydania'] > rok, ksiazki))

def pobierz_tytuly_ksiazek():
    return [ksiazka['tytul'] for ksiazka in ksiazki]
