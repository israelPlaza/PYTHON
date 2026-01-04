# Una LISTA que contiene DICCIONARIOS
def calcular_promedio(total_notas):
    media= sum(total_notas) / len(total_notas)
    return media

estudiantes = [
    {"nombre": "Ana", "notas": [8, 9, 7]},    # Estudiante 0
    {"nombre": "Beto", "notas": [3, 4, 5]},   # Estudiante 1
    {"nombre": "Carla", "notas": [9, 10, 10]} # Estudiante 2
]

#Añadir estudiante
estudiantes.append({"nombre": "Dani", "notas": [6, 6, 6]})

#Corregir Beto
estudiantes[1]["notas"][0]=5

#calcular nota media
total_notas = estudiantes[0]["notas"]
media= sum(total_notas) / len(total_notas)
print(f"La nota media es: {media}")

#imprimir solo nombre
for n in estudiantes:

    print(n["nombre"])
print()

#Calcular con la funcion la nota media
total_notas= estudiantes[1]["notas"]
print(calcular_promedio(total_notas))
print()

#Nota media de todos los estudiantes
for n in estudiantes:
    total_notas =n["notas"]
    print(f"La nota media de {n["nombre"]} es {calcular_promedio(total_notas)}")
    