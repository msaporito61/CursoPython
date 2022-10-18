def potencia(n):
    """
    Esta es la documentacion correspondiente

    algo mas???
    """
    return n * n

def desayuno(cafe: str, pan: str = "frances") -> str:
    print("Anotaciones:", desayuno.__annotations__ )
    print("Argumentos:", cafe, pan)
    return cafe + ' y ' + pan

print(potencia(5))
print(potencia.__doc__)
print(desayuno("Colombiano","Salvado"))