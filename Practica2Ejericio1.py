contrasenia = "Contraseña"
contra = str(input("Ingrese la Contraseña: "))
print("la contraseña ingresada es:  ", contra)

if contra.lower() == contrasenia.lower():
    print("Contraseña Correcta")
else:
    print("Contraseña Incorrecta")