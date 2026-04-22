def main():
    print("Bienvenido a Personal. Seleccione una opción:")
    while True:
        print("1. Ver promociones")
        print("2. Calcular descuento en abono actual")
        print("3. Simular cambio de plan")
        print("0. Salir")
        opcion = input("Ingrese opción: ")
        if opcion == "1":
            print("Promociones disponibles:")
            print("- Descuento del 20% en abonos por permanencia mayor a 6 meses")
            print("- Paquete de 10GB adicionales por $5")
            print("- Beneficio: llamadas ilimitadas los fines de semana")
        elif opcion == "2":
            try:
                abono = float(input("Ingrese su abono mensual actual: "))
                descuento = abono * 0.15
                nuevo = abono - descuento
                print(f"El nuevo monto con 15% de descuento es: ${nuevo:.2f}")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
        elif opcion == "3":
            try:
                nuevo_abono = float(input("Ingrese el valor del nuevo plan: "))
                descuento = nuevo_abono * 0.25
                final = nuevo_abono - descuento
                print(f"El costo final estimado con 25% de descuento de bienvenida es: ${final:.2f}")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
        elif opcion == "0":
            print("Gracias por llamar a Personal. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()