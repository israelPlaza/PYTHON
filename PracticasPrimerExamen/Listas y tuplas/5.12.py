"""
Pide dos listas y muestra los elementos que tienen en común.
"""

lista_1 = ["hola","pera","chocolate","limon"]
lista_2 = ["hola", "terron", "manzana"]
iguales = []


if len(lista_1) > len(lista_2):
    for valor in lista_1:
        if valor in lista_2:
            iguales.append(valor)
        
else:
    for valor in lista_2:
        if valor in lista_1:
            iguales.append(valor)
            
print("Valores iguales: ",iguales)
