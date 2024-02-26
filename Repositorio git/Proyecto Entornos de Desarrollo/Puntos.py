# Realizado por Miguel Ángel Bernal Sánchez

#Puntos(info): Función que recibe una lista con los partidos ganados, 
#empatados y perdidos y devuelve los puntos obtenidos.

def Puntos(info):
    # Utilizo [1:] para que comience desde la segunda fila, ya que sino escribirá la cabecera
    # Recorremos cada equipo obtenida de la función InfoEquipos
    for equipo_info in info[1:]:  
        equipo = equipo_info[0]   # Aquí tomamos el nombre del equipo
        partGanados = equipo_info[1]   # Aquí tomamos número de partidos ganados
        partEmpatado = equipo_info[2]   # Aquí tomamos número de partidos empatados
        puntos = partGanados * 3 + partEmpatado  # Aquí tomamos calculamos los puntos
        print(f"{equipo}: {puntos} puntos") # Mostramos en pantalla

