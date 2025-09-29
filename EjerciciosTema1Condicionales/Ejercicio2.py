"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte por la terminal por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas.
"""
pwd = "contraseña"

dato_entrada = str(input("Escriba la contraseña: "))

if dato_entrada.lower() == pwd: # .lower() funcion para obligar a escribir en minusculas
    input("La contraseña ES correcta.")
else :
    input("La contraseña NO es correcta.")