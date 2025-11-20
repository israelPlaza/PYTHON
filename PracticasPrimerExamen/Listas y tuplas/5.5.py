"""
Escribir un programa que pida por terminal una palabra y
muestre por pantalla el número de veces que
contiene cada vocal
"""
vocales = ["a","e","i","o","u"]
conteo_voclaes = [0,0,0,0,0]

palabra = input("Escribe la palabra ").lower()

for i in range(len(vocales)):
    conteo_voclaes[i] = palabra.count(vocales[i])
    

print(" A  E  I  O  U")
print(conteo_voclaes)






