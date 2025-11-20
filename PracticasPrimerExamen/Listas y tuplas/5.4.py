"""
Escribir un programa que almacene el abecedario en una lista,
elimine de la lista las letras que ocupen
posiciones múltiplos de 3, y muestre por pantalla la lista resultante
"""

abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"]
filatrado = []
for i in range(len(abecedario)):
    if (i +1)% 3 !=0:
        filatrado.append(abecedario[i])

print(filatrado)


