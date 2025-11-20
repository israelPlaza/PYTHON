lista = "cacahuetes,panchitos,coca-cola"

lista = lista.replace(" ,", ",").split(",")
print("\n".join(lista))