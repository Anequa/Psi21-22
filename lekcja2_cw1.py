from typing import AsyncIterable


Lorem="Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie="ania"
nazwisko="ged "
litera_1 = imie[2]
litera_2= nazwisko[3]

def licz_litery(Lorem):

    letter=0
    letter2=0
    for char in Lorem:
        if char==litera_1:
            letter+=1
        elif char==litera_2:
            letter2+=1
    print(f"W tekście jest {letter} liter '{litera_1}' oraz {letter2} liter '{litera_2}'")
#or
ilosc=Lorem.count(litera_1)
ilosc2=Lorem.count(litera_2)
print(f"W tekście jest {ilosc} liter '{litera_1}' oraz {ilosc2} liter '{litera_2}'")
licz_litery(Lorem)