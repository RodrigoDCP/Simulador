import Levenshtein
import random

def generar_errores_similitud(nombre_completo, num_variantes, umbral_distancia):
    variantes = set()
    while len(variantes) < num_variantes:
        partes_nombre = nombre_completo.split()
        nombre = partes_nombre[0]
        apellido_paterno = partes_nombre[1]
        apellido_materno = partes_nombre[2] if len(partes_nombre) > 2 else ""
        segundo_nombre = partes_nombre[3] if len(partes_nombre) > 3 else ""

        # Determina qué parte del nombre se modificará
        parte_modificar = random.choice(["nombre", "apellido_paterno", "apellido_materno", "segundo_nombre"])

        if parte_modificar == "nombre":
            palabra = nombre
        elif parte_modificar == "apellido_paterno":
            palabra = apellido_paterno
        elif parte_modificar == "apellido_materno":
            palabra = apellido_materno
        else:
            palabra = segundo_nombre

        if len(palabra) == 0:
            continue  # Si la palabra a modificar es vacía, saltamos a la siguiente iteración

        for _ in range(random.randint(1, umbral_distancia)):
            indice = random.randint(0, len(palabra) - 1)
            nueva_letra = chr(random.randint(97, 122))  # Genera una letra aleatoria
            palabra = palabra[:indice] + nueva_letra + palabra[indice+1:]

        # Reconstruye el nombre completo con la parte modificada
        if parte_modificar == "nombre":
            partes_nombre[0] = palabra
        elif parte_modificar == "apellido_paterno":
            partes_nombre[1] = palabra
        elif parte_modificar == "apellido_materno":
            partes_nombre[2] = palabra
        else:
            partes_nombre[3] = palabra

        variante = " ".join(partes_nombre)
        if variante != nombre_completo:
            variantes.add(variante)
    return variantes

# Ejemplo de uso
nombre_completo = "Juan Pérez López"
num_variantes = 10
umbral_distancia = 2

variantes = generar_errores_similitud(nombre_completo, num_variantes, umbral_distancia)
print("Nombre completo original:", nombre_completo)
print("Variantes con errores de similitud:")
for variante in variantes:
    print(variante)
