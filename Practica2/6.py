
def invertir(cadena):
    
    if len(cadena) == 0:
        return ""
    
    else:
        return invertir(cadena[1:]) + cadena[0]

print(invertir("israel"))