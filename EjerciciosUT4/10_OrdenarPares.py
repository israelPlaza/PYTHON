personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Marta", "edad": 20}
]

resultado = sorted(personas, key=lambda x: x["edad"])

for n in resultado:
    print(n)
