#!/usr/bin/env python3

class MiClase:
    def __init__(self, entero=0) -> None:
        self.valor = entero 

    def metodo(self):
        return "Metodo de mi clase"

if __name__ == '__main__':
    c = MiClase()
    print(type(c))
    print(c.valor)
    print(c.metodo())
    c.valor=9876
    print(c.valor)
    c.contador = 1
    while c.contador < 10:
        c.contador = c.contador*2
    print(c.contador)
    del c.contador