#Función que recibe un resultado y devuelve un 0 si es un empate, un 1 si gana el equipo de casa y -1 si gana el equipo visitante.

def QuienGana(resultado):
    #Separamos el primer valor de la lista del segundo con el guion
    #Presuponemos que son enteros los valores, si no, habría que hacer un casting a int
    goles1 = resultado.split("-")[0]
    goles2 = resultado.split("-")[1]
    if goles1 > goles2:
        return 1
    elif goles1 == goles2:
        return 0
    else:
        return -1
