import Levenshtein
import random

class GeneradorErroresSimilitud:
    def __init__(self, num_variantes=10, umbral_distancia=1):
        self.num_variantes = num_variantes
        self.umbral_distancia = umbral_distancia

    def generar_errores_similitud(self, dato_original):
        variantes = set()
        while len(variantes) < self.num_variantes:
            palabra = dato_original
            for _ in range(random.randint(1, self.umbral_distancia)):
                # Simular errores de similitud
                indice = random.randint(0, len(palabra) - 1)
                nueva_letra = chr(random.randint(97, 122))  # Generar una letra aleatoria
                palabra = palabra[:indice] + nueva_letra + palabra[indice+1:]
            if palabra != dato_original:
                variantes.add(palabra)
        return variantes

# Ejemplo de uso
if __name__ == "__main__":
    generador = GeneradorErroresSimilitud(num_variantes=10, umbral_distancia=1)
    dato_original = "Alejandro"
    variantes = generador.generar_errores_similitud(dato_original)
    print("Dato original:", dato_original)
    print("Variantes con errores de similitud:")
    for variante in variantes:
        print(variante)
