imiona = ["Anna", "Jan", "Maria", "Piotr"]

for indeks, imie in enumerate(imiona):
    print(f"Indeks: {indeks}, Imię: {imie}")

liczba = 6

if liczba > 0 and liczba % 2 == 0:
    print("Liczba jest dodatnia i parzysta")


liczbaa = 5

if liczbaa != 0:
    print("Liczba jest różna od zera")


owoc = "banan"
dostepne_owoce = ['jabłko', 'banan', 'pomarańcza']

if owoc in dostepne_owoce:
    print("Owoc jest dostępny")


suma = 0

while suma <= 100:
    liczba = int(input("Podaj liczbę: "))
    suma += liczba

print("Suma wprowadzonych liczb przekroczyła 100.")
print("Suma wszystkich wprowadzonych liczb:", suma)
