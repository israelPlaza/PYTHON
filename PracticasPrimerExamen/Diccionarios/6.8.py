"""
Pide al usuario nombres de estudiantes y sus notas, almacénalos
en un diccionario y muestra la nota más alta.
"""
estudiantes= {}
dato=""

while dato.lower() != "fin":
    dato = str(input("Escribe el nombre: "))
    if dato == "fin":
        break
    nota =int(input("Escribe la nota: "))
    estudiantes[dato]=nota
    
    print(f"{dato} {nota}")


print ("Estudiantes registrado:")
print(estudiantes)

if estudiantes:
    nota_max = max(estudiantes.values())

print("nota maás alta ",nota_max)
