import csv

estudiantes = [
    {"nombre": "Ana", "notas": [8, 9, 7]},
    {"nombre": "Beto", "notas": [3, 4, 5]},
    {"nombre": "Carla", "notas": [9, 10, 10]}
]

# Creamos el fichero CSV
with open("informe.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    
    # 1. ESCRIBIR CABECERA (Los títulos de las columnas)
    escritor.writerow(["Nombre", "Nota Media"])
    
    # 2. ESCRIBIR DATOS
    for alumno in estudiantes:
        # Calcula la media aquí (recuerda: sum / len)
        media = sum(alumno["notas"]) / len(alumno["notas"])
        
        # Escribe la fila con el nombre y la media calculada
        # escritor.writerow([ ... , ... ]) <-- Complétalo
        escritor.writerow([alumno["nombre"], round(media, 2)]) # round(..., 2) es para redondear a 2 decimales

print("¡Informe generado! Abre informe.csv en tu ordenador.")