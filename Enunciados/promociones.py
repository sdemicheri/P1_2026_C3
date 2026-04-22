try:
    print("Bienvenido al sistema de promociones")
    print("Opcion 1: listado de promociones disponibles")
    print("Opcion 2: aplicacion de promocion sobre valor actual ")
    print("Opcion 3: cambio de plan ")
    print("opcion 0: Finalizar la llamada")

    opcion=int(input("Ingrese una opcion:"))
    if  (opcion == 1) :
        print("descuentos en abonos\nbeneficios por permanencia\npaquetes de datos adicionales\notros beneficios ")
    elif (opcion == 2):
        valAct=float(input("Ingrese su valor actual de abono mensual: "))
        valDesc=valAct*0.85
        print("el nuevo monto con un descuento del 15% es: $", valDesc)
    elif (opcion == 3):
        valAct=float(input("Ingrese su valor actual de abono mensual: "))
        cambioplan=valAct*0.75
        print("el nuevo plan con un descuento del 25% es: $", cambioplan)
    elif (opcion == 0):
        print("Gracias por comunicarse con nosotros")
    else:
        print("Ingrese una opcion valida")
    print(Repetir)

except ValueError:
    print("Ingrese una opcion valida")



"""
ENTRADA:
opcion: int
valAct: float
PROCESO:
mostrar opciones 
si opcion = 1
mostrar promociones disponibles
si opcion = 2
leer valAct
valDesc=valAct*0.85
mostar valDesc
si opcion = 3
cambiodeplan=valAct*0.75
mostrar cambiodeplan
opcion = 0
mostrar "Gracias por comunicarse con nosotros"
sino
mostrar "Ingrese una opcion valida"
mos
SALIDA:
valDesc
cambiodeplan


"""