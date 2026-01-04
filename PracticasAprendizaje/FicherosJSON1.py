import json  # <--- Importante: Herramientas para JSON

# Nuestra lista compleja
estudiantes = [
    {"nombre": "Ana", "notas": [8, 9, 7]},
    {"nombre": "Beto", "notas": [3, 4, 5]},
    {"nombre": "Carla", "notas": [9, 10, 10]}
]

# 1. GUARDAR (Serializar)
# Fíjate: la extensión ahora es .json
with open("notas.json", "w", encoding="utf-8") as f:
    # json.dump(QUE_GUARDAR, DONDE_GUARDAR, indent=4)
    # 'indent=4' es un truco para que se vea bonito y ordenado en el archivo
    json.dump(estudiantes, f, indent=4) 

print("¡Base de datos guardada! Revisa el archivo notas.json")

