
opcion = 0
saldo = 10000
SALDO_USADO = 3000

while opcion != 5:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. consultar saldo gastado")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("\nSu saldo actual es: $", saldo)

    elif opcion == 2:
        print("\nPromociones disponibles:")
        print("- 2x1 en recargas")
        print("- 30% de descuento en datos móviles")

    elif opcion == 3:

            monto = int(input("Ingrese monto a recargar: "))

            saldo = saldo + monto
            print("Recarga exitosa. Nuevo saldo: $", saldo)

    elif opcion == 4:
        print("saldo utilizado hasta el momento $", SALDO_USADO)

    elif opcion == 5:
        print("\nGracias por comunicarse. ¡Hasta luego!, sus interracciones fueron")

    else:
        print("Opción inválida. Intente nuevamente.")
