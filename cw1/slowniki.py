
ja = {}


ja["imie"] = "klaudia"
ja["nazwisko"] = "kosciuk"
ja["wiek"] = 21
ja["rodzice"] = [{"imie": "Anna", "wiek": 55}, {"imie": "Tom", "wiek": 60}]


print("Wartość klucza 'rodzice':", ja["rodzice"])


print("Imię pierwszego rodzica:", ja["rodzice"][0]["imie"])


print("Wszystkie klucze słownika:", ja.keys())


czy_ma_rodzenstwo = "rodzenstwo" in ja
print("Czy słownik posiada klucz 'rodzenstwo'?", czy_ma_rodzenstwo)
