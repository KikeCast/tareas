def eliminar_duplicados(nums):
    # Si el arreglo está vacío, retornamos 0
    if not nums:
        return 0
    
    # Inicializamos K con 1, ya que el primer elemento es siempre único
    K = 1
    
    # Recorremos el arreglo desde el segundo elemento
    for i in range(1, len(nums)):
        # Si encontramos un número único, lo movemos a la posición K
        if nums[i] != nums[K - 1]:
            nums[K] = nums[i]
            K += 1
    
    # Retornamos el número de elementos únicos
    return K

# Ejemplo de uso
nums = [1, 1, 2, 2, 3, 4, 4, 5]
K = eliminar_duplicados(nums)
print(f"Número de elementos únicos: {K}")
print(f"Arreglo con elementos únicos: {nums[:K]}")
