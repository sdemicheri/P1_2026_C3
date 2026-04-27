CREDITO_GASTADO = 0
opcion = 0
saldo = 10000
operaciones = 0
cantidad_recargas = 0

while opcion != 6:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. Averiguar Credito Gastado")
    print("5. Verificar operaciones realizadas")
    print("6. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
        match opcion:
            case 1:
                print("\nSu saldo actual es: $", saldo)
            case 2:
                print("\nPromociones disponibles:")
                print("- 2x1 en recargas")
                print("- 30% de descuento en datos móviles")
            case 3:
                if cantidad_recargas < 3:
                    try:
                        monto = int(input("Ingrese monto a recargar: "))
                        if monto > 0:
                            saldo = saldo + monto
                            print("Recarga exitosa. Nuevo saldo: $", saldo)
                            cantidad_recargas += 1
                        else:
                            print("Ingrese un valor positivo")
                    except ValueError:
                        print("Ingrese un valor valido")
                else:
                    print("No se puede realizar mas recargas")
            case 4:
                print("Su credito gastado es: ",  CREDITO_GASTADO)
            case 5:
                print(operaciones)
            case 6:
                print("\nGracias por comunicarse. ¡Hasta luego!")
            case _:
                print("Opcion invalida. Intente nuevamente")
    except ValueError:
        print("Ingrese un valor valido")
    operaciones += 1