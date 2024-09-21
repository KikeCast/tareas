def sumar_numeros_pares(A, n):
    suma_pares = 0
    # Recorrer filas
    for i in range(n):
        # Recorrer columnas
        for j in range(n):
            # Verificar si el número es par
            if A[i][j] % 2 == 0:
                suma_pares += A[i][j]
    return suma_pares

# Ejemplo de uso
n = 3
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = sumar_numeros_pares(A, n)
print("La suma de los números pares es:", resultado)
