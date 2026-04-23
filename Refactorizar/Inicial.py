opcion = 0
saldo = 10000
DATOS_CONSUMIDOS = 30
interacciones = 0
recargas = 0

while opcion != 5:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. Consultar datos consumidos")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("\nSu saldo actual es: $", saldo)
        interacciones = interacciones + 1

    elif opcion == 2:
        print("\nPromociones disponibles:")
        print("- 2x1 en recargas")
        print("- 30% de descuento en datos móviles")
        interacciones = interacciones + 1
        
    elif opcion == 3:
        recargas = recargas + 1
        if recargas < 3:
            monto = int(input("Ingrese monto a recargar: "))
            if monto < 0:
                print("Ingrese un monto positivo")
            else:
                saldo = saldo + monto
            print("Recarga exitosa. Nuevo saldo: $", saldo)
            interacciones = interacciones + 1
        else:
            print("Cantidad de recargas superadas")
            
        
    elif opcion == 4:
        print("\nDatos consumidos: ", DATOS_CONSUMIDOS)
        interacciones = interacciones + 1
        
    elif opcion == 5:
        print("\nGracias por comunicarse. ¡Hasta luego!")
        print("Tu cantidad de interacciones fue:", interacciones) 
    
    else:
        print("Opción inválida. Intente nuevamente.")