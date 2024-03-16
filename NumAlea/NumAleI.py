import random

def generar_variantes_numero_telefonico(numero_original, num_variantes, umbral_distancia):
    """
    Esta función genera variantes de un número telefónico modificando los últimos 7 dígitos,
    dejando intacta la lada.

    :param numero_original: El número telefónico original.
    :param num_variantes: El número de variantes a generar.
    :param umbral_distancia: La distancia máxima permitida para la generación de errores.
    :return: Un conjunto de variantes del número telefónico.
    """
    variantes = set()
    lada = numero_original[:3]  # Extraemos la lada
    digitos_restantes = numero_original[3:]  # Extraemos los últimos 7 dígitos

    while len(variantes) < num_variantes:
        nuevo_numero = lada  # Comenzamos con la lada del número original
        for i in range(7):
            # Generamos un nuevo dígito aleatorio
            nuevo_digito = str(random.randint(0, 9))
            nuevo_numero += nuevo_digito

        # Agregamos la nueva variante a la lista, asegurándonos de que sea diferente al número original
        if nuevo_numero != numero_original:
            variantes.add(nuevo_numero)

    return variantes

# Ejemplo de uso
numero_original = "5551234567"
num_variantes = 10
umbral_distancia = 1

variantes = generar_variantes_numero_telefonico(numero_original, num_variantes, umbral_distancia)
print("Número original:", numero_original)
print("Variantes con errores en los últimos 7 dígitos:")
for variante in variantes:
    print(variante)
