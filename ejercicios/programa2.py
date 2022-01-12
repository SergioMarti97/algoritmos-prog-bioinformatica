import PracticasAlgoritmos as pa


# --- FUNCIONES --- #
def show_test_case(num_cut_points, distances):
    print('-'*50)
    print(f"Datos de entrada:\nn = {num_cut_points}\nDX = {distances}")
    print(f"Resultado:\nS = {pa.MapaRestriccionesBusquedaExhaustivaMax(num_cut_points, distances)}")
    print('')


# --- PROGRAMA --- #
test_data = [
    (7, [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9, 10, 11, 12]),
    (3, [2, 3, 5])
]

for data in test_data:
    show_test_case(num_cut_points=data[0], distances=data[1])
