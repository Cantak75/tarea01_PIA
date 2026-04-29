def procesar_lista(lista):
    
    # 1. Eliminar números negativos
    positivos = [x for x in lista if x >= 0]
    
    # 2. Eliminar repetidos usando un set
    sin_repetidos = set(positivos)
    
    # 3. Ordenar de menor a mayor
    resultado = sorted(sin_repetidos)
    
    return resultado

lista = [4, -1, 2, 4, 3, -5, 2]

print(procesar_lista(lista))