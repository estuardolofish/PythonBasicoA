nombre = str(input("Ingrese su nombre: "))
genero = str(input("Ingrese su sexo(M o H): "))

if genero == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"

print("El grupo al que corresponde es: ", grupo)