def operaciones_conjuntos(lista1, lista2):
    # Convertir listas a conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    resultado = {
        "interseccion": conjunto1 & conjunto2,
        "union": conjunto1 | conjunto2,
        "diferencia_simetrica": conjunto1 ^ conjunto2
    }

    return resultado

lista_a = [1, 2, 3, 4, 5]
lista_b = [1, 4, 5, 5, 6, 7]

resultado = operaciones_conjuntos(lista_a, lista_b)

# ===== Programa de prueba =====
print("Intersección:", resultado["interseccion"])
print("Unión:", resultado["union"])
print("Diferencia simétrica:", resultado["diferencia_simetrica"])

# =====Salida esperada: =====
'''
Intersección: {1, 4, 5}
Unión: {1, 2, 3, 4, 5, 6, 7}
Diferencia simétrica: {2, 3, 6, 7}
'''