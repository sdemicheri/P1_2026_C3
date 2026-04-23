opcion = 0
saldo = 10000
consumo = 0
contador = 0
recargas = 3

while opcion != 4:
    try:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Consultar saldo")
        print("2. Ver promociones")
        print("3. Recargar saldo")
        print("4. Ver consumo de saldo")
        print("5. Salir")

        print("Cantidad de operaciones realizadas: ", contador)

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("\nSu saldo actual es: $", saldo)
            contador += 1

        elif opcion == 2:
            print("\nPromociones disponibles:")
            print("- 2x1 en recargas")
            print("- 30% de descuento en datos móviles")
            contador +=1

        elif opcion == 3:
            if recargas != 0:
                monto = int(input("Ingrese monto a recargar: "))
                contador += 1
                if monto > 0:
                    saldo = saldo + monto
                    print("Recarga exitosa. Nuevo saldo: $", saldo)
                else:
                    print("Monto no valido")
            else:
                print("ya se acabaron las recargas")
        elif opcion == 4:
            print("\n"
                  "Se ha consumido", consumo, "de saldo")
            contaador += 1
        elif opcion == 5:
            print("\nGracias por comunicarse. ¡Hasta luego!")

    except ValueError:
        print("operacion no valida")
