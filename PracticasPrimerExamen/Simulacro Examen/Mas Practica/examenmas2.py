ventas = [
    {"producto": "Camiseta", "precio": 15.50, "cantidad": 2},
    {"producto": "Pantalón", "precio": 30.00, "cantidad": 1},
    {"producto": "Calcetines", "precio": 5.00, "cantidad": 4},
    {"producto": "Zapatos", "precio": 50.00, "cantidad": 0} # No se vendieron
]
suma_total=0
vendidos = [venta["producto"] for venta in ventas if venta["cantidad"] >0]
print(vendidos)

for venta in ventas :
    suma= float(venta.get("precio") * venta.get("cantidad"))
    suma_total+= suma
    
print(suma_total)


ventas[2]["precio"]=6.00
print(ventas[2])

nombres_str = ", ".join(vendidos)

print(f"Productos vendidos: {nombres_str}. Ingresos totales: {suma_total}€")