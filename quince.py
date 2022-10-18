cuadrados = []
for n in range(10):
    cuadrados.append(n**2)
print(cuadrados)

cuadrados2 = map(lambda n: n**2, range(10))
print(cuadrados2)

cuadrados3 = [n**2 for n in range(10)]
print(cuadrados3)