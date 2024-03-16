import random

def seleccionar_nombres(input_file):
    nombres_seleccionados = {}
    with open(input_file, 'r') as file:
        for line in file:
            nombre = line.strip()
            inicial = nombre[0].upper()
            if inicial.isalpha():
                if inicial not in nombres_seleccionados:
                    nombres_seleccionados[inicial] = []
                nombres_seleccionados[inicial].append(nombre)

    nombres_finales = {}
    for inicial, nombres in nombres_seleccionados.items():
        random.shuffle(nombres)
        nombres_finales[inicial] = nombres[:7]

    return nombres_finales

def guardar_nombres(output_file, nombres):
    with open(output_file, 'w') as file:
        for inicial, nombres_lista in nombres.items():
            for nombre in nombres_lista:
                file.write(nombre + '\n')

# Nombre del archivo de entrada
input_file = 'name_variant_hackathon.txt'
# Nombre del archivo de salida
output_file = 'nombres_seleccionados.txt'

# Seleccionar nombres y guardar en el archivo de salida
nombres_seleccionados = seleccionar_nombres(input_file)
guardar_nombres(output_file, nombres_seleccionados)

print("Nombres seleccionados guardados en", output_file)
