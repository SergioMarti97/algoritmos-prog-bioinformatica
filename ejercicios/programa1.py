import PracticasAlgoritmos as pa


# --- FUNCIONES --- #
def show_test_case(cut_points):
    print('-'*50)
    print(f"Datos de entrada: {cut_points}")
    print(f"Resultado: {pa.CalculaDX(cut_points)}")
    print('')


# --- PROGRAMA --- #
test_data = [
    [0, 6, 7, 8, 9, 11, 12],
    [0, 4, 5]
]

for cut_points in test_data:
    show_test_case(cut_points)
