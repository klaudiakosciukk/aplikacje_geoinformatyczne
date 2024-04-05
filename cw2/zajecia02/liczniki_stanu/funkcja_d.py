def licznik():
    if not hasattr(licznik, 'count'):
        licznik.count = 0
    licznik.count += 1
    return licznik.count
