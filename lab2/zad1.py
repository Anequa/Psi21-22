# Stwórz funkcję, która jako parametry przyjmuje dwie listy a_list oraz b_list. Następnie zwróć listę,
# która będzie posiadać parzyste indeksy z listy a_list oraz nieparzyste z b_list.


def zwroc_naprzemian(a_list, b_list):
    lista = []
    for i in range(len(max(a_list, b_list))):
        if len(a_list) != 0:
            lista.append(a_list.pop(0))
        if len(b_list) != 0:
            lista.append(b_list.pop(0))
    return lista


tab = zwroc_naprzemian([0, 2, 4, 6], [1, 3, 5, 7, 9])
print(tab)
