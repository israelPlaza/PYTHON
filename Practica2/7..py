
def es_palindromo(cadena):
    
    if len(cadena.lower()) <= 1:
        return True
    
    if cadena[0] == cadena[-1]:
        
        return es_palindromo(cadena[1:-1])
    else:
        
        return False

print(es_palindromo("anilina"))