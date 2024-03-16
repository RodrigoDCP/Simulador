import random

def generar_errores_similitud(dato_original, num_variantes, umbral_distancia):
    variantes = set()
    while len(variantes) < num_variantes:
        palabra = dato_original[:-4]  # Tomar todos los caracteres excepto los últimos 4
        ultimos_cuatro = dato_original[-4:]  # Tomar los últimos 4 caracteres
        for _ in range(random.randint(1, umbral_distancia)):
            # Simular errores de similitud solo en los últimos 4 caracteres
            indice = random.randint(0, 3)
            nueva_letra = chr(random.randint(97, 122))  # Generar una letra aleatoria
            ultimos_cuatro = ultimos_cuatro[:indice] + nueva_letra + ultimos_cuatro[indice+1:]
        palabra += ultimos_cuatro
        if palabra != dato_original:
            variantes.add(palabra)
    return variantes

# Ejemplo de uso
dato_original = "123456789"
num_variantes = 10
umbral_distancia = 4

variantes = generar_errores_similitud(dato_original, num_variantes, umbral_distancia)
print("Dato original:", dato_original)
print("Variantes con errores de similitud:")
for variante in variantes:
    print(variante)
