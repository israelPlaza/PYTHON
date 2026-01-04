def crear_perfil(nombre,**datos_extra):
    print(f"Perfil de {nombre}:")
    for datos in datos_extra.items():
        print(f"- {datos}")
        
crear_perfil("Carlos", edad=25, ciudad="Madrid", repetidor=False)