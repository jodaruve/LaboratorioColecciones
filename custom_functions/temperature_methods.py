def average (list):
    sum = 0
    for temp in list:
        sum = sum + temp

    prom = sum / len(list)

    return prom


def positions (posicion):
    if posicion == 0:
        mes_posicion = "Enero"
    elif posicion == 1:
        mes_posicion = "Febrero"
    elif posicion == 2:
        mes_posicion = "Marzo"
    elif posicion == 3:
        mes_posicion = "Abril"
    elif posicion == 4:
        mes_posicion = "Mayo"
    elif posicion == 5:
        mes_posicion = "Junio"
    elif posicion == 6:
        mes_posicion = "Julio"
    elif posicion == 7:
        mes_posicion = "Agosto"
    elif posicion == 8:
        mes_posicion = "Septiembre"
    elif posicion == 9:
        mes_posicion = "Octubre"
    elif posicion == 10:
        mes_posicion = "Noviembre"
    else:
        mes_posicion = "Dicioembre"

    return mes_posicion
