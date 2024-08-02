
#* Se tiene un número natural n, crear una función que retorne
#* una lista de todos los pares de números naturales que sumen
#* el número n.   n < 10^6


# Lo primero que se me ocurrio para visualizar los pares de numeros
# fue dar un ejemplo y analizarlo.
# n = 10 pares = [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)]
# Al analizar el ejemplo me di cuenta que los pares de numeros
# que suman n son todos los numeros naturales desde 1 hasta la mitad
# de n.

def get_pairs_list(n : int) -> list:
    """
    Esta funcion retorna una lista de todos los pares de numeros naturales
    que sumen el numero n.

    Argumentos:
        n (int) - Numero natural n.

    Retorna:
        Una lista de todos los pares de numeros naturales que sumen n.
    """

    # Para obtener los pares de numeros que suman n solo debo recorrer todos
    # los numeros naturales desde 1 hasta la mitad de n y restar n con el
    # numero actual para obtener el segundo numero del par.

    pares = []
    for i in range(1, n//2+1):
        pares.append((i, n-i))

    return pares

print(get_pairs_list(10))