# zad3
# 5 wybranych przykładów formatowania ciągów oznaczonego jako „New”,
# których nie było w przykładach z tego podrozdziału
# (np. z wyrównaniem, ilością pozycji liczby, znakiem itp.).


class Data(object):
    def __str__(self):
        return "str"

    def __repr__(self):
        return "repr"


print("{} {}".format("one", "two"))
print("{0!s} {0!r}".format(Data()))
print("{:>10}".format("test"))
print("{:_<10}".format("test"))
print("{:04d}".format(42))

# zad4
zmienna_typu_string = "porem Ipsum jest tekstem stosowanym"

print(dir(zmienna_typu_string))
help(zmienna_typu_string.capitalize())
