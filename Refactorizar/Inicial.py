opcion = 0
saldo = 10000
DATOS=3000
contador=0
recargas=3

while opcion != 5:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. Consuta datos consumidos")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))
    contador+=1

    if opcion == 1:
        print("\nSu saldo actual es: $", saldo)

    elif opcion == 2:
        print("\nPromociones disponibles:")
        print("- 2x1 en recargas")
        print("- 30% de descuento en datos móviles")

    elif opcion == 3:
        if recargas != 0:
            monto = int(input("Ingrese monto a recargar: "))
            while monto < 0:
                print("Ingrese un valor valido")
                monto = int(input("Ingrese monto a recargar: "))            
            saldo = saldo + monto
            print("Recarga exitosa. Nuevo saldo: $", saldo)
            recargas-=1
        else:
            print("Supero la cantidad de recargas disponibles")

    elif opcion == 4:
        print("\nSus datos consumidos son: $", DATOS)

    elif opcion == 5:
        print("\nGracias por comunicarse. ¡Hasta luego!")
        print("Realizaste", contador-1, "operaciones")

    else:
        print("Opción inválida. Intente nuevamente.")