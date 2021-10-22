# Stwórz funkcję, która przyjmuje parametr data_text, a następnie zwróci następujące informacje o parametrze w formie słownika (dict):

# length: długość podanego tekstu,

# letters: lista znaków w wyrazie np. ['D', 'o', 'g'],

# big_letters: zamieniony parametr w kapitaliki np. DOG

# small_letters: zamieniony parametr w małe litery np. dog


def foo(data_text):
    return {
        "length": len(data_text),
        "letters": list(data_text),
        "big_letters": data_text.capitalize(),
        "small_letters": data_text.lower(),
    }


print(foo("dogos"))
