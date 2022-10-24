#!/usr/bin/env python3
# Serie Fibonacci
def fib(n):
    resultado = []
    x, y = 0, 1
    while x < n:
        resultado.append(x)
        x, y = y, x+y
    return resultado

x = int(input("Ingrese un entero: "))
# y = fib(x)
# print(type(y))
print(fib(x),type(fib(x)))