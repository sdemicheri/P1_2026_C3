try:
    cantidad = int(input("Ingrese la cantidad "))
    resto = cantidad % 100
    cent_sup = cantidad - resto + 100
    print("La centena inmediata superior es:", cent_sup)
except ValueError:
    print("Ingrese un valor válido")