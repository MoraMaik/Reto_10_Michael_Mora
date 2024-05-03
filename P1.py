def calcular_promedio(numeros):
    if not numeros:  # verifica si la lista esta vacia
        return 0  # retorna 0 si la lista esta vacia para evitar una division por cero
    
    suma_total = sum(numeros)  # suma todos los elementos de la lista

    cant_numeros = len(numeros)  # obtiene la cantidad de numeros en la lista
    
    promedio = suma_total / cant_numeros  # calcula el promedio

    
    return promedio

# ejem de uso:
numeros = [10.5, 20.3, 15.2, 5.5, 30.8]  # lista de numeros reales
resultado = calcular_promedio(numeros)
print(f"El promedio de los numeros es: {resultado}")
