def busqueda_binaria(arreglo, inicio, fin, objetivo):
    # Caso base: si el inicio supera al fin, el elemento no está en el arreglo
    if inicio > fin:
        return -1
    
    # Calcular el punto medio
    medio = (inicio + fin) // 2
    
    # Si el elemento medio es el objetivo, devolver el índice
    if arreglo[medio] == objetivo:
        return medio
    
    # Si el objetivo es menor que el elemento medio, buscar en la mitad izquierda
    elif arreglo[medio] > objetivo:
        return busqueda_binaria(arreglo, inicio, medio - 1, objetivo)
    
    # Si el objetivo es mayor que el elemento medio, buscar en la mitad derecha
    else:
        return busqueda_binaria(arreglo, medio + 1, fin, objetivo)

# Ejemplo de uso
arreglo = [1, 3, 5, 7, 9, 11, 13, 15, 17]
objetivo = 7
resultado = busqueda_binaria(arreglo, 0, len(arreglo) - 1, objetivo)

if resultado != -1:
    print(f"Elemento encontrado en el índice {resultado}")
else:
    print("Elemento no encontrado")
