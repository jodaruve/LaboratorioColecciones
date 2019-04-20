"""
Laboratory solution
"""
import statistics as stats
from custom_functions import temperature_methods

guajira = []
santander = []
narigno = []
try:

    for i in range(0, 12):
        temperature = int(input("Por favor ingrese la temperatura {} del departamento de Guajira ".format(i+1)))
        guajira.append(temperature)

    print("")
    for i in range(0, 12):
        temperature = int(input("Por favor ingrese la temperatura {} del departamento de Santander ".format(i+1)))
        santander.append(temperature)

    print("")
    for i in range(0, 12):
        temperature = int(input("Por favor ingrese la temperatura {} del departamento de Narigno ".format(i+1)))
        narigno.append(temperature)

    print("")

    guajira_average = temperature_methods.average(guajira)
    print("--> El promedio de la temperatura del departamento de la guajira fue:", guajira_average)
    santander_average = temperature_methods.average(santander)
    print("--> El promedio de la temperatura del departamento de Santander fue:", santander_average)
    narigno_average = temperature_methods.average(narigno)
    print("--> El promedio de la temperatura del departamento de Narigno fue:", narigno_average)

    if guajira_average == santander_average and guajira_average == narigno_average:
        print("--> Las temperaturas de los tres departamentos son iguales")
    elif guajira_average == santander_average:
        print("--> Los promedios de las temperaturas del departamento de la guajira y santander son iguales")
    elif guajira_average == narigno_average:
        print("--> Los promedios de las temperaturas del departamento de la guajira y narigno son iguales")
    elif santander_average == narigno_average:
        print("--> Los promedios de las temperaturas del departamento de santander y narigno son iguales")
    elif guajira_average > santander_average and guajira_average > narigno_average:
        print("--> El mayor promedio de las temperaturas fue el del departamento de La guajira")
    elif santander_average > narigno_average:
        print("--> El mayor promedio de las temperaturas fue el del departamento de Santander")
    else:
        print("--> El mayor promedio de las temperaturas fue el del departamento de Narigno")

    list_sum = [guajira_average, santander_average, narigno_average]
    national_average = temperature_methods.average(list_sum)
    print("--> El promedio nacional es: ", national_average)

    max_temp_guajira = max(guajira)
    max_temp_santander = max(santander)
    max_temp_narigno = max(narigno)

    position_guajira = guajira.index(max_temp_guajira)
    position_santander = santander.index(max_temp_santander)
    position_narigno = narigno.index(max_temp_narigno)

    position_month_guajira = temperature_methods.positions(position_guajira)
    print("--> El mes mas caliente en el departamento de La guajira fue", position_month_guajira, "con una temperatura de ", max_temp_guajira)
    position_month_santander = temperature_methods.positions(position_santander)
    print("--> El mes mas caliente en el departamento de Santander fue", position_month_santander, "con una temperatura de ", max_temp_santander)
    position_month_narigno = temperature_methods.positions(position_narigno)
    print("--> El mes mas caliente en el departamento de Narigno fue", position_month_narigno, "con una temperatura de ", max_temp_narigno)

    max_list_months = [max_temp_guajira, max_temp_santander, max_temp_narigno]
    max_average_months = temperature_methods.average(max_list_months)
    print("--> El promedio de las temperaturas maximas de los tres meses es {}".format(max_average_months))

    max_temperature = max(max_list_months)
    state_position = max_list_months.index(max_temperature)
    if state_position == 0:
        state = "La guajira"
    elif state_position == 1:
        state = "Santander"
    else:
        state = "Narigno"

    max_average = max(list_sum)
    print("--> El promdeio mas caliente fue {} y se presento en el departamento de {}".format(max_average, state))

    print("--> La temperatura mas caliente fue {} y se presento en el departamento de {}".format(max_temperature, state))

    deviation_guajira = (stats.pstdev(guajira))
    print("--> La desviacion estandar del departamento de La guajira es: ", deviation_guajira)
    deviation_santander = (stats.pstdev(santander))
    print("--> La desviacion estandar del departamento de Santander es: ", deviation_santander)
    deviation_narigno = (stats.pstdev(narigno))
    print("--> La desviacion estandar del departamento de Narigno es: ", deviation_narigno)
except:
    print("Valor incorrecto. Por favor intentelo nuevamente")



