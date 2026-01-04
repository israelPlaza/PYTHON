stock = {
    "HDD": 50,
    "CPU": 200,
    "RAM": 70,
    "GPU": 400
}

for producto, precio in stock.items():
    if precio >=200:
        print(f"{producto} es CARO,{precio}")
    else:
        print(f"{producto} es BARATO,{precio}")
        