print("Bienvenido al cálculo de la media de sus notas")
acumulado=0
media=0
notaAcu=1
nota=input("cual es su nota?: ")
notaInt=int(nota)

nvoRegistro=input("quiere introducir una nueva nota?: si/no?")
nvoRegBool=bool(nvoRegistro)
print(nvoRegBool)

if nvoRegBool == True:
    notaAcu=+1
    acumulado= (acumulado + notaInt)
    media=(acumulado/notaAcu)
    print("media parcial: ", media)
    nvoRegistro=input("quiere introducir una nueva nota?: si/no?")
    nvoRegBool=bool(nvoRegistro)
else:
    print("media es igual a:", media)

