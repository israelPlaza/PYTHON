#Lambada anónima
detector_impares = lambda numero : numero % 2 !=0

print(detector_impares(7))

#Lambadas

#filter
edades = [12, 18, 24, 15, 30, 10, 17, 55]
adultos =list(filter(lambda x: x>=18, edades))
print(adultos)

#map
precios = [100, 50, 200, 10]
rebajas = list(map(lambda x: x*0.5, precios))
print(rebajas)

#sorted
jugadores = [
    {"alias": "Slayer", "puntos": 5000},
    {"alias": "NoobMaster", "puntos": 100},
    {"alias": "ProGamer", "puntos": 9999}
]

ranking = sorted(jugadores, key=lambda u: u["puntos"])
print(ranking)