# Realizado por Miguel Ángel Bernal Sánchez

#InfoEquipos(datosliga,equipos): Función que recibe la lista de diccionarios con los datos de la liga y el conjunto de equipos y devuelve una lista de tuplas, 
# en cada tupla se guarda un equipo con los partidos ganados, empatados y perdidos y los puntos obtenidos.

def InfoEquipos(datosliga, equipos):
    
    # Dentro de esta lista se almacenarán las tuplas que serán creadas en esta función
    infoEquipos = []

    # Le he querido añadir un encabezado, no queda bien del todo pero siempre se puede comentar esta linea u eliminarla.
    infoEquipos.append(("Equipo", "Partidos Ganados", "Partidos Empatados", "Partidos Perdidos"))

    # Le asignamos a cada equipo contadores de los partidos ganados, empatados y partidos perdidos
    for iEquipo in equipos:
        partGanados = 0
        partEmpatado = 0
        partPerdido = 0
    
        for iPartido in datosliga:
            local = iPartido["local"]
            visitante = iPartido["visitante"]
            golesLocal = iPartido["golesLocales"]
            golesVisitante = iPartido["golesVisitante"]

            if local == iEquipo:
                if golesLocal > golesVisitante:
                    partGanados += 1
                elif golesLocal == golesVisitante:
                    partEmpatado += 1
                else:
                    partPerdido += 1
            
            elif visitante == iEquipo:
                if golesVisitante > golesLocal:
                    partGanados += 1
                elif golesVisitante == golesLocal:
                    partEmpatado += 1
                else:
                    partPerdido += 1

        # Almacenamos los datos en una tupla y los agregamos a la lista de infoEquipos
        infoEquipos.append((iEquipo, partGanados, partEmpatado, partPerdido))

    return infoEquipos





