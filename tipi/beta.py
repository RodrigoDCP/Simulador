import Levenshtein

str1 = "gato"
str2 = "gate"

distance = Levenshtein.distance(str1, str2)
print("La distancia de Levenshtein entre '{}' y '{}' es: {}".format(str1, str2, distance))
