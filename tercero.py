#!/usr/bin/env python3
x = int(input("Ingrese un entero: "))
if x < 0:
    x = 0
    print("Los numero negativos los cambio a cero")
elif x == 0:
    print("Esto es cero")
elif x > 99:
    print("Es mayor o igual 100")
else:
    print("No es cero ni mayor a cien")
