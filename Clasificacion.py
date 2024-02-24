# Realizado por Héctor Martín Ortega 
#
#  Función que recibe la lista generada con la función anterior y la ordena según el número de puntos.

def Clasificacion (datos):
    datos.sort(reverse=True)
    print("Lista ordenada")
    return datos