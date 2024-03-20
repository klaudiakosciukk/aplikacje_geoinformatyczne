import json
import string


with open('teksty.json', 'r') as file:
    dane = json.load(file)
    teksty = [tekst_dict.values() for tekst_dict in dane["teksty"]]

polaczony_tekst = ' '.join([' '.join(tekst) for tekst in teksty])


polaczony_tekst = polaczony_tekst.lower() 
print(polaczony_tekst)

wyrazy = polaczony_tekst.split()  
print(wyrazy)

polaczony_tekst = polaczony_tekst.replace('.', '').replace(',', '') 
print(polaczony_tekst)


wyrazyy = polaczony_tekst.split()  
print(wyrazyy)

wyrazy_modyfikowane = []
for wyraz in wyrazyy:
    wyraz_modyfikowany = wyraz[:-1] + wyraz[-1].upper()  
    wyrazy_modyfikowane.append(wyraz_modyfikowany)

print(wyrazy_modyfikowane)


wyrazy_modyfikowane = [wyraz for wyraz in wyrazy_modyfikowane if 'a' in wyraz or 'A' in wyraz]

print(wyrazy_modyfikowane)


licznik_wystapien = {}
for wyraz in wyrazy_modyfikowane:
    if wyraz in licznik_wystapien:
        licznik_wystapien[wyraz] += 1
    else:
        licznik_wystapien[wyraz] = 1


unikatowe_wyrazy = [wyraz for wyraz, wystapienia in licznik_wystapien.items() if wystapienia == 1]

print(unikatowe_wyrazy)
print(licznik_wystapien)

data_to_save = {
    "wyrazy": wyrazy,
    "wyrazy_modyfikowane": wyrazy_modyfikowane,
    "unikatowe_wyrazy": unikatowe_wyrazy,
    "licznik_wystapien": licznik_wystapien
}


with open('wyniki.json', 'w') as json_file:
    json.dump(data_to_save, json_file, indent=4)
