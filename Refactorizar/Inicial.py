opcion = 0
saldo = 10000
consumido = 500
i=0

while opcion != 5:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. Mostrar datos consumidos")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("\nSu saldo actual es: $", saldo)

    elif opcion == 2:
        print("\nPromociones disponibles:")
        print("- 2x1 en recargas")
        print("- 30% de descuento en datos móviles")

    elif opcion == 3:
        if i >= 3:
            print("No podés hacer más recargas")
        else:
            recarga=1
            while i < 3 and recarga == 1:
                monto = int(input("Ingrese monto a recargar: "))
                while monto < 0:
                    monto = int(input("Ingrese un monto válido: "))
                saldo+=monto
                i+=1
                print("Recarga exitosa. Nuevo saldo: $", saldo)
                if i==1:
                    recarga = int(input("Te quedan 2 recargas. Presiona 1 para cargar de nuevo, 2 para volver al menú: "))
                elif i==2:
                    recarga = int(input("Te queda 1 recargas. Presiona 1 para cargar de nuevo, 2 para volver al menú: "))
                else:
                    print("No quedan más recargas")      

    elif opcion == 4:
        print("Consumiste:", consumido)    

    elif opcion == 5:
        print("\nGracias por comunicarse. ¡Hasta luego!")

    else:
        print("Opción inválida. Intente nuevamente.")