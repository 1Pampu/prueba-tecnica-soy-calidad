
#* Se tiene una matriz nxn de enteros, crear una función que
#* retorne un arreglo cuyo primer elemento es la cantidad de
#* numeros que aparecen solo una vez y cuyo segundo elemento
#* la cantidad de términos repetidos.
#* Ejemplos
#* [[2, 2], [2, 2]] - [0, 1]
#* [[2, 1, 3], [4, 5, 2], [6, 6, 6]] - [4, 2]


# Se me ocurrio que seria mas facil si separo la funcion en dos partes,
# una que se encargue de contar los numeros unicos y otra que se encargue
# de contar los repetidos y luego sumar los resultados en otra funcion.
# Luego intentare hacer la implementacion en una sola funcion.

def get_count_details(matriz : list) -> list:
    """
    Esta funcion cuenta la cantidad de numeros unicos y repetidos en una matriz nxn.

    Argumentos: matriz (list) - Matriz nxn de enteros.

    Retorna:
        Una lista con dos elementos:
        - El primer elemento es la cantidad de numeros que aparecen solo una vez.
        - El segundo elemento es la cantidad de numeros que aparecen mas de una vez.
    """

    # Lo primero que se me ocurrio fue hacer una lista para guardar todos los
    # numeros y otra lista que almacene el conteo de cada numero para luego filtrar
    # cuantos numeros no repetidos hay. Otra opcion seria usar un diccionario
    # para almacenar los numeros y su conteo en una unica variable.

    numeros_list = []
    conteo = []

    # Luego solo debo recorrer la matriz y verificar si el numero que se esta
    # iterando ya esta en la lista de numeros, si no esta se agrega y se suma
    # uno al conteo, si ya esta se suma uno al conteo de ese numero revisando
    # cual es su index.

    for fila in matriz:
        for numero in fila:
            if numero not in numeros_list:
                numeros_list.append(numero)
                conteo.append(1)
            else:
                conteo[numeros_list.index(numero)] += 1

    # Finalmente solo debo contar cuantos numeros tienen un conteo de 1
    # para saber cuantos numeros unicos hay en la matriz y retornarlo.
    # En este punto me di cuenta que no solo tengo el conteo de los numeros
    # unicos, sino tambien el conteo de los numeros repetidos, por lo que
    # solo debo agregar otro contador para los numeros repetidos y retornar ambos.

    unicos = 0
    repetidos = 0
    for numero in conteo:
        if numero == 1:
            unicos += 1
        else:
            repetidos += 1

    return [unicos, repetidos]

ejemplo1 = [[2, 2], [2, 2]]
resultado1 = get_count_details(ejemplo1)
print(f'{ejemplo1} - {resultado1}')

ejemplo2 = [[2, 1, 3], [4, 5, 2], [6, 6, 6]]
resultado2 = get_count_details(ejemplo2)
print(f'{ejemplo2} - {resultado2}')