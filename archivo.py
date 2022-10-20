#!/usr/bin/env python3

f = open('archivo.txt', 'a+', encoding="utf-8")
f.seek(0)
archivo= f.read()


print(len(archivo))
#f.write('Agrgado \n')
for linea in archivo:
    print(linea, end='')
f.write('Agrgado Nuevo \n')
f.close()