# Realizado por Miguel Ángel Bernal Sánchez

#Puntos(info): Función que recibe una lista con los partidos ganados, 
#empatados y perdidos y devuelve los puntos obtenidos.

def Puntos(info):
    puntos_por_equipo = []
    # Utilizo [1:] para que comience desde la segunda fila, ya que sino escribirá la cabecera
    # Recorremos cada equipo obtenida de la función InfoEquipos
    for equipo_info in info[1:]:
        partGanados = equipo_info[1]   # Aquí tomamos el número de partidos ganados
        partEmpatado = equipo_info[2]   # Aquí tomamos el número de partidos empatados
        puntos = partGanados * 3 + partEmpatado  # Calculamos los puntos
        puntos_por_equipo.append(puntos)
    return puntos_por_equipo

