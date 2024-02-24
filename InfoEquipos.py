# Realizado por Miguel Ángel Bernal Sánchez

#InfoEquipos(datosliga,equipos): Función que recibe la lista de diccionarios con los datos de la liga y el conjunto de equipos y devuelve una lista de tuplas, 
# en cada tupla se guarda un equipo con los partidos ganados, empatados y perdidos y los puntos obtenidos.

def InfoEquipos(datosliga, equipos):
    
    # Dentro de esta lista se almacenarán las tuplas que serán creadas en esta función
    infoEquipos=[]

    #Le he querido añadir un encabezado, no queda bien del todo pero siempre se puede comentar esta linea u eliminarla.
    infoEquipos.append(("Equipo", "Partidos Ganados", "Partidos Empatados", "Partidos Perdidos", "Puntos"))

    # Le asignamos a cada equipo contadores de los partidos ganados, empatados, pertidos y sus puntos por defecto
    # que será 0 en todos, básicamente, ya a partir de aquí vamos sumando dependiendo de los resultados
    # de los datos de la liga (están en el diccionario datosliga).
    for iEquipo in equipos:
        partGanados=0
        partEmpatado=0
        partPerdido=0
        puntos=0
    
        for iPartido in datosliga:
            # Dependiendo de cómo estén nombradas las claves del diccionario datosliga se
            # deberá cambiar las claves de este bucle for. Estos nombres son provisionales

            local=iPartido["local"]
            visitante=iPartido["visitante"]
            golesLocal=iPartido["golesLocales"]
            golesVisitante=iPartido["golesVisitante"]

            # Aquí, dependiendo de si el equipo en que se encuentra el bucle es local o no,
            # entonces deberemos hacer una comparación u otra para comenzar a asignar valores
            # a los contadores
            if local == iEquipo:
                if golesLocal > golesVisitante:
                    partGanados += 1
                    puntos += 3
                elif golesLocal == golesVisitante:
                    partEmpatado += 1
                    puntos += 1
                else:
                    partPerdido += 1
            
            elif visitante == iEquipo:
                if golesVisitante > golesLocal:
                    partGanados += 1
                    puntos += 3
                elif golesVisitante == golesLocal:
                    partEmpatado += 1
                    puntos += 1
                else:
                    partPerdido += 1

        # Aquí una vez se hayan sumado los resultados correspondientes a los contadores estos serán
        # almacenados en una tupla, así hasta que finalice con todos los datos
        infoEquipos.append((iEquipo, partGanados, partEmpatado, partPerdido, puntos))

    return infoEquipos





