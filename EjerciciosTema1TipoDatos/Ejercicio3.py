"""
Escribir un programa que pida por consola dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error sin que se lance una
Excepción.
"""
numero_primero = int(input("Escriba el primer número: "))
numero_segundo = int(input("Escriba el segundo número: "))

division= numero_primero / numero_segundo

if numero_primero % numero_segundo == 0 :
    print("Error")
else :
    print("Resultado " , numero_primero / numero_segundo)
    