#Función que recibe la lista de diccionarios con los datos de la liga y devuelve un conjunto con los equipos de la liga.

def Equipos(datosLiga):
    #Creamos una lista vacía.
    equipos = []
    #Recorremos datosLiga y vamos añadiendo los nombres de los equipos si no estaban ya añadidos.
    for partido in datosLiga:
        if partido["Team 1"] not in equipos:
            equipos.append(partido["Team 1"])
        if partido["Team 2"] not in equipos:
            equipos.append(partido["Team 2"])
    return equipos
#Finalmente devolvemos la lista llena.
