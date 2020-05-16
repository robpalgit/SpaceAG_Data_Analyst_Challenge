# Coding Interview 2020-05-15

# 1) Soy palíndromo

# Escribir una función que recibe un string y evalúa si este se lee igual al derecho que al revez. 
# Esta propiedad significa que ese texto es un palíndromo. Esto no toma en cuenta capitalización ni espacios vacíos.

# Ejemplo: 
# Si el input es “Abba” debe retornar true.
# Si el input es “sator arepo tenet opera rotas" debe retornar true.
# Si el input es “Gilberto” debe retornar false

# Respuesta:

def soy_palindromo(palabra):
    palabra = palabra.lower()
    palabra.replace(' ', '')
    return palabra==palabra[::-1]

print(soy_palindromo('Abba'))
print(soy_palindromo('sator arepo tenet opera rotas'))
print(soy_palindromo('Gilberto'))


# 2) Ya he visto esa letra

# Escribir una función que recibe un string y retorna el primer carácter en repetirse. 
# Si no se repite ningún carácter retorna null.

# Ejemplo:
# Si el input es ‘Abnsba’ debe retornar ‘b’.
# Si el input es ‘Gilberto’ debe retornar null.

# Respuesta:

def ya_he_visto_esa_letra(palabra):
    palabra = palabra.lower()
    dict_conteo = {}
    for i in palabra:
        if i in dict_conteo:
            print(i)
            break
        else:
            dict_conteo[i] = 1
            
print(ya_he_visto_esa_letra('Abnsba'))
print(ya_he_visto_esa_letra('Gilberto'))


# 3) Cuantas islas hay en el océano?

# Escribir una función que recibe una matriz 2D que contiene sólo ceros o unos. 
# Los ceros representan el mar y los unos, tierra. Esta función retorna la cantidad de islas que hay. 
# Una isla es un conjunto de unos (uno o más) que están juntos.

# Ejemplo

# En la siguiente matriz hay 2 islas.

import numpy as np

matriz_2d = np.array([1,0,1,0,0,1,1,0,0,1,0,0,1,0,0,1]).reshape(4,4)
print(matriz_2d)

# Respuesta:

def contador_islas(matriz):   
    conteo = 0
    dim_x = matriz.shape[0]
    dim_y = matriz.shape[1]
    
    def detector(x, y):
        if 0 <= x < dim_x and 0 <= y < dim_y and matriz[x][y]==1:
            matriz[x][y] = 0
            detector(x, y+1)
            detector(x-1, y+1)
            detector(x-1, y)
            detector(x-1, y-1)
            detector(x, y-1)
            detector(x+1, y-1)
            detector(x+1, y)
            detector(x+1, y+1)
        
    for i in range(dim_x):
        for j in range(dim_y):
            if matriz[i][j]==1:
                conteo += 1
                detector(i, j)
        
    return conteo

print(contador_islas(matriz_2d))


