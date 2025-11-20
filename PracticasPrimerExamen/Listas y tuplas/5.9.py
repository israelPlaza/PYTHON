"""
Crea una lista con 10 números aleatorios entre 1 y 50 y
cuenta el número de veces que aparecen números
pares y el número de veces que aparecen números impares.
"""
import random

aleatorios = []
par=0
impar=0

for i in range(10):
    aleatorios.append(random.randint(1, 50))


for numero in aleatorios:
    if aleatorios [i] %2 ==0 :
        par+=1
    else:
        impar+=1

print(f"par {par} impar {impar}")