# Reto_10_Michael_Mora
Desarrollo reto 10, segun lo aprendido en clase de Arreglos y listas.

*(Al final de cada codigo dejo una breve explicacion si miro que es necesario)*

_______________________________
## **Punto 1**

**Instrucciones:** Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.


```python
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
```
### Explicacion P1:

+ **Funcion `calcular_promedio`**: Esta funcion toma una lista llamada `numeros`.
+ **Verificacion de lista vacia**: Antes de realizar cualquier calculo, el codigo verifica si la lista esta vacia para prevenir errores de division por cero.
+ **Calculo del promedio**:
`sum(numeros)`: Suma todos los elementos de la lista.
`len(numeros)`: Cuenta la cantidad de elementos en la lista.
Divide la suma total por la cantidad de elementos para obtener el promedio.
+ **Ejemplo de uso**: Se define una lista de numeros reales y se llama a la funcion `calc_promedio` para obtener y mostrar el promedio.

_______________________________
## **Punto 2**

**Instrucciones:** Desarrollar un algoritmo que calcule el producto punto de dos arreglos de numeros enteros (reales) de igual tamaño.
Nota: se me hizo mas sencillo el reto por estar mirando Algebra Lineal al tiempo.

```python
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
```

### Explicacion P2:

+ **Funcion `producto_punto`**: Toma dos listas (`arr1` y `arr2`) como argumentos.
+ **Verificacion de tamaño**: Comprueba si los arreglos tienen el mismo tamaño. Si no es asi, la funcion retorna `None`.
+ **Calculo del producto punto**:
`zip(arr1, arr2)`: Combina los elementos de ambos arreglos en pares.
`sum(x * y for x, y in zip(arr1, arr2))`: Genera los productos de los elementos correspondientes y luego suma estos productos.
+ **Ejemplo de uso**: Define dos arreglos y llama a la funcion `producto_punto` para calcular y mostrar el resultado. Se maneja el caso en que los arreglos no sean del mismo tamaño.

_______________________________
## **Punto 3**

**Instrucciones:** Hacer un algoritmo que deje al final de un arreglo de numeros todos los ceros que aparezcan en dicho arreglo.

```python
def mov_ceros(arr):

    no_ceros = [x for x in arr if x != 0]  # lista con TODOS los elementos que NO son cero

    
    ceros = [x for x in arr if x == 0]     # lista con todos los ceros
    
    
    return no_ceros + ceros                # concatena las listas de no ceros y ceros

# ejem de uso:

arr = [0, 1, 0, 3, 12, 0]
resultado = mov_ceros(arr)

print(f"Arreglo con ceros al final: {resultado}")
```

### Explicacion P3:
+ **Funcion `mov_ceros`**: Esta funcion acepta una lista `arr` como argumento.
+ **Lista `no_ceros`**: Utiliza list comprehension para crear una lista de todos los elementos en arr que no son cero.
+ **Lista `ceros`**: Utiliza otra list comprehension para recolectar todos los ceros del arreglo.
+ **Retorno**: Retorna la concatenacion de las listas `no_ceros` y `ceros`, poniendo asi todos los ceros al final del arreglo original.
+ **Ejemplo de uso**: Define un arreglo de ejemplo y muestra el resultado despues de aplicar la funcion.

_______________________________
## **Punto 4**

**Instrucciones:** Revisar que son los algoritmos de sorting, entender bubble-sort ([enlace a implementacion](http://https://www.geeksforgeeks.org/bubble-sort/ "enlace a implementacion")).

**Mi explicacion**:

Los algoritmos de *sorting*, o algoritmos de ordenamiento, son tecnicas que se utilizan para *reordenar elementos* en una secuencia (como una lista o un arreglo) en un orden especifico, generalmente ascendente o descendente

+ Bubble sort

El algoritmo de Bubble Sort, o "ordenamiento de burbuja", es uno de los metodos de ordenamiento mas sencillos pero menos eficientes en terminos de tiempo de ejecucion, especialmente para listas grandes. La idea basica detras de Bubble Sort es:

1. Comparar pares de elementos adyacentes en la lista o arreglo.
2. Intercambiarlos si estan en el orden incorrecto.
3. Repetir el proceso para cada par de la lista, recorriendola varias veces hasta que no se necesiten mas intercambios, lo que significa que la lista esta ordenada.

_______________________________
FIN RETO.

