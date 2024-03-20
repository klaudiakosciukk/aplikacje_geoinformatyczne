import math
import random
wartosc=100
dodawanie=wartosc+123.15
print(dodawanie)
potega=dodawanie**12
print(potega)
tekst=str(potega)
print(tekst)
wartosc_pi=math.pi
print(wartosc_pi)
losowa=random.choice([1,2,3,4,5])
print(losowa)

#-----
tekst=f"Wartosc: {tekst}"
print("Długość tekstu:", len(tekst))
print(dir(tekst))
tekst=tekst.upper()
print(tekst)
#tekst[2]='p'


#------
lista = list(tekst)
print (lista)
lista = lista[:7] + lista[12:13]
print(lista)
lista.append([1, 2, 3, 4, 5])
#lista.remove(':')
print(lista)

#------

lista2 = [1, 2, 3, "banan", 100]

lista3 = [x ** 2 for x in lista2 if x != "banan"]

lista4 = list(range(2, 17, 2))

print("Lista2:", lista2)
print("Lista3:", lista3)
print("Lista4:", lista4)





