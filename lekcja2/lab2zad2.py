def zadanie2(data_text):
    return{
        "length":len(data_text),
        "letters":list(data_text),
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower(),
    }
a="ania"
print(zadanie2(a))
