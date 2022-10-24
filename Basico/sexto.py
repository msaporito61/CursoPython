#!/usr/bin/env python3

for numero in range(2,10):
    for y in range(2, numero):
        if numero % y == 0:
            print(numero, " es igual ", y, '*', numero//y)
            break
        elif y+1 == numero:
            print(numero, "es primo")