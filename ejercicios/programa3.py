import PracticasAlgoritmos as pa


# --- FUNCIONES --- #
def show_sorting_process(permutations, pi):
    print(pi)
    for i in range(len(permutations)):
        print(f"Permutación {i + 1}: inicio {permutations[i][0]}, fin {permutations[i][1]}")
        pa.do_permutation(pi, permutations[i][0], permutations[i][1])
        print(pi)


def show_test_case(pi):
    print('-'*50)
    print(f"pi: {pi}\n")

    permutations = pa.OrdenacionInversionSimple(pi)
    print(f"\npermutaciones: {permutations}\ndistancia de permutación: {len(permutations)}\n")

    print(f"--- Proceso de ordenación ---")
    show_sorting_process(permutations, pi)
    print('')


# --- PROGRAMA --- #

# datos de entrada
pis = [
    [1, 2, 3, 6, 4, 5],
    [6, 1, 2, 3, 4, 5],
    [3, 4, 2, 1, 5, 6, 7, 10, 9, 8]
]

# resolvemos para cada lista de datos de entrada
for pi in pis:
    show_test_case(pi)
