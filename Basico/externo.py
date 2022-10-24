#!/usr/bin/env python3
import sys
import argparse

def fib(n):
    resultado = []
    x, y = 0, 1
    while x < n:
        resultado.append(x)
        x, y = y, x+y
    return resultado

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='externo', 
        description='Programa de Fibonacci con argumentos')
    parser.add_argument('-n', '--number', type=int)
    parser.add_argument('-r', '--repetion', type=int)
    args = parser.parse_args()
    try:
        print(sys.argv)
        numero = int(args.number)
        print(fib(numero))
        print(args.repetion)
    except ValueError as e:
        print('Error de valor')