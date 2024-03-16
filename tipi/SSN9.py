import random

def generar_errores_similitud(dato_original, num_variantes, umbral_distancia):
    variantes = set()
    while len(variantes) < num_variantes:
        palabra = dato_original[:-9]  # Tomar todos los caracteres excepto los últimos 9
        ultimos_nueve = dato_original[-9:]  # Tomar los últimos 9 caracteres
        for _ in range(random.randint(1, umbral_distancia)):
            # Simular errores de similitud solo en los últimos 9 caracteres
            indice = random.randint(0, 8)
            nueva_letra = chr(random.randint(97, 122))  # Generar una letra aleatoria
            ultimos_nueve = ultimos_nueve[:indice] + nueva_letra + ultimos_nueve[indice+1:]
        palabra += ultimos_nueve
        if palabra != dato_original:
            variantes.add(palabra)
    return variantes

# Ejemplo de uso
dato_original = "holamundocomoestasamiguito"
num_variantes = 10
umbral_distancia = 9

variantes = generar_errores_similitud(dato_original, num_variantes, umbral_distancia)
print("Dato original:", dato_original)
print("Variantes con errores de similitud:")
for variante in variantes:
    print(variante)
