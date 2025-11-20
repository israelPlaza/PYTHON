numero =3
otro = 0


try:
    resultado = numero / otro
    
except (ZeroDivisionError):
    print("No se puede dividi entre cero")
finally:
    print("ejecución finalizada")