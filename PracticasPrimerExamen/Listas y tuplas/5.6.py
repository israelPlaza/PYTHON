import random
aleatorios = []
for i in range(10):
    aleatorios.append(random.randint(1, 100))

aleatorios.sort()
print(aleatorios)

print(f"El mayor es {aleatorios[-1]}") #Muestra el ultimo
print(f"El menor es {aleatorios[0]}")