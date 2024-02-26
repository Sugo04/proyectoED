# Realizado por Miguel Ángel Bernal Sánchez

#InfoEquipos(datosliga,equipos): Función que recibe la lista de diccionarios con los datos de la liga y el conjunto de equipos y devuelve una lista de tuplas, 
# en cada tupla se guarda un equipo con los partidos ganados, empatados y perdidos y los puntos obtenidos.

def InfoEquipos(datosliga, equipos):
    #Importamos las demás funciones y le aplicamos un alias a cada una
    import QuienGana as qg
    import Puntos as p
    import Clasificacion as c
    
    # Dentro de esta lista se almacenarán las tuplas que serán creadas en esta función
    infoEquipos = []

    # # Le he querido añadir un encabezado, no queda bien del todo pero siempre se puede comentar esta linea u eliminarla.
    # infoEquipos.append(("Equipo", "Partidos Ganados", "Partidos Empatados", "Partidos Perdidos", "Puntos"))

    # Le asignamos a cada equipo contadores de los partidos ganados, empatados y partidos perdidos
    for iEquipo in equipos:
        partGanados = 0
        partEmpatado = 0
        partPerdido = 0

        # Recorremos los datos de la liga
        for iPartido in datosliga:
            local = iPartido["Team 1"]
            visitante = iPartido["Team 2"]
            resultados= iPartido["FT"]

            # Verificamos si el equipo estaba jugando como local, de no ser así
            # será identificado como visitante
            if local == iEquipo:
                # Verificamos el resultado del partido y sumamos +1 en el contador correspondiente
                resultado= qg.QuienGana(resultados)
                if resultado==1:
                    partGanados += 1
                elif resultado==0:
                    partEmpatado += 1
                else:
                    partPerdido += 1
            
            elif visitante == iEquipo:
                # Verificamos el resultado del partido y sumamos +1 en el contador correspondiente
                resultado= qg.QuienGana(resultados)
                if resultado==1:
                    partGanados += 1
                elif resultado==0:
                    partEmpatado += 1
                else:
                    partPerdido += 1

        # Calculamos los puntos de cada equipo, para ello accedemos a la funcion Puntos
        info=[iEquipo, partGanados, partEmpatado, partPerdido]
        puntos=p.Puntos(info)
        # Almacenamos los datos en una tupla y los agregamos a la lista de infoEquipos
        infoEquipos.append([iEquipo, partGanados, partEmpatado, partPerdido, puntos])
    
    # Ordenamos la lista según sus puntos saltandonos la primera fila, debemos utilizar la funcion CLasificacion
    infoEquipos=c.Clasificacion(infoEquipos[1:])
    
    # Devolvemos los resultados en pantalla
    return infoEquipos