"""
Dada una lista de números, elimina los impares y
muestra la lista resultante.
"""
import random

lista_numeros = []
lista_pares =[]
for i in range(10):  #Para crar lista con numero ramdon del 1 al 30
    lista_numeros.append(random.randint(1,60))

for numero in lista_numeros:
    if numero % 2 ==0:
        lista_pares.append(numero)
        
print(lista_pares)

