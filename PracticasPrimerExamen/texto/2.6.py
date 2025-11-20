
fecha = input("Por favor, introduce una fecha en formato dd/mm/aaaa: ")
dia, mes, anio = fecha.split('/')
dia = int(dia)
mes = int(mes)
print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")