import json

# LEER (Deserializar)
with open("notas.json", "r", encoding="utf-8") as f:
    # json.load convierte el texto del archivo otra vez en LISTAS y DICCIONARIOS
    datos_recuperados = json.load(f)

# ¡La prueba de la verdad!
# Si fuera texto, esto daría error. Como es una lista real, funcionará:
print("El segundo estudiante es:", datos_recuperados[1]["nombre"])

# Imprimimos todo para ver que está tal cual lo guardamos
print(datos_recuperados)