import Levenshtein

# Semilla
semilla = ["Juan Pérez"]

# Arcos
arcos = [
    ["Juan Pérez"],
    ["Juan Peréz"],
    ["Juan Peérez"],
    ["Juan Péréz"],
    ["Juan Pérezz"],
    ["Juan Perrez"],
    ["Juan Pé rezz"],
    ["Juan Peerez"],
    ["Juan Perézz"],
    ["Juan Peréz"]
]

# Calcular y mostrar las similitudes normalizadas
for i, arco in enumerate(arcos):
    distancia = Levenshtein.distance(semilla[0].lower(), arco[0].lower())
    longitud_maxima = max(len(semilla[0]), len(arco[0]))
    similitud_normalizada = (longitud_maxima - distancia) / longitud_maxima
    print(f"Similitud normalizada entre semilla y arco{i}: {similitud_normalizada}")
