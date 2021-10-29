# zad5
class Calculator:
    """Klasa Calculator, posiada funkcje add, difference, multiply, divide"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def difference(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


# zad6
# Stwórz klasę ScienceCalculator, która dziedziczy po klasie Calculator i dodaj dodatkowe funkcje np. potęgowanie.
class ScienceCalculator(Calculator):
    """Klasa ScienceCalculator, dziedziczy po klasie Calculator oisiada funkcję power."""

    def power(self):
        return pow(self.a, self.b)


kalkulator = Calculator(1, 5)
print(kalkulator.add())
print(kalkulator.difference())
print(kalkulator.multiply())
print(kalkulator.divide())

kalkulator2 = ScienceCalculator(3, 2)
print(kalkulator2.add())
print(kalkulator2.difference())
print(kalkulator2.multiply())
print(kalkulator2.divide())
print(kalkulator2.power())
