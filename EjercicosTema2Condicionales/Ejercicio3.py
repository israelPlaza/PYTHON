"""
Escribir un programa que pida por consola dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error sin que se lance una
Excepción.
"""


primero= int(input("Escribe primer número: "))
segundo= int(input("Escribe segundo número: "))
rsultado= primero / segundo

if (segundo ==0) :
    print("ERROR")
else:
    print(rsultado)


