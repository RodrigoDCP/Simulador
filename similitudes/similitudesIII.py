import os
import json
import Levenshtein

# Cargar la semilla desde el archivo JSON
with open('semilla.json', 'r') as semilla_file:
    semilla = json.load(semilla_file)

# Obtener la lista de archivos en el directorio actual
lista_archivos = os.listdir()

# Filtrar solo los archivos que siguen el formato "arcoX.json"
arcos = [archivo for archivo in lista_archivos if archivo.startswith('arco') and archivo.endswith('.json')]

# Calcular y mostrar las similitudes normalizadas
for arco_nombre in arcos:
    with open(arco_nombre, 'r') as arco_file:
        arco = json.load(arco_file)
    
    distancia = Levenshtein.distance(semilla["firstName"].lower(), arco["firstName"].lower())
    longitud_maxima = max(len(semilla["firstName"]), len(arco["firstName"]))
    similitud_normalizada = (longitud_maxima - distancia) / longitud_maxima
    print(f"Similitud normalizada entre semilla y {arco_nombre}: {similitud_normalizada}")
