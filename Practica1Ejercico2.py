numero = int(input("Ingrese un mumero: "))
print("el numero ingresado es ", numero)
primo = 0
for x in range(1,numero+1):
    print("x",x)
    if numero%x == 0:
        primo+=1
        print("pri",primo)

if primo == 2:
    print("El ", numero, " Es numero primo")

else:
    print("El ", numero, " NO numero primo")

