try:
    producto=int(input("cantidad actual de productos: "))
    if producto >0:
        centena=((producto//100)+1)
        print("centenas completas: ", centena)
    else:
        print("Ingrese un numero mayor a 0")
except ValueError:
    print("ingrese un dato valido")