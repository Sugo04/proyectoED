# Realizado por Miguel Ángel Bernal Sánchez

#Puntos(info): Función que recibe una lista con los partidos ganados, 
#empatados y perdidos y devuelve los puntos obtenidos.

def Puntos(info):

    partGanados = info[1]   # Aquí tomamos el número de partidos ganados
    partEmpatado = info[2]   # Aquí tomamos el número de partidos empatados
    puntos = partGanados * 3 + partEmpatado  # Calculamos los puntos
    return puntos

