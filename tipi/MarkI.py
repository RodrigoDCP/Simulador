import Levenshtein
import random

def generar_errores_similitud(dato_original, num_variantes, umbral_distancia):
    variantes = set()
    while len(variantes) < num_variantes:
        palabra = dato_original
        for _ in range(random.randint(1, umbral_distancia)):
            # Simular errores de similitud
            indice = random.randint(0, len(palabra) - 1)
            nueva_letra = chr(random.randint(97, 122))  # Generar una letra aleatoria
            palabra = palabra[:indice] + nueva_letra + palabra[indice+1:]
        if palabra != dato_original:
            variantes.add(palabra)
    return variantes

# Ejemplo de uso
dato_original = "Keny Alexander"
num_variantes = 10
umbral_distancia = 1

variantes = generar_errores_similitud(dato_original, num_variantes, umbral_distancia)
print("Dato original:", dato_original)
print("Variantes con errores de similitud:")
for variante in variantes:
    print(variante)
