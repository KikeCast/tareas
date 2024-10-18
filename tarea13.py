def es_palindromo(x):
    # Guardamos el número original
    original = x
    invertido = 0
    
    # Invertimos el número
    while x > 0:
        digito = x % 10  # Extraer el último dígito
        invertido = invertido * 10 + digito  # Formar el número invertido
        x = x // 10  # Remover el último dígito del número original
    
    # Comparamos el número original con su versión invertida
    return invertido == original

# Ejemplo de uso
x = 121
if es_palindromo(x):
    print(f"{x} es un palíndromo.")
else:
    print(f"{x} no es un palíndromo.")
