# Recibe la lista de diccionarios generado a parir de la función anterior, genera los datos de la clasificación y los imprime por pantalla.
# Esta última función utiliza internamente las siguientes funciones:
# -Equipos(datosliga): Función que recibe la lista de diccionarios con los datos de la liga y devuelve un conjunto con los equipos de la liga.
# -InfoEquipos(datosliga,equipos): Función que recibe la lista de diccionarios con los datos de la liga y el conjunto de equipos y devuelve una
# lista de tuplas, en cada tupla se guarda un equipo con los partidos ganados, empatados y perdidos y los puntos obtenidos.

def impClasificacion(equipos, infoEquipos):
    # Eliminamos la cabecera si viene desde infoEquipos
    if infoEquipos[0][0] == "Equipo":
        infoEquipos = infoEquipos[1:]

    # Ordenamos la lista de equipos por el número de puntos como en el ejercicio de listas
    infoEquipos.sort(key=lambda x: x[4], reverse=True)

    #Imprimimos la nueva cabecera
    print("Posición | Equipo | Ganados | Empatados | Perdidos | Puntos ")
    print("---------|--------|---------|-----------|----------|--------")
    
    #Recorremos el rango de todos los equipos.
    for i in range(len(equipos)):
        equipo = equipos[i]
        print("%2d | %15s | %2d | %2d | %2d | %2d" % (
            i + 1, equipo, infoEquipos[i][1], infoEquipos[i][2], infoEquipos[i][3], infoEquipos[i][4]))

    #He asignado 2 huecos por número y 15 para el nombre, no sé exactamente como queda el formato, pero se puede modificar más adelante.