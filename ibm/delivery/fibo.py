#!/usr/bin/env python3
# # Serie Fibonacci
def fib(n):
    resultado = []
    x, y = 0, 1
    while x < n:
        resultado.append(x)
        x, y = y, x+y
    return resultado

def fib2(n):
    resultado = []
    x, y = 0, 1
    while x < n:
        resultado.append(x)
        x, y = y, x+y
    return resultado

def fib3(n):
    resultado = []
    x, y = 0, 1
    while x < n:
        resultado.append(x)
        x, y = y, x+y
    return resultado


if __name__ == '__main__':
    import sys
    print(fib(int(sys.argv[1])))