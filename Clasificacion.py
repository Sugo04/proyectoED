# Realizado por Héctor Martín Ortega 
#
#  Función que recibe la lista generada con la función anterior y la ordena según el número de puntos.

def Clasificacion (datos):
    datos.sort(key=lambda x: x[4],reverse=True)
    print("Lista ordenada")
    return datos