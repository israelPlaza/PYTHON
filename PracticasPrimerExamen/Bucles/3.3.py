"""
Escribir un programa que pida por consola dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error sin que se lance una
Excepción.
"""

a=int(input("Escribe el primer número:"))
b=int(input("Escribe el segundo número:"))
c= a /b

if(c==0):
    print("es un error")
else:
    print("la dvison es ",c)
