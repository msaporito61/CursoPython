#!/usr/bin/env python3



class Mago:
    
    def __init__(self, nombre) -> None:
        self.nombre = nombre 
        self.trucos=[]
        self.nacionalidad=''
        self.__interno=''

    def agregar_truco(self, truco):
        self.trucos.append(truco)

    def __str__(self) -> str:
        return f'El mago {self.nombre} es {self.nacionalidad}'

class Ilusionista(Mago):
    def __str__(self) -> str:
        return f'El Ilusionista {self.nombre}'


if __name__ == '__main__':
    mandrake = Mago('Mandrake')
    mandrake.nacionalidad='Chino'
    sindientes= Mago('Sin Dientes')
    fumanchu=Ilusionista('Fu ManChu')
    mandrake.agregar_truco('Sacar Conejo de Galera')
    
    sindientes.agregar_truco('Adivinar el naipe')
    print(mandrake.trucos)
    print(mandrake, mandrake.trucos)
    print(fumanchu)