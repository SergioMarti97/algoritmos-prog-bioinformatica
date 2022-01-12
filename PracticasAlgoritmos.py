# Líbrería/Módulo PracticasAlgoritmos.py
from itertools import *


def CalculaDX(posCortes):
    """
    Obtener la lista de tamaños de fragmentos de DNA
    a partir de la lista de posiciones de puntos de
    o sitios de restricción en la secuencia de DNA.
    :param posCortes: lista de las posiciones de los puntos de restricción
    :return: lista de los tamaños de los fragmentos de DNA después de tratar
    con las enzimas de restricción
    """
    dist = []
    for i in range(len(posCortes)):
        for j in range(i + 1, len(posCortes)):
            dist.append(posCortes[j] - posCortes[i])

    dist.sort()

    return dist


def MapaRestriccionesBusquedaExhaustivaMax(n, lengths):
    """
    Determina las posiciones de los puntos de corte en una secuencia
    de DNA a partir de la lista de fragmentos obtenida tras un tratamiento
    con enzimas de restricción y una electroforesis en gel.
    Obtiene las soluciones intentando máximizar el tamaño de los fragmentos

    :param n: numero de puntos de corte. Inclye la posición de inicio 0 y la posición
    final (el máximo tamaño de un fragmento)
    :param lengths: lista de enteros que representa las longitudes de los fragmentos
    producidos tras tratar con enzimas de restricción y electroforesis en gel la secuencia de DNA.
    Corresponde con el conjunto de todos los pares de distancias entre puntos
    que contiene n * (n - 1) / 2 enteros
    :return: una lista con las soluciones que contengan el punto de corte más cercano
    a M, de todas las soluciones posibles. Cada solución es una lista de posiciones
    de puntos de corte o sitios de restricción en la secuencia de DNA
    """
    s = [] # la solución
    m = lengths[len(lengths) - 1]
    for combina in combinations(range(m + 1), n):
        # Filtramos las combinaciones para quedarnos con solo los candidatos que cumplen
        # que su primer elemento es 0 y su último elemento es 'm'.
        if combina[0] == 0 and combina[n - 1] == m:
            # Comprobamos que este candidato cumple que los fragmentos que genera son
            # los mismos que pasamos por parámetro
            distances = CalculaDX(combina)
            if distances == lengths:
                # Si el penultimo elemento de la combinación es más próximo a 'm', limpiamos
                # las soluciones, ya que no son buenas
                if len(s) > 0:  # se podría hacer con un assert
                    if s[0][n - 2] < distances[len(distances) - 2]:
                        s.clear()
                # Añadimos el elemento
                s.append(combina)

    return s


def make_identity(length):
    """
    Construye la secuencia de genes identidad, es decir,
    la lista de elementos ordenados de menor a mayor,
    empezando en 1
    :param length: el tamaño de la secuencia de elementos desordenados
    :return: una nueva lista con los elementos ordenados
    de la lista 'permutation'
    """
    return list(range(1, length + 1))


def left_prefix(pi, original):
    """
    Devuelve el indice del primer elemento desordenado por la izquierda
    Devuelve 'n' si esta ordenado
    :param pi: la lista de elementos desordenados
    :param original: la lista original de elementos
    :return: el índice del primer elemento por la izquierda ordenado
    """
    length = 0

    while length < len(pi) and pi[length] == original[length]:
        length += 1

    return length


def right_prefix(pi, original):
    """
    Devuelve el indice del primer elemento desordenado por la derecha
    Devuelve -1 cuando la lista permutation esta ordenada
    :param pi: la lista de elementos desordeados
    :param original: la lista original de elementos
    :return: el índice del primer elemento por la derecha ordenado
    """
    length = len(pi) - 1

    while length >= 0 and pi[length] == original[length]:
        length -= 1

    return length


def do_permutation(pi, pos1, pos2):
    """
    Esta función realiza una permutacion de los elementos
    de la lista 'permutation' de los elementos entre la
    posicion 'pos1' y la posición 'pos2'
    Modifica el objeto 'permutation' pasado por parametro
    :param pi: la lista de elementos
    :param pos1: posición 1
    :param pos2: posición 2
    """
    sub_list = pi[pos1:pos2 + 1]
    sub_list.reverse()
    for i in range(pos1, pos2 + 1):
        pi[i] = sub_list[i - pos1]


def find_left_permutations(pi, identity, n):
    """
    Busqueda de izquierda a derecha las permutaciones
    de la lista permutation para obtener la lista identity
    :param pi: lista desordenada
    :param identity: lista ordenada
    :param n: tamaño de la lista
    :return: una lista de tuplas con las permutaciones para ordenar 'permutation'
    """
    left_permutations = []
    while True:
        tOrdInicial = left_prefix(pi, identity)

        if tOrdInicial >= n:
            break

        i = 0
        for i in range(tOrdInicial, n):
            if pi[i] == identity[tOrdInicial]:
                break

        left_permutations.append((tOrdInicial, i))
        do_permutation(pi, tOrdInicial, i)

    return left_permutations


def find_right_permutations(pi, identity):
    """
    Busqueda de derecha a izquierda las permutaciones de la
    lista permuttion para obtener la lista identity
    :param pi: la lista desordenada
    :param identity: lista ordenada
    :return: una lista de tuplas con las permutaciones
    """
    right_permutations = []
    while True:
        tOrdInicial = right_prefix(pi, identity)

        if tOrdInicial < 0:
            break

        i = tOrdInicial
        for i in range(tOrdInicial, -1, -1):
            if pi[i] == identity[tOrdInicial]:
                break

        right_permutations.append((i, tOrdInicial))
        do_permutation(pi, i, tOrdInicial)

    return right_permutations


def which_is_best(left_permutations, right_permutations):
    """
    Devuelve la mejor lista de permutaciones entre la izquierda y la derecha
    La mejor lista es la lista con menos permutaciones, y si son iguales,
    la lista con permutaciones más cortas, es decir: cuyas diferencias entre
    las posiciones iniciales y las posiciones finales de cada permutación son
    más pequeñas
    :param left_permutations: las permutaciones por el lado de la izquierda
    :param right_permutations: las permutaciones por el lado de la derecha
    :return: devuelve la mejor de las dos listas de permutaciones pasadas por parametro
    """
    if len(left_permutations) < len(right_permutations):
        return left_permutations
    elif len(left_permutations) > len(right_permutations):
        return right_permutations
    else:
        sum_dist_left = 0
        for p_left in left_permutations:
            sum_dist_left += p_left[1] - p_left[0]

        sum_dist_right = 0
        for p_right in right_permutations:
            sum_dist_right += p_right[1] - p_right[0]

        if sum_dist_left <= sum_dist_right:
            return left_permutations
        else:
            return right_permutations


def OrdenacionInversionSimple(permutacionInicial):
    """
    Resolver el problema de Ordenación por Inversión mediante avance rápido
    :param permutacionInicial: lista de enteros que representa un segmento genómico
    :return: la lista de inversiones que permiten obtener la permutación identity
    a partir de la permutación inicial
    """
    n = len(permutacionInicial)
    identity = make_identity(n)

    left_permutations = find_left_permutations(permutacionInicial.copy(), identity, n)
    print(f"Permutaciones izquierda: {left_permutations}")

    right_permutations = find_right_permutations(permutacionInicial.copy(), identity)
    print(f"Permutaciones derecha: {right_permutations}")

    return which_is_best(left_permutations, right_permutations)


def do_permutations(list_permutations, pi):
    """
    Ejecuta todas las permutaciones contenidas en la lista de
    permutaciones para transformar la lista 'permutation'
    Modifica el objeto 'permutation'
    :param list_permutations: lista de permutaciones, representadas por tuplas
    :param pi: lista desordenada
    :return: 'permutation' modificado según las permutaciones pasadas por parametro
    """
    for permutation in list_permutations:
        do_permutation(pi, permutation[0], permutation[1])

    return pi
