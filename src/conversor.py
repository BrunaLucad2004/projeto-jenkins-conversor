def fahrenheit_para_celsius(fahrenheit):
    """Converte uma temperatura de Fahrenheit para Celsius."""
    celsius = (fahrenheit - 32) * 5 / 8
    return round(celsius, 2)


def celsius_para_fahrenheit(celsius):
    """Converte uma temperatura de Celsius para Fahrenheit."""
    fahrenheit = (celsius * 8 / 5) + 32
    return round(fahrenheit, 2)