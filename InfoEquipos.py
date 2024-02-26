# Realizado por Miguel Ángel Bernal Sánchez

#InfoEquipos(datosliga,equipos): Función que recibe la lista de diccionarios con los datos de la liga y el conjunto de equipos y devuelve una lista de tuplas, 
# en cada tupla se guarda un equipo con los partidos ganados, empatados y perdidos y los puntos obtenidos.

def InfoEquipos(datosliga, equipos):
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
    
        for iPartido in datosliga:
            local = iPartido["Team 1"]
            visitante = iPartido["Team 2"]
            resultados= iPartido["FT"]

            if local == iEquipo:
                resultado= qg.QuienGana(resultados)
                if resultado==1:
                    partGanados += 1
                elif resultado==0:
                    partEmpatado += 1
                else:
                    partPerdido += 1
            
            elif visitante == iEquipo:
                resultado= qg.QuienGana(resultados)
                if resultado==1:
                    partGanados += 1
                elif resultado==0:
                    partEmpatado += 1
                else:
                    partPerdido += 1
        # Calculamos los puntos de cada equipo
        info=[iEquipo, partGanados, partEmpatado, partPerdido]
        puntos=p.Puntos(info)
        # Almacenamos los datos en una tupla y los agregamos a la lista de infoEquipos
        infoEquipos.append([iEquipo, partGanados, partEmpatado, partPerdido, puntos])
    
    # Ordenamos la lista según sus puntos saltandonos la primera fila
    infoEquipos=c.Clasificacion(infoEquipos[1:])
    for i in infoEquipos: 
        print(i)