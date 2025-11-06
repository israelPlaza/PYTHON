import secrets

#Creamos primero la función para verificar la posición de las letras
def verficar_letras(palabra_secreta, intento):
    intento = intento.upper();
    palabra_secreta= palabra_secreta.upper()
    longitud=int(5)
    resultado= ["⬛"] *longitud #Para poner los huecos de la palbra en negro
    letras_secreta = list(palabra_secreta)
    
    #hacemos primera pasada para colocar los huecos verdes
    for i in range(longitud):
        if intento[i] == palabra_secreta[i]:
            resultado[i] = "🟩"
            letras_secreta[i] = None #None es para poner que ya ha sido usada
            
    #Segunda pasada para amarillos
    for i in range(longitud):
        if resultado[i] == "🟩":
            continue #Si ya es verde se salta, paa poner amarillos
        if intento[i] in letras_secreta:
            resultado[i] = "🟨"
            letras_secreta.remove(intento[i]) 
            #para evitar que una misma letra de la palabra secreta cuente dos veces como amarilla

    return resultado


#creamos la lista de palabras
lista_palabras = ["ARBOL", "CASAS", "CALDO", "CABRA", "CABAL",
                  "MANGO", "PERRO", "GATOS", "LAPIZ", "LENIN","MARXS"]
palabra_secreta = secrets.choice(lista_palabras)
LONGITUD = int(5)
INTENTOS = int(5)
adivinado = False
resultados = []  #para quese vea la colocacion final de los cuadritos
contador=0

print("=================== WORDLE ======================")
print("             ¡Bienvenido a Wordle!")
print("           Adivina la palabra secreta.")
print("          La palabra tiene 5 letras.")
print("=================================================")

while contador < INTENTOS and not adivinado:
    print(f"Estas en el intento {contador} de 5")
    print("Escriba la palabra:")
    palabra = input().upper()
    
    #Validamos para saber la longitud
    if len(palabra) != LONGITUD:
        print("La palabra tiene que tener 5 letras")
        continue
    #Validar que solo se escriben  letras
    if not palabra.isalpha():
        print("Escribe solo LETRAS")
        continue
    
    contador+=1    
    
    #Mostrar de forma visual los cuadraditos    
    resultado_cuadraditos= verficar_letras(palabra_secreta,palabra)
    resultado_junto = " ".join(resultado_cuadraditos)# para juntar y que se vea un espacio por cada cuadradito
    print(f"Resultado: {resultado_junto}")
    
    resultados.append(resultado_junto) #Para meter cada linea de cuadritos en el resultado final
    
    #Comprobacion
    if palabra == palabra_secreta:
        adivinado = True
        

print("=================== WORDLE ======================")
print("                                                 ")
print("               FIN DE LA PARTIDA")
print("                                                 ")
print("=================================================")
if adivinado == True:
    print("¡¡¡ FELICIDADES HAS ADIVINADO LA PALABRA !!!")
else:
    print(" ¡¡ Te has quedado sin intentos !!")
print("")
print(f"La palabra secreta era: {palabra_secreta}")
print("Tú resultado: ")
for linea in resultados:
    print(linea)
