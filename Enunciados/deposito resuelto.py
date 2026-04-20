while True:
        entrada_usuario = input("Ingrese la cantidad de productos que llegaron: ")
        try:
            cantidad_real = int(entrada_usuario)
            if cantidad_real < 0:
                print("La cantidad no puede ser negativa.")
                continue
            if cantidad_real == 0:
                print("Cantidad: 0 unidades, no se reserva nada.")
                break
            residuo = cantidad_real % 100
            if residuo == 0:
                espacio_necesario = cantidad_real
            else:
                centenas_completas = cantidad_real // 100
                espacio_necesario = (centenas_completas + 1) * 100
            print(f"Cantidad de productos: {cantidad_real}")
            print(f"Espacio a reservar: {espacio_necesario}")
            break
        except ValueError:
            print("Entrada inválida. Por favor, use solo números enteros.")