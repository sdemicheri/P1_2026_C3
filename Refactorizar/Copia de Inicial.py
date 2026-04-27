opcion = 0
saldo = 10000

while opcion != 4:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("\nSu saldo actual es: $", saldo)

        elif opcion == 2:
            print("\nPromociones disponibles:")
            print("- 2x1 en recargas")
            print("- 30% de descuento en datos móviles")

        elif opcion == 3:
            try:
                monto = int(input("Ingrese monto a recargar: "))
                saldo = saldo + monto
                print("Recarga exitosa. Nuevo saldo: $", saldo)
            except ValueError:
                print("Ingrese un valor valido")
        elif opcion == 4:
            print("\nGracias por comunicarse. ¡Hasta luego!")

        else:
            print("Opción inválida. Intente nuevamente.")
    except ValueError:
        print("Ingrese un valor valido")