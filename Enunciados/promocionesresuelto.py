opcion=4
while (opcion != 0 or opcion == 4):
    try:
        print("Bienvenido al sistema de promociones")
        print("Opcion 1: listado de promociones disponibles")
        print("Opcion 2: aplicacion de promocion sobre valor actual ")
        print("Opcion 3: cambio de plan ")
        print("opcion 4: Menu principal")
        print("opcion 0: Finalizar la llamada")

        opcion=int(input("Ingrese una opcion:"))
        while  (opcion == 1) :
            print("1-descuentos en abonos\n2-beneficios por permanencia\n3-paquetes de datos adicionales\n4-otros beneficios ")
            print("ingrese 4 para volver al menu principal")
            print("opcion 0: Finalizar la llamada")
            opcion=int(input("Ingrese una opcion:"))
        while (opcion == 2):
            valAct=float(input("Ingrese su valor actual de abono mensual: "))
            valDesc=valAct*0.85
            print("el nuevo monto con un descuento del 15% es: $", valDesc)
            print("ingrese 4 para volver al menu principal")
            print("opcion 0: Finalizar la llamada")
            opcion=int(input("Ingrese una opcion:"))
        while (opcion == 3):
            valAct=float(input("Ingrese su valor actual de abono mensual: "))
            cambioplan=valAct*0.75
            print("el nuevo plan con un descuento del 25% es: $", cambioplan)
            print("ingrese 4 para volver al menu principal")
            print("opcion 0: Finalizar la llamada")
            opcion=int(input("Ingrese una opcion:"))
        if (opcion == 0):
            print("Gracias por comunicarse con nosotros")
        else:
            print("*"*10,"Ingrese una opcion valida","*"*10)

    except ValueError:
        print("Ingrese una opcion valida")