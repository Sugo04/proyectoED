# Realizado por Héctor Martín Ortega 

#  Función que lee el fichero CSV y devuelve los datos del mismo en una lista de diccionarios.

# importamos la libreria que nos permitirá trabajar con el archivo CSV

import csv

def leerEquipos():
    # Crearemos una lista liga antes de realizar un try catch que se encargue de comprobar que el archivo exista, si no existe nos avisa de que no existe
    liga=[]
    try:
        # abrimos el fichero csv y rellenamos el reader con diccionarios a través del DictReader
        with open('liga.csv') as file:
            # Aquí en el reader me la he jugado un poco al poer el DictReader como si fuera la version de lectura del DictWriter (ha colao) 
            # lo cual considero que puede ser una manera muy eficiente de leer los archivos como diccionarios directamente
            csv_reader = csv.DictReader(file , delimiter=',')
            
            # Nos saltamos la primera línea para sacarla de la ordenación (Mis ganas de comentar todo lo que hago JAJAJAJ)
            next(csv_reader)
            
            # recorremos todo el lector y agregamos en la lista cada diccionario con una variable lista que es la que recorre nuestro fichero csv
            for fila in csv_reader:
                liga.append(fila)       

        return liga
    
    except FileNotFoundError:
        print('No existe el fichero en la ruta especificada')
    