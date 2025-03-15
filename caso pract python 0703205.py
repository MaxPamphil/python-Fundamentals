#Lanche
''' el presente proyecto desarrollado en espanol'
'presenta el servicio de atencion de un lanchonete,'
'en el se muestra un menú y el cliente ordena y'
'solicita la cuenta'''

print("****************************************")
print("bienvenidos al lanchonete virtual\n")
print("menú del día\n")
print("\n")
print("cachorro quente (preço R$ 4.00; cod. 1)")
print("X - salada      (preço R$ 4.50; cod. 2)")
print("X - bacon       (preço R$ 5.00; cod. 3)")
print("torrada simples (preço R$ 2.00; cod. 4)")
print("refrigerante    (preço R$ 1.50; cod. 5)")
print("\n")
NumOrd=0
NumOrd=+1
Rplato=4
print("Realice su orden indicando el código de su plato preferido")
plat=input("ingrese el código, por favor: ")
plato=int(plat)

cant=input("indique cuantos platos de este tipo va a ordenar: ")
cantInt=int(cant)
print("la cantidad de platos pedidos son: " , cant)

if plato == 1:
    print("el precio del plato es: ", Rplato)
    print("el monto del pedido es: ", (Rplato*cantInt))
elif plato == 2:
    print("el precio del plato es: ", (Rplato + 0.5))
    print("el monto del pedido es: ", ((Rplato + 0.50)*cantInt))
elif plato == 3:
    print("el precio del plato es: ", (Rplato + 1.0))
    print("el monto del pedido es: ", ((Rplato + 1.00)*cantInt))
elif plato == 4:
    print("el precio del plato es: ", (Rplato + 2.0))
    print("el monto del pedido es: ", ((Rplato + 2.00)*cantInt))
elif plato == 5:
    print("el precio del plato es: ", (Rplato - 2.5))
    print("el monto del pedido es: ", ((Rplato - 2.50)*cantInt))
else:
    print("el codigo del plato debe estar entre 1 y 5, intente nuevamente..")
print("\n")
print("gracias por preferirnos")
