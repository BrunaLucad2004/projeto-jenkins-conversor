from src.conversor import fahrenheit_para_celsius, celsius_para_fahrenheit


def test_fahrenheit_para_celsius_ponto_congelamento():
    """32°F deve ser 0°C."""
    assert fahrenheit_para_celsius(32) == 0.0


def test_fahrenheit_para_celsius_ponto_ebulicao():
    """212°F deve ser 100°C."""
    assert fahrenheit_para_celsius(212) == 100.0


def test_celsius_para_fahrenheit_ponto_congelamento():
    """0°C deve ser 32°F."""
    assert celsius_para_fahrenheit(0) == 32.0


def test_celsius_para_fahrenheit_ponto_ebulicao():
    """100°C deve ser 212°F."""
    assert celsius_para_fahrenheit(100) == 212.0