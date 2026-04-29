import string

def contar_palabras(lista_palabras, ruta_fichero):
    # Crear diccionario con las palabras presentes en la lista con frecuencia = 0
    frecuencia_palabras = {palabra.lower(): 0 for palabra in lista_palabras}

    with open(ruta_fichero, "r", encoding="utf-8") as fichero:
        for linea in fichero:
            # 1. Eliminar signos de puntuación y pasar a minúsculas
            linea = linea.lower()
            linea = linea.translate(str.maketrans("", "", string.punctuation))
            
            palabras_linea = linea.split()
            
            # 2. Contar las palabras de la lista
            for palabra in palabras_linea:
                if palabra in frecuencia_palabras:
                    frecuencia_palabras[palabra] += 1

    return frecuencia_palabras


# ===== Programa de prueba =====
lista = ["python", "texto", "archivo", "palabra"]
ruta = "ejemplo.txt"

resultado = contar_palabras(lista, ruta)

# 3. Mostrar ordenado por palabra
for palabra in sorted(resultado):
    print(f"{palabra}: {resultado[palabra]}")