#6
import this
dane = (2024, 'Python', 3.8)
rok, jezyk, wersja = dane
print("Rok:", rok)
print("Język:", jezyk)
print("Wersja:", wersja)

#7
oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny
print("Pierwsza:", pierwsza)
print("Środek:", srodek)
print("Ostatnia:", ostatnia)

#8
info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
imie, nazwisko, *_ , zawod= info
print("Imię:", imie)
print("Nazwisko:", nazwisko)
print("Zawod:", zawod)

#9
dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
rok = dane[0]
jezyk = dane[1][0]
wersja = dane[1][1]
opis = dane[1][2][0]
print("Rok:", rok)
print("Język:", jezyk)
print("Wersja:", wersja)
print("Opis wersji:", opis)

#10
a = b = [1, 2, 3]
b[0] = 'zmieniono'

print("Lista a po zmianie w b:", a)
print("Lista b po zmianie w b:", b)

#11
c = a[:]

c[0] = 'nowa wartość'

print("Lista a:", a)
print("Lista b:", b)
print("Lista c po modyfikacji:", c)

#12
x = y = 10
y = y + 1

print("Wartość x:", x)
print("Wartość y:", y)

#13
K=[1,2]
L=K
K=K+[3,4]
M=[1,2]
N=M
M +=[3,4]

print(K, L, M, N)

#14
