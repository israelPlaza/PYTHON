#ficheros
# 1. Usamos 'with' para que sea seguro
# 2. "diario.txt" es el nombre del archivo
# 3. "w" significa que vamos a ESCRIBIR (si no existe, lo crea)
# 4. encoding="utf-8" es OBLIGATORIO si escribes tildes o 'ñ' 

with open("diario.txt", "w", encoding="utf-8") as f:
    f.write("Hoy empiezo mi diario de Python.\n") 
    # El \n es un "Enter" (salto de línea), si no, escribe todo seguido.
    

# 1. AÑADIR (Append)
# Cambia la 'w' por 'a' para no borrar lo anterior
with open("diario.txt", "a", encoding="utf-8") as f:
    f.write("¡Y esto es la segunda línea!\n")

# 2. LEER (Read)
# Abrimos en modo lectura "r"
with open("diario.txt", "r", encoding="utf-8") as f:
    contenido = f.read()  # Lee TODO el archivo de golpe
    print("--- CONTENIDO DEL DIARIO ---")
    print(contenido)