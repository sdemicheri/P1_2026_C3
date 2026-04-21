mensaje_bienvenida = "Hola!"
mensaje_despedida = "Chau!"
promociones = "Promociones"
opciones = "1. Promociones, 2. Descuento por promoción, 3. Cambio de plan, 0. Finalizar interacción"
opcion = 0
DESCUENTO_PROMOCION = 15
DESCUENTO_CAMBIO = 25
NUEVO_PLAN = 3000


try:
    print(mensaje_bienvenida)
    while opcion == 0:
        print("Elija una opción:")
        print(opciones)
        opcion = int(input())
        while  opcion < 0 or opcion > 3:
            print("Ingrese una opción válida: ")
            print(opciones)
            opcion = int(input())
        match opcion:
            case 1:
                print(promociones)
                print("--------")
                print("")
                opcion = 0
            case 2:
                valor = float(input("Ingrese el valor actual de su abono: "))
                valor_desc = valor * (100 - DESCUENTO_PROMOCION) / 100
                print("El valor final con el descuento promocional es:", valor_desc)
                print("--------")
                print("")
                opcion = 0
            case 3:
                print("Abono nuevo plan:", NUEVO_PLAN)
                nuevo_plan_desc = 3000 * (100 - DESCUENTO_CAMBIO) / 100
                print("Valor con descuento del 25% de bienvenida:", nuevo_plan_desc)
                print("--------")
                print("")
                opcion = 0
            case 0:
                print(mensaje_despedida)
                break
except ValueError:
    print("Ingrese un caracter válido")