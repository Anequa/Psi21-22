# Stwórz funkcję, która przelicza temperaturę w stopniach Celsjusza na Fahrenheit, Rankine, Kelvin.
# Typ konwersji powinien być przekazany w parametrze temperature_type i uwzględniać błędne wartości.


def convert_temperature_to(temperature_type, value):
    try:
        return {
            "Fahrenheit": value * 9 / 5 + 32,
            "Rankine": value + 491.67,
            "Kelvin": value + 273.15,
        }[temperature_type]
    except TypeError:
        return "Niewłaściwa wartość temperatury"
    except KeyError:
        return "Niewłaściwy typ"


print(convert_temperature_to("Rankine", 0))
print(convert_temperature_to("Fahrenheit", 0))
print(convert_temperature_to("Kelvin", 0))
print(convert_temperature_to("Kot", 0))
