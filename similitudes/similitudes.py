import Levenshtein

# Ejemplo de dos nombres
nombre1 = "Keny"
nombre2 = "Keni"

# Calcular la distancia de Levenshtein entre los dos nombres
distancia = Levenshtein.distance(nombre1.lower(), nombre2.lower())

# Calcular la similitud normalizada entre los dos nombres
longitud_maxima = max(len(nombre1), len(nombre2))
similitud_normalizada = (longitud_maxima - distancia) / longitud_maxima

print("Distancia de Levenshtein:", distancia)
print("Similitud normalizada:", similitud_normalizada)
