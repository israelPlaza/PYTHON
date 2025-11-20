
rol = input("Escriba ek rol [admin, editor, otros.. :]").lower()

if rol =="admin" :
    print("Acceso total.")
elif rol == "editor" :
    print("Acceso limitado.")
else:
    print("Acceso denegado.")