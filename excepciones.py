while True:
    try:
        x = int(input("Numero.: "))
        print(x)
        break
    except ValueError:
        print("Error de valor... intente nuevamente")

try:
    f = open('trabajo.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OSError: {0}", err)
except ValueError:
    print("Los datos no son enteros")
except BaseException as err:
    print(f"Inesperado {err=}, {type(err)=}")
    raise 
else:
    print('Valor.:', i)