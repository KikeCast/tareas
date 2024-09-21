def candles(candles: list[int]) -> int:
    # Encontrar la altura máxima de las velas
    max_altura = max(candles)
    
    # Contar cuántas velas tienen esa altura máxima
    contador = 0
    for vela in candles:
        if vela == max_altura:
            contador += 1
    
    # Retornar el número de velas más altas
    return contador

# Pruebas
print(candles([4, 4, 1, 3]))  # Debe devolver 2
print(candles([1, 1, 1, 1, 1]))  # Debe devolver 5
