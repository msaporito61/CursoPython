anio = 2022
evento = "Mundial"
votos_si = 30_126_234
votos_no = 3_123_456
porcentaje = votos_si /(votos_si+votos_no)
# texto = evento + str(anio)
texto = f'El año {anio} es {evento} '
texto2 = '{:+9} Si {:2.2%}'.format(votos_si, porcentaje)
print(texto2, porcentaje)