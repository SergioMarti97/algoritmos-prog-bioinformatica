from itertools import *
from PracticasAlgoritmos import CalculaDX

L = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9, 10, 11, 12]
n = 7
m = L[len(L) - 1]

print("Puntos de corte que generan la lista de fragmentos:")
for combina in combinations(range(m + 1), n):
    if combina[0] == 0 and combina[len(combina) - 1] == m:
        if CalculaDX(combina) == L:
            print(combina)

