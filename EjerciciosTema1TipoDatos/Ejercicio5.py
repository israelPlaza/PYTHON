"""
Escribir un programa que lea un entero positivo n , introducido por la linea de
comandos y después muestre en pantalla la suma de todos los enteros desde 1 hasta
n . La suma de los n primeros enteros se puede calcular como n*(n + 1)/2 .

"""

n = int(input("Escribe hasta donde quieres sumar :"))
aux=1
for i in range(n):
    aux=i
    print(f"numero {aux + i}")