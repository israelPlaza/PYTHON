"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte por la terminal por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas
"""

contrasena = "hola"

dato = str(input("Escribe la contraseña: ").lower())

if(contrasena == dato):
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

