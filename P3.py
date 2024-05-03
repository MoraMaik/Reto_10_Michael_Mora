def mov_ceros(arr):

    no_ceros = [x for x in arr if x != 0]  # lista con TODOS los elementos que NO son cero

    
    ceros = [x for x in arr if x == 0]     # lista con todos los ceros
    
    
    return no_ceros + ceros                # concatena las listas de no ceros y ceros

# ejem de uso:

arr = [0, 1, 0, 3, 12, 0]
resultado = mov_ceros(arr)

print(f"Arreglo con ceros al final: {resultado}")
