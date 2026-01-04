# Estado inicial del inventario
componentes = {
    "disco_ssd": 50,
    "memoria_ram": 80,
    "procesador": 200
}

# --- TUS TAREAS EMPIEZAN AQUÍ ---

# 1. Ha llegado un producto nuevo: añade una "tarjeta_grafica" que valga 400.
componentes["tarjeta grafica"] = 400

# 2. Oferta flash: baja el precio de la "memoria_ram" a 70.
componentes["memoria_ram"] = 70

# 3. Se han agotado los procesadores: elimina la clave "procesador" del diccionario.
componentes.pop("procesador")

# 4. Print the final dictionary to see how it turned out.
print(componentes)

# Escribe un código que intente buscar el precio del "monitor".
print(componentes.get("monitor", "Producto no disponible"))
