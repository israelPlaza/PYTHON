# --- 1. Obtener y validar el número ---
numero = 0
while numero < 1:
    try:
        numero = int(input("Introduce un número (mayor o igual a 1): "))
        
        if numero < 1:
            print("Error: El número debe ser 1 o superior.")
            
    except ValueError:
        print("Error: Debes introducir un número entero.")

print(f"Has elegido el número: {numero}")
print("--- Aquí está tu triángulo ---")

# --- 2. Lógica del triángulo ---

# Bucle exterior: Controla las filas (i tomará los valores: 5, 4, 3, 2, 1)
for i in range(numero, 0, -1):
    
    # Bucle interior: Controla lo que se imprime en CADA fila
    # (j tomará valores desde i hasta 1)
    for j in range(i, 0, -1):
        
        # print(j, end="") imprime el número y evita el salto de línea
        print(j, end="")
    
    # Cuando el bucle interior termina, imprimimos un salto 
    # de línea vacío para pasar a la siguiente fila.
    print()