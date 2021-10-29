# zad1
# Stwórz funkcję, która jako parametry przyjmuje dwie listy a_list oraz b_list. Następnie zwróć listę,
# która będzie posiadać parzyste indeksy z listy a_list oraz nieparzyste z b_list.
def zwroc_naprzemian(a_list, b_list):
    lista = a_list.copy()
    list_len = len(lista)
    for i in range(1, list_len, 2):
        lista[i] = b_list[i]
        if i == len(a_list) - 1:
            lista.extend(b_list[list_len:])
    return lista


# zad2
# Stwórz funkcję, która przyjmuje parametr data_text, a następnie zwróci następujące informacje o parametrze w formie słownika (dict):
# length: długość podanego tekstu,
# letters: lista znaków w wyrazie np. ['D', 'o', 'g'],
# big_letters: zamieniony parametr w kapitaliki np. DOG
# small_letters: zamieniony parametr w małe litery np. dog
def foo(data_text):
    return {
        "length": len(data_text),
        "letters": list(data_text),
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower(),
    }


# zad3
# Stwórz funkcję, która przyjmie jako parametry text oraz letter, a następnie zwróci wynik usunięcia wszytkich wystąpień wartości w letter z tekstu text.
def delete_letter(sentence, letter):
    return sentence.replace(letter, "")


print(zwroc_naprzemian([0, 2, 4, 6], [1, 3, 5, 7, 9]))

print(foo("dogos"))

print(delete_letter("anabela tanczy tanczy aaa", "a"))
