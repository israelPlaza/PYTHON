"""
Crea un diccionario donde las claves sean nombres de personas y
los valores sean otro diccionario coninformación como edad y
ciudad. Luego, permite consultar la información de una persona por consola.
"""

personas = {}
datos = {}
dato = ""

while dato.capitalize() != "Fin":
    dato = str(input("Escribe el nombre: ")).capitalize()
    
    if dato == "fin":
        break
    
        edad = input("Escriba la edad: ")
        ciudad = input("Escrib ala ciudad: ")
    
        datos["Edad"] = edad
        datos["Ciudad"] = ciudad
    
        personas[dato] = datos
    
print("Personas: ",personas)

clave = input("Escribe el nombre de la persona: ").capitalize()

if clave in personas :
    print(personas.get(clave))