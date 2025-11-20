personas = [
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Beto", "ciudad": "Madrid"}, # No tiene clave 'edad'
    {"nombre": "Cloe", "edad": 40}
    ]
for per in personas :
    
    print(per.get("edad","desconocida"))
