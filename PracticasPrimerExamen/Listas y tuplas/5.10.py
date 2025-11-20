"""
Crea una lista con los colores ["rojo", "azul", "verde"]
y que lea por consola otro color, debe decir
si el color introducido está en la lista
"""

colores = ["rojo", "azul", "verde"]

color= input("Escriba el color ").lower()

if color in colores:
    print("color está")
else:
    print("color no esta")
