


def convert_temperature_to(temperature_type, value):
    try:
        return {
            "Fahrenheit": value * 9 / 5 + 32,
            "Rankine": value + 491.67,
            "Kelvin": value + 273.15,
        }[temperature_type]
    except KeyError:
        return "Niewłaściwy typ"

print(convert_temperature_to("Fahrenheit",10))