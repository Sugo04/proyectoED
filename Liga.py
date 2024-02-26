# Ejercicio Liga: realizar un programa en equipo que muestre la tabla de clasificación al final de la liga, 
#       en el que debe aparece el orden que ha quedado cada equipo, los partidos ganados, los empatados y 
#       perdidos, y por último los puntos conseguidos.
#
# Alumnos: Miguel Ángel Bernal, Emilio Neva, Héctor Martín

import LeerPartidos as lp
import InfoEquipos as ie
import Equipos as e

liga=lp.leerEquipos()

equipos=e.Equipos(liga)

ie.InfoEquipos(liga,equipos)