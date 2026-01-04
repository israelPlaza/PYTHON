alumnos = [
    {"id": 1, "nombre": "Juan", "notas": [7, 8, 9]},
    {"id": 2, "nombre": "Maria", "notas": [4, 5, 5]},
    {"id": 3, "nombre": "Pedro", "notas": [9, 9, 10]}
]

suma=0
for notas in alumnos[0]["notas"]:
    suma+=notas

media=suma / len(alumnos[0]["notas"])

print(media)

# mejor opcion
mis_notas = alumnos[0]["notas"]  # Sacamos la lista: [7, 8, 9]

# sum() suma todo lo que hay dentro, len() cuenta cuántos hay
media = sum(mis_notas) / len(mis_notas) 

print(f"La media calculada con sum() es: {media}")