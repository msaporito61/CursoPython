#!/usr/bin/env python3
# Serie Fibonacci
def fib(n):
    x, y = 0, 1
    while x < n:
        print(x, end=' ')
        x, y = y, x+y

x = int(input("Ingrese un entero: "))
