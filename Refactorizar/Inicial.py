
opcion = 0
saldo = 10000
SALDO_USADO = 3000
usos = 0
recarga = 0
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
            if recarga < 3:
                recarga += 1
                monto = int(input("Ingrese monto a recargar: "))
                while monto < 0:
                    print("Ingrese un valor positivo")
                    monto = int(input("Ingrese monto a recargar: "))
                saldo = saldo + monto
                print("Recarga exitosa. Nuevo saldo: $", saldo)
            else:
                print("maximo de recargas alcanzadas")
    elif opcion == 4:
        print("saldo utilizado hasta el momento $", SALDO_USADO)

    elif opcion == 5:
        print("\nGracias por comunicarse. ¡Hasta luego!, sus interracciones fueron", usos)

    else:
        print("Opción inválida. Intente nuevamente.")
    usos += 1