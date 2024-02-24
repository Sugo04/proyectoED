# Realizado por Héctor Martín Ortega 
#
#  Función que recibe la lista generada con la función anterior y la ordena según el número de puntos.

def Clasificacion (datos):
    # Ordenamos la lista a partir de la cantidad de puntos obtenidos los cuales se encuentran en 4ª posición. 
    datos.sort(key=lambda x: x[4],reverse=True)
    return datos