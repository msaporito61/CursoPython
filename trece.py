def opciones(tipo, *arguments, **keywords):
    print("Tipo ", tipo)
    for arg in arguments:
        print(arg)
    print("-" * 50)
    for kw in keywords:
        print(kw, ":", keywords[kw])


opciones("Oficina", "Sistemas",  "Desarrollo conatble", "IBM",
            gerente="Jose Perez",
            empleado="Juan Sanchez",
            cadete="Cacho",
            secretaria="Wanda Nara",
            encargado="Kiko")

# def f(pos1, pos2, /, pos_o_kwd, *, kwd1, kwd2, kwdn ):