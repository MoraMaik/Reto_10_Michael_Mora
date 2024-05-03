def producto_punto(arr1, arr2):

    if len(arr1) != len(arr2):  # verifica que ambos arreglos tengan el mismo tamaño

        return None  # retorna None si los arreglos no son del mismo tamaño 
    
    resultado = sum(x * y for x, y in zip(arr1, arr2))  # calcula el producto punto
    return resultado

# ejem uso:
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

resultado = producto_punto(arr1, arr2)

if resultado is not None:
    print(f"El producto punto de las listas es: {resultado}")

else:
    print("Las listas deben tener el mismo tamaño.")
