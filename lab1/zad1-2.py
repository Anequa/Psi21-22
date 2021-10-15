sentence = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Weronika"
nazwisko = "Krejner"
print(
    "W tekście jest {0} liter '{2}' oraz {1} liter '{3}'".format(
        sentence.count(imie[2]),
        sentence.count(nazwisko[3]),
        imie[2],
        nazwisko[3],
    )
)
