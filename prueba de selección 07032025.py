a= int(input("valor de a?: "))
b= int(input("valor de b?: "))
c= int(input("valor de c?: "))
d= int(input("valor de d?: "))

if b > c:
    if d > a:
        if (c+d) > (a+b):
            if c > 0:
                if d > 0:
                    if a%2 == 0:
                        print("valores aceptados")
                    else:
                        print("Valores NO aceptados, a es impar")
                else:
                    print("Valores NO aceptados, d es negativo")
            else:
                print("Valores NO aceptados, c es negativo")
        else:
            print("Valores NO aceptados, c+d no es mayor q a+b")
    else:
        print("Valores NO aceptados, d no es mayor q a")
else:
    print("Valores NO aceptados, b no es mayor q c")





